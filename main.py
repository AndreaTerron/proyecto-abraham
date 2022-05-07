distance = 0
servos.P0.set_angle(90)

def on_forever():
    global distance
    distance = sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.CENTIMETERS)
basic.forever(on_forever)
