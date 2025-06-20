import unittest
<<<<<<< HEAD

from ..overlap_checker import run_overlap_funcs
=======
import logging

<<<<<<< HEAD:src/overlap_hours/API/tests/functional_tests.py
from overlap_hours import funcs as f
>>>>>>> 78352b2 (reimplemented the main func logic)
=======
from overlap_app.overlap_hours import funcs as f
>>>>>>> dc0e855 (finished building django):overlap_project/overlap_app/overlap_hours/API/tests/functional_tests.py


class TestCalledFunctions(unittest.TestCase):
    def test_overlap_check_1(self):
<<<<<<< HEAD
=======
        testName = self._testMethodName
        logging.info(f"Running test: {testName}")
>>>>>>> 78352b2 (reimplemented the main func logic)
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "11:00"},
            {"Day": "Friday", "Start": "10:00", "End": "11:00"},
            {"Day": "Working days", "Start": "09:00", "End": "12:30"},
        ]
<<<<<<< HEAD
        self.assertFalse(run_overlap_funcs(data=data))

    def test_overlap_check_2(self):
=======
        self.assertFalse(f.overlapping(data=data))

    def test_overlap_check_2(self):
        testName = self._testMethodName
        logging.info(f"Running test: {testName}")
>>>>>>> 78352b2 (reimplemented the main func logic)
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "11:00"},
            {"Day": "Friday", "Start": "10:00", "End": "11:00"},
            {"Day": "Weekend", "Start": "09:00", "End": "12:30"},
            {"Day": "Friday", "Start": "16:00", "End": "18:00"},
        ]
<<<<<<< HEAD
        self.assertTrue(run_overlap_funcs(data=data))

    def test_overlap_check_3(self):
=======
        self.assertTrue(f.overlapping(data=data))

    def test_overlap_check_3(self):
        testName = self._testMethodName
        logging.info(f"Running test: {testName}")
>>>>>>> 78352b2 (reimplemented the main func logic)
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "11:00"},
            {"Day": "Friday", "Start": "10:00", "End": "11:00"},
            {"Day": "All days", "Start": "10:30", "End": "12:30"},
        ]
<<<<<<< HEAD
        self.assertFalse(run_overlap_funcs(data=data))

    def test_overlap_check_4(self):
=======
        self.assertFalse(f.overlapping(data=data))

    def test_overlap_check_4(self):
        testName = self._testMethodName
        logging.info(f"Running test: {testName}")
>>>>>>> 78352b2 (reimplemented the main func logic)
        data = [
            {"Day": "Saturday", "Start": "09:00", "End": "11:00"},
            {"Day": "Friday", "Start": "10:00", "End": "11:00"},
            {"Day": "All days", "Start": "10:30", "End": "12:30"},
        ]
<<<<<<< HEAD
        self.assertFalse(run_overlap_funcs(data=data))

    def test_overlap_check_5(self):
=======
        self.assertFalse(f.overlapping(data=data))

    def test_overlap_check_5(self):
        testName = self._testMethodName
        logging.info(f"Running test: {testName}")
>>>>>>> 78352b2 (reimplemented the main func logic)
        data = [
            {"Day": "Saturday", "Start": "09:00", "End": "11:00"},
            {"Day": "Friday", "Start": "10:00", "End": "11:00"},
            {"Day": "Weekend", "Start": "10:30", "End": "12:30"},
        ]
<<<<<<< HEAD
        self.assertFalse(run_overlap_funcs(data=data))

    def test_overlap_check_6(self):
=======
        self.assertFalse(f.overlapping(data=data))

    def test_overlap_check_6(self):
        testName = self._testMethodName
        logging.info(f"Running test: {testName}")
>>>>>>> 78352b2 (reimplemented the main func logic)
        data = [
            {"Day": "Saturday", "Start": "09:00", "End": "11:00"},
            {"Day": "Saturday", "Start": "18:00", "End": "22:00"},
            {"Day": "Friday", "Start": "10:00", "End": "11:00"},
            {"Day": "Weekend", "Start": "14:00", "End": "16:00"},
        ]
<<<<<<< HEAD
        self.assertTrue(run_overlap_funcs(data=data))

    def test_overlap_check_7(self):
=======
        self.assertTrue(f.overlapping(data=data))

    def test_overlap_check_7(self):
        testName = self._testMethodName
        logging.info(f"Running test: {testName}")
