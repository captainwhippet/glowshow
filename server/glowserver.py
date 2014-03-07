#
# Filename: glowserver.py
# Author:   @captainwhippet
# Created:  7 March 2014
#
#   A simple socket server that takes commands and puts them on a queue
#   on the glowthread, which then sets the pattern on the PiGlow

import pickle, SocketServer
import glowthread

class GlowServer(SocketServer.BaseRequestHandler):

    def handle(self):

        self.f = self.request.makefile('b')
        cmd = pickle.load(self.f)
        glowthread.cmd_q.put(cmd)
        self.f.close()

glowthread = glowthread.GlowThread()
glowthread.start()

SocketServer.TCPServer.allow_reuse_address = True
serv = SocketServer.TCPServer(("", 13379), GlowServer)
serv.serve_forever()

