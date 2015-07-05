import cgi
import urllib
import webapp2
import jinja2
import os



from google.appengine.api import users

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"))

class MainPage(webapp2.RequestHandler):
    def get(self):
        template =  jinja_environment.get_template('home.html')
        self.response.out.write(template.render())

class Copy_link(webapp2.RequestHandler):
    def post(self):
        url_link=self.request.get('str')
        template_values = {
            'url_link': url_link
            }
        template = jinja_environment.get_template('link.html')
        self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/link', Copy_link),
], debug=True)
