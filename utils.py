from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.api import memcache

import jinja2
import logging
import json
import os

class BaseHandler(webapp.RequestHandler):
    context = {}
    def initialize(self, request, response):
        """docstring for __init__"""
        self.populateContext()
        super(BaseHandler, self).initialize(request, response)

    def populateContext(self):
        """Load up the stuff that every web handler will need"""
        user = users.get_current_user()

        if user:
            self.context['logged_in'] = True
            self.context['is_admin'] = users.is_current_user_admin()

    def render(self, template_name):
        """Rending a template in a base directory by passing the name of the template"""
        env = jinja2.Environment(loader=jinja2.FileSystemLoader('views'))
        template = env.get_template(template_name)
        self.response.out.write(template.render(self.context))

