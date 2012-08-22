import web

urls = (
    '', 'Login',
)

login = web.application(urls, locals())

class Login():
    def GET(self):
        if web.ctx.session.login == 1:
            raise web.seeother('/', absolute = True)
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

        db = web.ctx.db
        user = list(db.select('users', where="name='" + username + "'"))
        if len(user) == 0:
            return web.ctx.render.login(1)

        info = user[0]
        if info.password != password:
            return web.ctx.render.login(2)

        web.ctx.session.login = 1;
        web.ctx.session.privilege = info.privilege
        raise web.seeother('/', absolute=True)

