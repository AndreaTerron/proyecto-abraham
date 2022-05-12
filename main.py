distance = 0
servos.P2.set_angle(90)

def on_forever():
    global distance
    distance = sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.CENTIMETERS)
    basic.show_number(distance)
    if distance < 15:
        servos.P2.set_angle(0)
        basic.pause(10)
    else:
        servos.P2.set_angle(90)

basic.forever(on_forever)
