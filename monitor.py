import sys
from time import sleep

def vitals_ok(temperature, pulseRate, spo2):
    #Pure function: returns status and message based on vitals.
    if temperature > 102 or temperature < 95:
        return False, 'Temperature critical!'
    if pulseRate < 60 or pulseRate > 100:
        return False, 'Pulse Rate is out of range!'
    if spo2 < 90:
        return False, 'Oxygen Saturation out of range!'
    return True, 'All vitals are normal'

def show_alert(msg, cycles=6, printer=print, flusher=None, sleeper=None):
    #Handles alert animation and printing. Can be mocked for testing.
    if flusher is None:
        flusher = sys.stdout.flush
    if sleeper is None:
        sleeper = sleep
    printer(msg)
    for _ in range(cycles):
        for symbol in ['* ', ' *']:
            printer('\r' + symbol, end='')
            flusher()
            sleeper(1)

# Example usage (separation of logic and side effects):
if __name__ == "__main__":
    status, message = vitals_status(101, 55, 95)
    if not status:
        show_alert(message)
