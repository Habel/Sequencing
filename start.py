import web
import Login
import Sequencing

urls = (
    '/', 'Index',
    '/login', Login.login,
    '/sequencing', Sequencing.sequencing,
    '/logout', 'Logout', #just a hack until i feel like putting in real logout
)

app = web.application(urls, locals())

if web.config.get("_session") is None:
    session = web.session.Session(app, web.session.DiskStore('sessions'), {"login": 0, "privilege": 0})
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/', base="base")
db     = web.database(dbn="sqlite", db="manipdb")

def session_hook():
    web.ctx.session = session
    web.ctx.db      = db
    web.ctx.render  = render

app.add_processor(web.loadhook(session_hook))

def logged_in():
    return True if session.login == 1 else False

class Index():
    def GET(self):
        if logged_in():
            web.seeother('/sequencing')
        else:
            web.seeother('/login')

class Logout():
    def GET(self):
        session.login = 0
        raise web.seeother('/')

if __name__ == "__main__":
    app.run()
