                      Formset validation task for working hours

Validates a list of working hour inputs to ensure no overlapping time slots for the same days.

Expected Input:
  List of dicts containing the day, start and end time. 
  Example --> [{'Day': 'Monday', 'Start': '10:00', 'End': '12:00'}, {'Day': 'Friday', 'Start': '10:00', 'End': '12:00'}]
  
Expected Output:
  It returns True or Flase, depending if there is an overlapse or not.
