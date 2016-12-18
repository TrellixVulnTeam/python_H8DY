#!flask/bin/python

from app import app
app.jinja_loader.searchpath[0] = app.root_path + '\\..\\templates'
app.debug = True
app.run(host='0.0.0.0', port=8000)