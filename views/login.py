__author__ = 'modulus'

from flask.views import View
from flask import render_template


class LoginView(View):
    
    def dispatch_request(self):
        return render_template("login.html", name="loginView")