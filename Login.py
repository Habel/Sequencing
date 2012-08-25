import web
from google.appengine.ext import db
from gaesessions import get_current_session
from DatabaseEntities import User

urls = (
    '', 'Login',
)

login = web.application(urls, locals())

class Login():
    def GET(self):
        session = get_current_session()
        if session.is_active() and session['login'] == 1:
            raise web.seeother('/', absolute=True)
        else:
            return web.ctx.render.login(0)
    def POST(self):
        i = web.input()
        username = i.username
        password = i.password

        """
        error codes:
            1 - bad username
            2 - bad password
        """
        user = db.GqlQuery("SELECT * FROM User WHERE name=:1", username).get()
        if user == None:
            return web.ctx.render.login(1)
        elif user.pw != password:
            return web.ctx.render.login(2)

        session = get_current_session()
        session['privilege'] = user.privilege
        session['login'] = 1

        raise web.seeother('/', absolute=True)

