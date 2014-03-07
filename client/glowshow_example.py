#
# Filename: glowthread.py
# Author:   @captainwhippet
# Created:  7 March 2014
#
#    An example for using the glowshow that sends some
#    simple patterns to the glowserver

import glowclient

host = ("raspberrypi.home", 13379)

pattern = [1,0,0,0,0,0,
           1,0,0,0,0,0,
           1,0,0,0,0,0]

for speed in range(1, 101, 10):
    
    # Set the speed
    command = { 'cmd': 'set_speed', 'value' : speed }
    print 'send command: ', command
    glowclient.send_command(host, command)

    for i in range(0, 10):
        # Send the pattern
        command = { 'cmd' : 'set_pattern', 'value': pattern }
        print 'send command: ', command
        glowclient.send_command(host, command)
        
        # Shift the pattern along
        for i in range(0,5):
            pattern.append(pattern.pop(0))

glowclient.send_command(host, command)
command = { 'cmd' : 'set_pattern', 'value': pattern }
