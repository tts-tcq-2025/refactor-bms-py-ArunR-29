def vitals_ok(temperature, pulseRate, spo2):
    """Checks all vitals and returns overall status and all messages."""
    messages = []
    status = True

    if temperature > 102 or temperature < 95:
        messages.append('Temperature critical!')
        status = False
    if pulseRate < 60 or pulseRate > 100:
        messages.append('Pulse Rate is out of range!')
        status = False
    if spo2 < 90:
        messages.append('Oxygen Saturation out of range!')
        status = False
    if status:
        messages.append('All vitals are normal')
    return status, messages

def show_alert(msg, cycles=6, printer=None, flusher=None, sleeper=None):
    """Handles alert animation and printing. Can be mocked for testing."""
    if printer is None:
        printer = print
    if flusher is None:
        import sys
        flusher = sys.stdout.flush
    if sleeper is None:
        from time import sleep
        sleeper = sleep
    printer(msg)
    for _ in range(cycles):
        for symbol in ['* ', ' *']:
            printer('\r' + symbol, end='')
            flusher()
            sleeper(1)

# Example mock usage for testing
def mock_printer(msg, end='\n'):
    mock_printer.output.append((msg, end))
mock_printer.output = []

def mock_flusher():
    mock_printer.output.append(('flush', None))

def mock_sleeper(seconds):
    mock_printer.output.append(('sleep', seconds))

# Example usage (separation of logic and side effects):
if __name__ == "__main__":
    status, message = vitals_ok(101, 55, 95)
    if not status:
        show_alert(message, printer=mock_printer, flusher=mock_flusher, sleeper=mock_sleeper)
        #print("Mocked output:", mock_printer.output)
