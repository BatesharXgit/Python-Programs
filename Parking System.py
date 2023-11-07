import machine
import urequests
import utime
import network, time

HTTP_HEADERS = {'Content-Type': 'application/json'} 
THINGSPEAK_WRITE_API_KEY = 'K52X43D5H7PK0CAU'

ssid = 'oneplus'
password = '123456789'

# Configure Pico W as Station
sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
 
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.connect(ssid, password)
    while not sta_if.isconnected():
     pass
print('network config:', sta_if.ifconfig())

# Defining the servo pin and IR sensor pin
servo_pin1 = machine.Pin(17)
servo_pin2 = machine.Pin(18)
ir_sensor_pin1 = machine.Pin(16)
ir_sensor_pin2 = machine.Pin(19)
ir_sensor_pin3 = machine.Pin(14)
ir_sensor_pin4 = machine.Pin(15)
ir_sensor_pin5 = machine.Pin(13)

#Defining variables
slot = 0
total_slots = 3

# Createing a PWM object for the servo motor 1
m1 = machine.PWM(servo_pin1)
m1.freq(50)

# Createing a PWM object for the servo motor 2
m2 = machine.PWM(servo_pin2)
m2.freq(50)

try:
    while True:
        # Storing the IR values in variables
        ir1 = ir_sensor_pin1.value()
        ir2 = ir_sensor_pin2.value()
        ir3 = ir_sensor_pin3.value()
        ir4 = ir_sensor_pin4.value()
        ir5 = ir_sensor_pin5.value()
        
        if ir1 == 1 and (ir3 == 1 or ir4 == 1 or ir5 == 1):
            # Rotate the servo from 0 to 90 degrees
            for duty_cycle in range(4800, 500, -10):
                m1.duty_u16(duty_cycle)
                utime.sleep_ms(5)
                
            utime.sleep(2)

            # Rotate the servo from 90 to 0 degrees
            for duty_cycle in range(500, 4800, 10):
                m1.duty_u16(duty_cycle)
                utime.sleep_ms(5)
            
            slot = slot + 1
            
        else:
            # IR sensor value is 0, do not rotate the servo
            m1.duty_u16(0)
            
        if ir2 == 1:
            # Rotate the servo from 0 to 90 degrees
            for duty_cycle in range(4800, 500, -10):
                m2.duty_u16(duty_cycle)
                utime.sleep_ms(5)
                
            utime.sleep(2)

            # Rotate the servo from 90 to 0 degrees
            for duty_cycle in range(500, 4800, 10):
                m2.duty_u16(duty_cycle)
                utime.sleep_ms(5)
                
            slot = slot - 1
            
        else:
            # IR sensor value is 0, do not rotate the servo
            m2.duty_u16(0)
            
        slot_available = total_slots - slot
        
        # Sending data to thingspeak
        ir_readings = {'field1':ir3, 'field2':ir4, 'field3':ir5, 'field4':slot_available}
        request = urequests.post( 'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_WRITE_API_KEY, json = ir_readings, headers = HTTP_HEADERS )
        request.close()
        print(ir_readings)

finally:
    # Clean up by turning off the PWM signal
    m1.duty_u16(0)
    m2.duty_u16(0)
    m1.deinit()
    m2.deinit()