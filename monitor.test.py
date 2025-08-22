import unittest
from monitor import vitals_ok

class MonitorTest(unittest.TestCase):
    def test_temperature_out_of_range(self):
        status, msgs = vitals_ok({'temperature': 103, 'pulseRate': 80, 'spo2': 95})
        self.assertFalse(status)
        self.assertIn('Temperature critical!', msgs)

    def test_pulse_out_of_range(self):
        status, msgs = vitals_ok({'temperature': 98, 'pulseRate': 120, 'spo2': 95})
        self.assertFalse(status)
        self.assertIn('Pulse Rate is out of range!', msgs)

    def test_spo2_out_of_range(self):
        status, msgs = vitals_ok({'temperature': 98, 'pulseRate': 80, 'spo2': 85})
        self.assertFalse(status)
        self.assertIn('Oxygen Saturation out of range!', msgs)

    def test_all_vitals_normal(self):
        status, msgs = vitals_ok({'temperature': 98.6, 'pulseRate': 75, 'spo2': 98})
        self.assertTrue(status)
        self.assertIn('All vitals are normal', msgs)

if __name__ == '__main__':
    unittest.main()
