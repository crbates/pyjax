# Demonstration of python + cherrypy + ajax + flot

This repository is for exploring using the javascript plotting library flot in an environment where the data being plotted is updated by calling a python function that returns updated data. The current version updates a histogram at a user specified rate. The long term goal is to have the data be a live plot of raw or processed instrument data. 

Usage:  
After cloning this repository run the ajax_app.py script. Then navigate to localhost:8080 on your web browser. The current version updates the data based on the javascript calls so having multiple clients attached may cause non-deterministic behavior.
