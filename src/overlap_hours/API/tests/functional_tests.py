import unittest

from ..overlap_checker import run_overlap_funcs


class TestCalledFunctions(unittest.TestCase):
    def test_overlap_check_1(self):
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "11:00"},
            {"Day": "Friday", "Start": "10:00", "End": "11:00"},
            {"Day": "Working days", "Start": "09:00", "End": "12:30"},
        ]
        self.assertFalse(run_overlap_funcs(data=data))

    def test_overlap_check_2(self):
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "11:00"},
            {"Day": "Friday", "Start": "10:00", "End": "11:00"},
            {"Day": "Weekend", "Start": "09:00", "End": "12:30"},
            {"Day": "Friday", "Start": "16:00", "End": "18:00"},
        ]
        self.assertTrue(run_overlap_funcs(data=data))

    def test_overlap_check_3(self):
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "11:00"},
            {"Day": "Friday", "Start": "10:00", "End": "11:00"},
            {"Day": "All days", "Start": "10:30", "End": "12:30"},
        ]
        self.assertFalse(run_overlap_funcs(data=data))

    def test_overlap_check_4(self):
        data = [
            {"Day": "Saturday", "Start": "09:00", "End": "11:00"},
            {"Day": "Friday", "Start": "10:00", "End": "11:00"},
            {"Day": "All days", "Start": "10:30", "End": "12:30"},
        ]
        self.assertFalse(run_overlap_funcs(data=data))

    def test_overlap_check_5(self):
        data = [
            {"Day": "Saturday", "Start": "09:00", "End": "11:00"},
            {"Day": "Friday", "Start": "10:00", "End": "11:00"},
            {"Day": "Weekend", "Start": "10:30", "End": "12:30"},
        ]
        self.assertFalse(run_overlap_funcs(data=data))

    def test_overlap_check_6(self):
        data = [
            {"Day": "Saturday", "Start": "09:00", "End": "11:00"},
            {"Day": "Saturday", "Start": "18:00", "End": "22:00"},
            {"Day": "Friday", "Start": "10:00", "End": "11:00"},
            {"Day": "Weekend", "Start": "14:00", "End": "16:00"},
        ]
        self.assertTrue(run_overlap_funcs(data=data))

    def test_overlap_check_7(self):
        data = [
            {"Day": "Monday", "Start": "18:00", "End": "20:00"},
            {"Day": "Monday", "Start": "10:00", "End": "12:00"},
            {"Day": "Monday", "Start": "09:00", "End": "09:30"},
            {"Day": "Monday", "Start": "14:00", "End": "16:30"},
        ]
        self.assertTrue(run_overlap_funcs(data=data))

    def test_overlap_check_8(self):
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "11:00"},
            {"Day": "Monday", "Start": "08:00", "End": "12:30"},
        ]
        self.assertFalse(run_overlap_funcs(data=data))

    def test_overlap_check_9(self):
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "12:30"},
            {"Day": "Monday", "Start": "12:30", "End": "14:30"},
            {"Day": "Monday", "Start": "16:30", "End": "18:00"},
        ]
        self.assertTrue(run_overlap_funcs(data=data))

    def test_overlap_check_10(self):
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "12:30"},
            {"Day": "Monday", "Start": "16:00", "End": "18:30"},
        ]
        self.assertTrue(run_overlap_funcs(data=data))

    def test_overlap_check_11(self):
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "12:30"},
            {"Day": "All days", "Start": "16:00", "End": "18:30"},
        ]
        self.assertTrue(run_overlap_funcs(data=data))

    def test_overlap_check_12(self):
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "12:30"},
            {"Day": "All days", "Start": "08:00", "End": "08:30"},
        ]
        self.assertFalse(run_overlap_funcs(data=data))

    def test_overlap_check_13(self):
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "12:30"},
            {"Day": "Weekend", "Start": "08:00", "End": "16:30"},
        ]
        self.assertTrue(run_overlap_funcs(data=data))


if __name__ == "__main__":
    unittest.main()