>>>>>>> 78352b2 (reimplemented the main func logic)
        data = [
            {"Day": "Monday", "Start": "18:00", "End": "20:00"},
            {"Day": "Monday", "Start": "10:00", "End": "12:00"},
            {"Day": "Monday", "Start": "09:00", "End": "09:30"},
            {"Day": "Monday", "Start": "14:00", "End": "16:30"},
        ]
<<<<<<< HEAD
        self.assertTrue(run_overlap_funcs(data=data))

    def test_overlap_check_8(self):
=======
        self.assertTrue(f.overlapping(data=data))

    def test_overlap_check_8(self):
        testName = self._testMethodName
        logging.info(f"Running test: {testName}")
>>>>>>> 78352b2 (reimplemented the main func logic)
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "11:00"},
            {"Day": "Monday", "Start": "08:00", "End": "12:30"},
        ]
<<<<<<< HEAD
        self.assertFalse(run_overlap_funcs(data=data))

    def test_overlap_check_9(self):
=======
        self.assertFalse(f.overlapping(data=data))

    def test_overlap_check_9(self):
        testName = self._testMethodName
        logging.info(f"Running test: {testName}")
>>>>>>> 78352b2 (reimplemented the main func logic)
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "12:30"},
            {"Day": "Monday", "Start": "12:30", "End": "14:30"},
            {"Day": "Monday", "Start": "16:30", "End": "18:00"},
        ]
<<<<<<< HEAD
        self.assertTrue(run_overlap_funcs(data=data))

    def test_overlap_check_10(self):
=======
        self.assertTrue(f.overlapping(data=data))

    def test_overlap_check_10(self):
        testName = self._testMethodName
        logging.info(f"Running test: {testName}")
>>>>>>> 78352b2 (reimplemented the main func logic)
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "12:30"},
            {"Day": "Monday", "Start": "16:00", "End": "18:30"},
        ]
<<<<<<< HEAD
        self.assertTrue(run_overlap_funcs(data=data))

    def test_overlap_check_11(self):
=======
        self.assertTrue(f.overlapping(data=data))

    def test_overlap_check_11(self):
        testName = self._testMethodName
        logging.info(f"Running test: {testName}")
>>>>>>> 78352b2 (reimplemented the main func logic)
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "12:30"},
            {"Day": "All days", "Start": "16:00", "End": "18:30"},
        ]
<<<<<<< HEAD
        self.assertTrue(run_overlap_funcs(data=data))

    def test_overlap_check_12(self):
=======
        self.assertTrue(f.overlapping(data=data))

    def test_overlap_check_12(self):
        testName = self._testMethodName
        logging.info(f"Running test: {testName}")
>>>>>>> 78352b2 (reimplemented the main func logic)
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "12:30"},
            {"Day": "All days", "Start": "08:00", "End": "08:30"},
        ]
<<<<<<< HEAD
        self.assertFalse(run_overlap_funcs(data=data))

    def test_overlap_check_13(self):
=======
        self.assertTrue(f.overlapping(data=data))

    def test_overlap_check_13(self):
        testName = self._testMethodName
        logging.info(f"Running test: {testName}")
>>>>>>> 78352b2 (reimplemented the main func logic)
        data = [
            {"Day": "Monday", "Start": "09:00", "End": "12:30"},
            {"Day": "Weekend", "Start": "08:00", "End": "16:30"},
        ]
<<<<<<< HEAD
        self.assertTrue(run_overlap_funcs(data=data))


if __name__ == "__main__":
    unittest.main()
=======
        self.assertTrue(f.overlapping(data=data))


#   personal tests
    def test_overlap_check_14(self):
        testName = self._testMethodName
        logging.info(f"Running test: {testName}")
        data = []
        self.assertFalse(f.overlapping(data=data))
        
    def test_overlap_check_15(self):
        testName = self._testMethodName
        logging.info(f"Running test: {testName}")
        data = [{"Day": "Monday", "Start": "09:00", "End": "12:30"}]
        self.assertFalse(f.overlapping(data=data))
    
    def test_overlap_check_16(self):
        testName = self._testMethodName
        logging.info(f"Running test: {testName}")
        data = [
                {"Day": "Monday", "Start": "23:00", "End": "00:02"},
                {"Day": "Monday", "Start": "00:00", "End": "02:30"}
            ]
        self.assertTrue(f.overlapping(data=data))
           
if __name__ == "__main__":
    unittest.main()
>>>>>>> 78352b2 (reimplemented the main func logic)
