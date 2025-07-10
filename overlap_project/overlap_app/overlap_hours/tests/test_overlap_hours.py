import unittest
from overlap_app.overlap_hours.funcs import overlapping

class TestOverlappingHours(unittest.TestCase):
    def test_overlapping_days(self):
        data = [
                {"Day": "Monday", "Start": "09:00", "End": "11:00"},
                {"Day": "Friday", "Start": "12:00", "End": "14:00"},
                {"Day": "Monday", "Start": "15:00", "End": "19:00"}
            ]
        self.assertFalse(overlapping(data))
    
    def test_no_overlapping_days(self):
        data = [
                {"Day": "Monday", "Start": "09:00", "End": "11:00"},
                {"Day": "Tuesday", "Start": "12:00", "End": "14:00"},
                {"Day": "Friday", "Start": "015:00", "End": "19:00"}
            ]
        self.assertTrue(overlapping(data))
        
    def test_overlapping_time(self):
        data = [
                {"Day": "Monday", "Start": "09:00", "End": "18:00"},
                {"Day": "Monday", "Start": "12:00", "End": "14:00"},
                {"Day": "Friday", "Start": "15:00", "End": "19:00"}
            ]
        self.assertFalse(overlapping(data))
        
    def test_no_overlapping_time(self):
        data = [
                {"Day": "Monday", "Start": "09:00", "End": "14:00"},
                {"Day": "Monday", "Start": "15:00", "End": "19:00"},
                {"Day": "Friday", "Start": "15:00", "End": "19:00"}
            ]
        self.assertTrue(overlapping(data))