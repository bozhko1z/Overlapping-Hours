import unittest
from unittest.mock import patch
from overlap_project.overlap_app.overlap_hours.API.overlap_checker import run_overlap_funcs


class TestCalledFunctions(unittest.TestCase):
    @patch("overlap_hours.funcs.overlapping")
    def test_overlapping_days(self, mock):

        data = [
            {"Day": "Monday", "Start": "09:00", "End": "11:00"},
            {"Day": "Friday", "Start": "10:00", "End": "11:00"},
            {"Day": "Monday", "Start": "09:00", "End": "11:00"},
        ]

        # new solution

        # trying all combinations of true/false
        for mock_day in [True, False]:
                # sets mock values
                mock.return_value = mock_day
                # tests the result(if both are true -> True - otherwise -> False)
                self.assertEqual(mock_day, run_overlap_funcs(data=data))
                # checks if mocks were called correctly
                mock.assert_called_once_with(data=data)
                # resets for the next loop
                mock.reset_mock()


if __name__ == "__main__":
    unittest.main()
