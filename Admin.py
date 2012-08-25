import web
#from urlparse import urlparse, parse_qsl
from google.appengine.ext import db
from DatabaseEntities.User import User

urls = (
    '/Add_User', 'Add_User',
    '', 'Admin',
)

admin = web.application(urls, locals())

# Error codes for admin page are:
# 0 - nothing is wrong
# 1 - user is already created and stored

class Admin():
    def GET(self, error = 0):
        #parsed_url = urlparse(web.ctx.fullpath)
        #args       = dict(parse_qsl(parsed_url.query))
        #try:
            #error = args['error']
        #except KeyError:
            #pass
        return web.ctx.render.admin(int(error))

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
            raise web.seeother('?error=0')
        else:
            raise web.seeother('?error=1')
