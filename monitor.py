from time import sleep
import sys

def vitals_ok(temperature, pulseRate, spo2):
    def alert(msg):
        print(msg)
        for _ in range(6):
            for symbol in ['* ', ' *']:
                print('\r' + symbol, end='')
                sys.stdout.flush()
                sleep(1)
        return False

    if temperature > 102 or temperature < 95:
        return alert('Temperature critical!')
    if pulseRate < 60 or pulseRate > 100:
        return alert('Pulse Rate is out of range!')
    if spo2 < 90:
        return alert('Oxygen Saturation out of
