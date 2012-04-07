"""
ajax_app.py

Demo of AJAX using:
	- cherrypy
	- simplejson
	- jquery
"""
import cherrypy
import webbrowser
import os
import simplejson
import sys
sys.path.append('../libraries')
from generic.maestrofile import maestrofile
import numpy as np
MEDIA_DIR = os.path.join(os.path.abspath("."), u"media")

class AjaxApp(object):
    y = np.zeros(300)
    livetime = 0
    @cherrypy.expose
    def index(self):
        return open(os.path.join(MEDIA_DIR, u'index.html'))
        
    @cherrypy.expose
    def upload(self, myFile):
        f = open('temp.spe','wb')
        f.write(myFile.file.read())
        f.close()
        mf = maestrofile('temp.spe')
        self.y = mf.counts
        self.livetime = mf.livetime
        return open(os.path.join(MEDIA_DIR, u'index.html'))

    @cherrypy.expose
    def submit(self,name):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        #y = np.random.normal(50,25,300)
        #self.y = self.y + np.histogram(y,300)[0]
        return simplejson.dumps(dict(title=name,val = list(self.y),livetime=self.livetime))

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
cherrypy.quickstart(AjaxApp(),config=config)
