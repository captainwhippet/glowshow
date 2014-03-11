glowshow
========

Controlling the PiGlow remotely via a simple socket server.

These simple scripts help you get a server running on the RaspberryPi. You can send commands to it from another device (e.g. PC or iPhone/iPad using Pythonista) and set patterns, the speed of change and brightness.

This is version 0.1, so a bit basic, but more will follow!

PiGlow setup
------------

First of all, go to @pimoroni for details of how to get the PiGlow running: https://github.com/pimoroni/piglow

Running the server
------------------

Once the PiGlow is all set up, you can run this (in the server sub directory):

    python server.py

This runs the socket server running on port 13379. (Hardcoded for now.) It will sit there waiting for commands.

Running client commands
-----------------------

On your other device (or the RPi itself) you can now send commands using glowclient.send_command. See client/glowserver.py.

To set a pattern:




    # Set the speed
    host = ("raspberrypi.home", 13379)
    speed = 50
    command = { 'cmd': 'set_speed', 'value' : speed }
    glowclient.send_command(host, command)




