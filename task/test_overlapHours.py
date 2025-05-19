import unittest
from main import overlapping_days, overlapping_time

class TestOverlappingHours(unittest.TestCase):
    def test_overlapping_days(self):
        data = [
                {"Day": "Monday", "Start": "09:00", "End": "11:00"},
                {"Day": "Monday", "Start": "12:00", "End": "14:00"},
                {"Day": "Monday", "Start": "015:00", "End": "19:00"}
            ]
        self.assertFalse(overlapping_days(data))
    
    def test_no_overlapping_days(self):
        data = [
                {"Day": "Monday", "Start": "09:00", "End": "11:00"},
                {"Day": "Tuesday", "Start": "12:00", "End": "14:00"},
                {"Day": "Friday", "Start": "015:00", "End": "19:00"}
            ]
        self.assertTrue(overlapping_days(data)) 
        
    def test_overlapping_time(self):
        data = [
                {"Day": "Monday", "Start": "09:00", "End": "18:00"},
                {"Day": "Monday", "Start": "12:00", "End": "14:00"},
                {"Day": "Friday", "Start": "15:00", "End": "19:00"}
            ]
        self.assertFalse(overlapping_time(data))
        
    def test_no_overlapping_time(self):
        data = [
                {"Day": "Monday", "Start": "09:00", "End": "14:00"},
                {"Day": "Monday", "Start": "15:00", "End": "19:00"},
                {"Day": "Friday", "Start": "15:00", "End": "19:00"}
            ]
        self.assertTrue(overlapping_time(data))