#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import logging
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import util
from google.appengine.api import users


from models import User
from constants import *


#What the Template App Still Needs

#- Basic Security Features
#- Paypal payment integration
#- Data validation decorator
#- Sign in 
#- Must sign in decorator


class MainHandler(webapp.RequestHandler):
    def get(self):
        
        content_template_values = {
           
        }
       
        self.response.out.write(RenderFullPage('page1.html', content_template_values))


# Page Handlers
class PageHandler1(webapp.RequestHandler):
    def get(self):
        template_values = {

        }
        
        path = os.path.join(os.path.dirname(__file__), 'page1.html')
        self.response.out.write(template.render(path, template_values))

       
        
class PageHandler2(webapp.RequestHandler):
    def get(self):
        template_values = {
        
        }
        
        path = os.path.join(os.path.dirname(__file__), 'page2.html')
        self.response.out.write(template.render(path, template_values))


# Gets
class GetMethod(webapp.RequestHandler):
    def get(self):
        return 0



# Posts
class PostMethod(webapp.RequestHandler):
    def post(self):
        return 0


# Helpers
def RenderFullPage(template_file_name, content_template_values):
    """This re-renders the full page with the specified template."""
    
    main_path = os.path.join('templates/index.html')
    content_path = os.path.join('templates/' + template_file_name )
    
    content = template.render(content_path, content_template_values)
    template_values = {
        'CONTENT': content
    }
    
    return template.render(main_path, template_values)


# Decorators





appRoute = webapp.WSGIApplication( [('/page1', PageHandler1),
										('/page2', PageHandler2),
										('/', MainHandler)
										], debug=True)
										
def main():
    run_wsgi_app(appRoute)

if __name__ == '__main__':
    main()
