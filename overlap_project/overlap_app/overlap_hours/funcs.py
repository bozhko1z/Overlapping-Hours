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
    "All days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ],
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

    converted_inputs = {}



    for item in data:
        mapped_days = days_mapping[item["Day"]]

        for day in mapped_days:
            if day not in converted_inputs:
                converted_inputs[day] = []
            try:
                start = datetime.strptime(item["Start"], time_format).time()
                end = datetime.strptime(item["End"], time_format).time()
            except ValueError:
                print("invalid format")
                return False

            converted_inputs[day].append({"start": start, "end": end})

    for day in converted_inputs:
        converted_inputs[day].sort(key=lambda x: x["start"])

    # slot a      (called them slots for better understanding)
    for day in converted_inputs:
        relative_start = converted_inputs[day][0]["end"]
        for slot in converted_inputs[day][1:]:
            slot_start = slot["start"]
            slot_end = slot["end"]
            if slot_start <= relative_start:
                print("overlap")
                return False
            relative_start = slot_end

    print("no overlap")
    return True


def time_converting(day: str, time: str) -> int:
    dayNum = day_index[day]
    parts = time.split(":")
    hours = int(parts[0])
    minutes = int(parts[1])
    return dayNum * 24 * 60 + hours * 60 + minutes
