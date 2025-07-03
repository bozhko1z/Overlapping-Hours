import datetime
import unittest

from overlap_hours.funcs import overlapping
from overlap_project.overlap_app.overlap_hours import funcs as f


class TestOverlappingHours(unittest.TestCase):
    def test_overlapping_days(self):
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "11:00"},
            {"Day": "Friday", "Start": "12:00", "End": "14:00"},
            {"Day": "Monday", "Start": "15:00", "End": "19:00"},
        ]
        self.assertFalse(f.overlapping_days(data))

    def test_no_overlapping_days(self):
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "11:00"},
            {"Day": "Tuesday", "Start": "12:00", "End": "14:00"},
            {"Day": "Friday", "Start": "015:00", "End": "19:00"},
        ]
        self.assertTrue(f.overlapping_days(data))

    def test_overlapping_time(self):
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "18:00"},
            {"Day": "Monday", "Start": "12:00", "End": "14:00"},
            {"Day": "Friday", "Start": "15:00", "End": "19:00"},
        ]
        self.assertFalse(f.overlapping_time(data))

    def test_no_overlapping_time(self):
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "14:00"},
            {"Day": "Monday", "Start": "15:00", "End": "19:00"},
            {"Day": "Friday", "Start": "15:00", "End": "19:00"},
        ]
        self.assertTrue(f.overlapping_time(data))

    def test_mock(self):
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "14:00"},
        ]
        self.assertTrue(overlapping(data))

    def test_mock_1(self):
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "14:00"},
            {"Day": "Tuesday", "Start": "09:00", "End": "14:00"},
        ]
        self.assertTrue(overlapping(data))

    def test_mock_2(self):
        data = []
        for day in [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]:
            for hour in range(0, 24):
                for minute in range(0, 60, 2):
                    data.append(
                        {
                            "Day": day,
                            "Start": f"{hour}:{minute}",
                            "End": f"{hour}:{minute + 1}",
                        },
                    )

        time_start = datetime.datetime.now()
        result = overlapping(data)
        time_end = datetime.datetime.now()
        self.assertTrue(result)

        duration_ms = (time_end - time_start).total_seconds() * 1000
        print(f"Time taken: {duration_ms:.2f} ms")
