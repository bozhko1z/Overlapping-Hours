from overlap_hours import funcs as f

data1 = [{"Day": "Monday", "Start": "09:00", "End": "11:00"}, 
        {"Day": "Friday", "Start": "10:00", "End": "11:00"}, 
        {"Day": "Monday", "Start": "09:00", "End": "11:00"}
    ]
data2 = [{"Day": "Monday", "Start": "09:00", "End": "11:00"}, 
        {"Day": "Friday", "Start": "09:00", "End": "11:00"}, 
        {"Day": "Wednesday", "Start": "09:00", "End": "11:00"}
    ]
data3 = [{"Day": "Monday", "Start": "09:00", "End": "11:00"}, 
        {"Day": "Monday", "Start": "12:00", "End": "14:00"}, 
        {"Day": "Monday", "Start": "15:00", "End": "17:00"}
    ]

def test_overlapping_days():
    assert f.overlapping_days(data1) == False
    assert f.overlapping_days(data2) == True

def test_overlapping_time():
    assert f.overlapping_time(data1) == False
    assert f.overlapping_time(data2) == True