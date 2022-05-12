let distance = 0
servos.P2.setAngle(90)
basic.forever(function on_forever() {
    
    distance = sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.Centimeters)
    basic.showNumber(distance)
    if (distance < 15) {
        servos.P2.setAngle(0)
        basic.pause(10)
    } else {
        servos.P2.setAngle(90)
    }
    
})
