from twisted.internet import reactor
from twisted.web import static, server, twcgi, script, vhost
from twisted.web.resource import Resource
from twisted.web.wsgi import WSGIResource
from twisted.web.server import Site
from flask import Flask, render_template, g, request
from multiprocessing import Process
import logging
from base_plugin import BasePlugin
from core_plugins.player_manager import permissions, UserLevels
import json
app = Flask(__name__)

class WebappPlugin(BasePlugin):
    """
    Example plugin that sends a message of the day to a client after a
    successful connection.
    """
    name = "webapp_plugin"
    auto_activate = True

    def activate(self):
        super(WebappPlugin, self).activate()
        with open("plugins/webapp_plugin/config.json", "r+") as config:
            self.webapp_config = json.load(config)
        resource = WSGIResource(reactor, reactor.getThreadPool(), app)
        site = Site(resource)
        print("now in activate")
        print("starting to listen on 21080")
        reactor.listenTCP(21080, site)
        
    @app.route("/")
    def index():
        return render_template("plugins/webapp_plugin/views/index.html")


