from overlap_app.overlap_hours.funcs import overlapping

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
    assert overlapping(data1) == False
    assert overlapping(data2) == True

def test_overlapping_time():
    assert overlapping(data1) == False
    assert overlapping(data2) == True