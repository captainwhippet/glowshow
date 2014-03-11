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

On your other device (or the RPi itself) you can now send commands using glowclient.send_command. (See client/glowserver.py)

To set a pattern:

    # Send a pattern from the client to the glowserver
    host = ("raspberrypi.home", 13379)
    pattern = [1,0,0,0,0,0, # Arm 1
               1,0,0,0,0,0, # Arm 2
               1,0,0,0,0,0] # Arm 3
    command = { 'cmd' : 'set_pattern', 'value': pattern }
    glowclient.send_command(host, command)

The pattern is mapped to the LEDs on the Pi in a way that's a bit easier to understand than the mapping in piglow.py

Command queue
-------------
Each command received is stored in a queue on the server side and handled in turn, so you can fire off a sequence of patterns from the client and sit back and watch them cycle through on the PiGlow.

You can control the speed of the cycle like this from the client:

    # Set the speed
    speed = 50
    command = { 'cmd': 'set_speed', 'value' : speed }
    glowclient.send_command(host, command)

You can also set the brightness:

    # Set the brightness
    brightness = 75
    command = { 'cmd': 'set_brightness', 'value' : brightness }
    glowclient.send_command(host, command)

Example Script
--------------

Please take a look at client/glowshow_example.py for an example of how to send commands from the client once the server is running.

