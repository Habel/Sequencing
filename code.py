import web
from google.appengine.api import users
from gaesessions import get_current_session
import Login
import Sequencing
import Admin

urls = (
    '/', 'Index',
    '/login', Login.login,
    '/sequencing', Sequencing.sequencing,
    '/logout', 'Logout', #just a hack until i feel like putting in real logout
    '/admin', Admin.admin
)

app = web.application(urls, locals())

render = web.template.render('templates/', base="base")
#db     = web.database(dbn="sqlite", db="manipdb")

def session_hook():
    #web.ctx.db      = db
    web.ctx.render  = render

app.add_processor(web.loadhook(session_hook))

class Index():
    def GET(self):
        session = get_current_session()
        if session.is_active() and session['login'] == 1:
            return web.seeother('/sequencing')
        else:
            return web.seeother('/login')

class Logout():
    def GET(self):
        session = get_current_session()
        session['login'] = 0
        raise web.seeother('/')

app = app.gaerun()
