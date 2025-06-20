import unittest
from unittest.mock import patch
from overlap_app.overlap_hours.API import overlap_checker as o

class TestCalledFunctions(unittest.TestCase):
    @patch('overlap_hours.funcs.overlapping_days')
    @patch('overlap_hours.funcs.overlapping_time')
    def test_overlapping_days(self, mock_time, mock_days):
        
        data = [{"Day": "Monday", "Start": "09:00", "End": "11:00"}, 
        {"Day": "Friday", "Start": "10:00", "End": "11:00"}, 
        {"Day": "Monday", "Start": "09:00", "End": "11:00"}
    ]
        
        #new solution
        
        #trying all combinations of true/false
        for mock_day in [True, False]:
            for mock_time in [True, False]:
                #sets mock values
                mock_days.return_value = mock_day
                mock_time.return_value = mock_time
                #tests the result(if both are true -> True - otherwise -> False)
                self.assertEqual(mock_day and mock_time, o.interf_run(data))
                #checks if mocks were called correctly
                mock_days.assert_called_once_with(data=data)
                mock_time.assert_called_once_with(data=data)
                #resets for the next loop
                mock_days.reset_mock()
                mock_time.reset_mock()
        
        
        
        #       not as effective
        # funcs.overlapping_days()
        # funcs.overlapping_time()
        
        # mock_days.assert_called_once()
        # mock_time.assert_called_once()
if __name__ == '__main__':
    unittest.main()
        