from datetime import datetime


days_mapping = {
    "Monday": ["Monday"],
    "Tuesday": ["Tuesday"],
    "Wednesday": ["Wednesday"],
    "Thursday": ["Thursday"],
    "Friday": ["Friday"],
    "Saturday": ["Saturday"],
    "Sunday": ["Sunday"],
    "Weekend": ["Saturday", "Sunday"],
    "Working days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "All days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
   }
day_index = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7,
   }


def overlapping(data):
   
   time_format = "%H:%M"
   
   converted_inputs = []
   
   if data == []:
       print("invalid input")
       return False
   
   for item in data:
       mapped_days = days_mapping[item["Day"]]
       
       try:
            # manual parsing
        #    start = time_converting(mapped_days[0] ,item["Start"])
        #    end = time_converting(mapped_days[0], item["End"])
           start = datetime.strptime(item["Start"], time_format).time()
           end = datetime.strptime(item["End"], time_format).time()
           
       except ValueError:
           print("invalid format")
           return False
       
       converted_inputs.append({
           "days": mapped_days,
           "start": start,
           "end": end
            })
    
        # slot a      (called them slots for better understanding)
   for i in range(len(converted_inputs)):
            # slot b
        for j in range(i + 1, len(converted_inputs)):
            # check if two slots have the same days
            commons = set(converted_inputs[i]["days"]) & set(converted_inputs[j]["days"])
            if commons:
                start1 = converted_inputs[i]["start"]
                end1 = converted_inputs[i]["end"]
                start2 = converted_inputs[j]["start"]
                end2 = converted_inputs[j]["end"]
                
                if not (end1 <= start2 or end2 <= start1):
                    print("Overlap")
                    return False
   print("no overlap")
   return True



def time_converting(day: str, time: str) -> int:
    dayNum = day_index[day]
    parts = time.split(":")
    hours = int(parts[0])
    minutes = int(parts[1])
    return dayNum * 24 * 60 + hours * 60 + minutes