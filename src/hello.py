# vim modeline (put ":set modeline" into your ~/.vimrc)
# vim:set expandtab ts=4 sw=4 ai ft=python:

import os
import json
import sys
import cherrypy

class Hello(object):
    @cherrypy.expose
    def hi(self):
        return "Hiho" + json.dumps(os.environ, indent=2)

    @cherrypy.expose
    def bye(self):
        print("You said bye!")
        sys.exit(0)
        
if __name__ == '__main__':
    conf = {
        'global':{
            'server.socket_port': os.environ.get('PORT') or 8080,
            'server.socket_host': '0.0.0.0'
        },
    }

    cherrypy.quickstart(Hello(), '/', conf)

