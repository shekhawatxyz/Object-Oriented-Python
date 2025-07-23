class Lightswitch:
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        # Turn the switch on
        self.switchIsOn = True

    def turnOff(self):
        # Turn the switch off
        self.switchIsOn = False

    def show(self):
        # Added for testing
        print(self.switchIsOn)


# Main code
oLightSwitch = Lightswitch()  # create a lightswitch object

# Calls to methods
oLightSwitch.show()
oLightSwitch.turnOn()
oLightSwitch.show()
oLightSwitch.turnOff()
oLightSwitch.show()
oLightSwitch.turnOn()
oLightSwitch.show()
