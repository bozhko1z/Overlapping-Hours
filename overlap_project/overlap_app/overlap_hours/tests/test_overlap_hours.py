import datetime
import unittest

from overlap_hours.funcs import is_data_valid


class TestOverlappingHours(unittest.TestCase):
    def test_overlapping_days(self):
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "11:00"},
            {"Day": "Friday", "Start": "12:00", "End": "14:00"},
            {"Day": "Monday", "Start": "15:00", "End": "19:00"},
        ]
        self.assertTrue(is_data_valid(data))

    def test_no_overlapping_days(self):
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "11:00"},
            {"Day": "Tuesday", "Start": "12:00", "End": "14:00"},
            {"Day": "Friday", "Start": "15:00", "End": "19:00"},
        ]
        self.assertTrue(is_data_valid(data))

    def test_overlapping_time(self):
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "18:00"},
            {"Day": "Monday", "Start": "12:00", "End": "14:00"},
            {"Day": "Friday", "Start": "15:00", "End": "19:00"},
        ]
        self.assertFalse(is_data_valid(data))


    def test_overlapping_time_1(self):
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "18:00"},
            {"Day": "Friday", "Start": "15:00", "End": "19:00"},
            {"Day": "Working days", "Start": "16:00", "End": "17:00"},
        ]
        self.assertFalse(is_data_valid(data))

    def test_overlapping_time_2(self):
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "18:00"},
            {"Day": "Friday", "Start": "15:00", "End": "19:00"},
            {"Day": "All days", "Start": "16:00", "End": "17:00"},
        ]
        self.assertFalse(is_data_valid(data))

    def test_no_overlapping_time(self):
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "14:00"},
            {"Day": "Monday", "Start": "15:00", "End": "19:00"},
            {"Day": "Friday", "Start": "15:00", "End": "19:00"},
        ]
        self.assertTrue(is_data_valid(data))

    def test_no_overlapping_time_2(self):
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "14:00"},
            {"Day": "Monday", "Start": "15:00", "End": "19:00"},
            {"Day": "All days", "Start": "20:00", "End": "21:00"},
        ]
        self.assertTrue(is_data_valid(data))

    def test_no_overlapping_time_3(self):
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "18:00"},
            {"Day": "Friday", "Start": "15:00", "End": "19:00"},
            {"Day": "Weekend", "Start": "16:00", "End": "17:00"},
        ]
        self.assertTrue(is_data_valid(data))

    def test_mock(self):
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "14:00"},
        ]
        self.assertTrue(is_data_valid(data))

    def test_mock_1(self):

        data = [
            {"Day": "Monday", "Start": "09:00", "End": "14:00"},
            {"Day": "Tuesday", "Start": "09:00", "End": "14:00"},
        ]
        self.assertTrue(is_data_valid(data))

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
        result = is_data_valid(data)
        time_end = datetime.datetime.now()
        self.assertTrue(result)

        duration_ms = (time_end - time_start).total_seconds() * 1000
        print(f"Time taken: {duration_ms:.2f} ms")
