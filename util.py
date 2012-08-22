import web

def get_session():
    if web.config.get("_session") is None:
        session = web.session.Session(main_app, web.session.DiskStore('sessions'),
                                    {"login": 0, "privilege": 0})
        return session
    else:
        return web.config._session
