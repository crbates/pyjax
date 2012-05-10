"""
This is a simple 

Demo of AJAX using:
	- cherrypy
	- simplejson
	- jquery
	- flot
"""
import cherrypy
import os
import json
import numpy as np

MEDIA_DIR = os.path.join(os.path.abspath("."), u"media")

class AjaxApp(object):
    y = np.zeros(300)
    
    @cherrypy.expose
    def index(self):
        return open(os.path.join(MEDIA_DIR, u'index.html'))

    @cherrypy.expose
    def submit(self,name):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        y = np.random.normal(50,25,300)
        self.y = self.y + np.histogram(y,300)[0]
        return json.dumps(dict(title=name,val = self.y.tolist()))

config = {'/media':
                {'tools.staticdir.on': True,
                 'tools.staticdir.dir': MEDIA_DIR,
                }
        }

#def open_page():
#    webbrowser.open("http://127.0.0.1:8080/")
#cherrypy.engine.subscribe('start', open_page)
#cherrypy.tree.mount(AjaxApp(), '/', config=config)
#cherrypy.engine.start()
#cherrypy.quickstart(AjaxApp())
cherrypy.quickstart(AjaxApp(),config=config)
