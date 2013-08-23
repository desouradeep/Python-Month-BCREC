import fbconsole
fbconsole.AUTH_SCOPE = ['publish_actions']
fbconsole.authenticate()
fbconsole.post('/me/feed', {'message':'Python Rocks!!!'})
fbconsole.logout()
