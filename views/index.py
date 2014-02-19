__author__ = 'modulus'

from flask.views import View
from flask import render_template


class IndexView(View):

    def dispatch_request(self):
        return render_template("index.html", name=None)