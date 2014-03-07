#
# Filename: glowthread.py
# Author:   @captainwhippet
# Created:  7 March 2014
#
#    Send a command to the server running the glowserver

import pickle, socket

def send_command(host, pattern):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(host)
    f = s.makefile('b')    
    pickle.dump(pattern, f)
    f.flush()
    f.close()
    s.close()
