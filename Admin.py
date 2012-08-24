import web
from google.appengine.ext import db
from DatabaseEntities.User import User

urls = (
    '', 'Admin',
    '/', 'Admin',
    '/Add_User', 'Add_User',
)

admin = web.application(urls, locals())

# Error codes for admin page are:
# 0 - nothing is wrong
# 1 - user is already created and stored

class Admin():
    def GET(self):
        return web.ctx.render.admin(0)

class Add_User():
    def POST(self):
        i = web.input()
        # getting the inputs
        name = i.username
        pw   = i.password
        privilege = int(i.privilege)

        # checking if the user is already created
        user = db.GqlQuery("SELECT * FROM User WHERE name=:1", name).get()
        if(user == None):
            User(name = name, pw = pw, privilege = privilege).put()

        return web.ctx.render.admin(1)
