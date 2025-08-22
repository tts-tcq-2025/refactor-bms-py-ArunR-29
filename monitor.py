def vitals_status(temperature, pulseRate, spo2):
    if temperature > 102 or temperature < 95:
        return False, 'Temperature critical!'
    if pulseRate < 60 or pulseRate > 100:
        return False, 'Pulse Rate is out of range!'
    if spo2 < 90:
        return False, 'Oxygen Saturation out of range!'
    return True, 'All vitals are normal'

def show_alert(msg):
    from time import sleep
    import sys
    print(msg)
    for _ in range(6):
        for symbol in ['* ', ' *']:
            print('\r' + symbol, end='')
            sys.stdout.flush()
            sleep(1)

def vitals_ok(temperature, pulseRate, spo2):
    status, msg = vitals_status(temperature, pulseRate, spo2)
    if not status:
        show_alert(msg)
    return
