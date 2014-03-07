#
# Filename: glowthread.py
# Author:   @captainwhippet
# Created:  7 March 2014
#
#   A thread with a queue that take commands and executes them on a
#   GlowShow instance for displaying with the PiGlow

import threading
import Queue
import glowshow
import traceback

class GlowThread(threading.Thread):
    
    def __init__(self):
        super(GlowThread, self).__init__()
        self.daemon = True
        self.cmd_q = Queue.Queue()
        self.glow = glowshow.GlowShow()
    
    def run(self):
        while True:
            try:
                cmd = self.cmd_q.get(True)
                f = getattr(self.glow, cmd['cmd'])
                f(cmd['value'])
            except:
                traceback.print_exc()
                continue
