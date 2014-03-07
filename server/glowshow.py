#
# Filename: glowshow.py
# Author:   @captainwhippet
# Created:  7 March 2014
#
#   Provides a convenient class for displaying patterns on the PiGlow:
#   - includes a smooth transition between patterns
#   - a more intuitive structure for the pattern, which is mapped onto
#     the led values

from piglow import PiGlow
import time

class GlowShow(object):

    piglow = PiGlow(1)
    led_val = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    brightness=25
    smoothness=50
    speed=10

    def set_speed(self, speed):
        print 'set_speed = ', speed
        self.speed = speed

    def set_brightness(self, brightness):
        print 'set_brightness = ', brightness
        self.brightness = brightness
        
    def set_pattern(self, pattern):
        print 'set_pattern = ', pattern
        led_last = list(self.led_val)
        self.led_val = self.map_vals(pattern)        
        self.led_val = [ v * self.brightness for v in self.led_val ]
        
        # smooth transition from last to this value
        for i in range(0, self.smoothness + 1):
            led_step = [ v0 + int((v1 - v0) * float(i)/float(self.smoothness))
                for v0, v1 in zip(led_last, self.led_val)]

            # update the piglow with current values
            self.piglow.update_leds(led_step)
            time.sleep(1.0/float(self.speed)/float(self.smoothness))

    def map_vals(self, led_set):
        led_map = [7, 8, 9, 6, 5, 10, 18, 17, 16, 14, 12, 11, 1, 2, 3, 4, 15, 13]
        for i in range(0, len(led_map)):
            self.led_val[led_map[i] - 1] = led_set[i]
        return self.led_val

