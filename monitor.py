from time import sleep
import sys
def vitals_ok(temperature, pulseRate, spo2):
    if temperature > 102 or temperature < 95:
        return False, 'Temperature critical!'
    if pulseRate < 60 or pulseRate > 100:
        return False, 'Pulse Rate is out of range!'
    if spo2 < 90:
        return False, 'Oxygen Saturation out of range!'
    return True, 'All vitals are normal'

def show_alert(msg):
    print(msg)
    for _ in range(6):
        for symbol in ['* ', ' *']:
            print('\r' + symbol, end='')
            sys.stdout.flush()
            sleep(1)

# Example usage:
status, message = vitals_ok(101, 55, 95)
if not status:
    show_alert(message)
