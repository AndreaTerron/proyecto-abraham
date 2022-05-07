let distance = 0
servos.P0.setAngle(90)
basic.forever(function on_forever() {
    
    distance = sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.Centimeters)
})
