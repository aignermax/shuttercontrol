

class Shutter(object):
    """Shutter infront of the window controlling the hardware"""
    def __init__(self):
        print "[shutter] created"
    def rise(self):
        """starts moving the shutter upwards until stop is called."""
        print "[shutter] start go up"
    def lower(self):
        """starts moving the shutter downwards until stop is called"""
        print "[shutter] start go down"
    def stop(self):
        """stopps the shutter immediately"""
        print "[shutter] stop"
    