import unittest
from monitor import vitals_ok


class MonitorTest(unittest.TestCase):
    def test_temperature_out_of_range(self):
        status, msg = vitals_ok(103, 80, 95)
        self.assertFalse(status)
        self.assertEqual(msg, 'Temperature critical!')

    def test_pulse_out_of_range(self):
        status, msg = vitals_ok(98, 120, 95)
        self.assertFalse(status)
        self.assertEqual(msg, 'Pulse Rate is out of range!')

    def test_spo2_out_of_range(self):
        status, msg = vitals_ok(98, 80, 85)
        self.assertFalse(status)
        self.assertEqual(msg, 'Oxygen Saturation out of range!')

    def test_all_vitals_normal(self):
        status, msg = vitals_ok(98.6, 75, 98)
        self.assertTrue(status)
        self.assertEqual(msg, 'All vitals are normal')


if __name__ == '__main__':
  unittest.main()

