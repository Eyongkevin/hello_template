from templates import app

#app.debug = True
app.config.from_object('configurations.DevelopmentConfig')
app.run()


