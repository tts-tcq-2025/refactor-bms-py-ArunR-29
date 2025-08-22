from time import sleep
import sys

def vitals_ok(vitals):
    """
    Pure function: checks all vitals and returns status and messages.
    Easily extensible for new parameters.
    """
    rules = [
        ('temperature', lambda v: v > 102 or v < 95, 'Temperature critical!'),
        ('pulseRate', lambda v: v < 60 or v > 100, 'Pulse Rate is out of range!'),
        ('spo2', lambda v: v < 90, 'Oxygen Saturation out of range!')
        # Add more rules here as needed
    ]
    messages = []
    status = True
    for key, check, msg in rules:
        if key in vitals and check(vitals[key]):
            messages.append(msg)
            status = False
    if status:
        messages.append('All vitals are normal')
    return status, messages

def show_alert(msgs, cycles=6, printer=None, flusher=None, sleeper=None):
    """
    Handles alert animation and printing. Can be mocked for testing.
    Accepts a list of messages.
    """
    if printer is None:
        printer = print
    if flusher is None:
        flusher = sys.stdout.flush
    if sleeper is None:
        sleeper = sleep
    for msg in msgs:
        printer(msg)
    for _ in range(cycles):
        for symbol in ['* ', ' *']:
            printer('\r' + symbol, end='')
            flasher()
            sleeper(1)

# Example mock usage for testing
def mock_printer(msg, end='\n'):
    mock_printer.output.append((msg, end))
mock_printer.output = []

def mock_flasher():
    mock_printer.output.append(('flush', None))

def mock_sleeper(seconds):
    mock_printer.output.append(('sleep', seconds))

# Example usage (separation of logic and side effects):
if __name__ == "__main__":
    vitals = {'temperature': 101, 'pulseRate': 55, 'spo2': 95}
    status, messages = vitals_ok(vitals)
    if not status:
        show_alert(messages, printer=mock_printer, flasher=mock_flasher, sleeper=mock_sleeper)
