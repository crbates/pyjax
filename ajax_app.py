"""
This is a simple demo of a live histogram on webpage updated by python.

This cherrypy server starts a web page on localhost:8080. When a user opens 
the page the page displays a plot of a normal distribution that is updated
at the refresh rate specified. This is done by calling a jquery post command
which cherrypy handles and returns a json object containing new data for the 
plot.
 
"""
import cherrypy
import os
import json
import numpy as np

#add the directory where jquery and flot are located
MEDIA_DIR = os.path.join(os.path.abspath("."), u"media")

class AjaxApp(object):
    #set an initial value for the plot data
    y = np.zeros(300)
    
    #expose the basic index page
    @cherrypy.expose
    def index(self):
        return open(os.path.join(MEDIA_DIR, u'index.html'))

    #expose the submit command(called by jquery) and have it return the 
    #updated histogram
    @cherrypy.expose
    def submit(self,name):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        y = np.random.normal(50,25,300)
        self.y = self.y + np.histogram(y,300)[0]
        return json.dumps(dict(title=name,val = self.y.tolist()))

#setup the cherrypy server configuration to have access to flot and jquery
config = {'/media':
                {'tools.staticdir.on': True,
                 'tools.staticdir.dir': MEDIA_DIR,
                }
        }

cherrypy.quickstart(AjaxApp(),config=config)
