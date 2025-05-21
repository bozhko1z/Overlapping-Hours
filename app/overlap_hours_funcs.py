from flask import Flask, render_template
from collections import Counter

app = Flask(__name__)

def overlapping_days(data):
    working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    weekend = ["Saturday", "Sunday"]
    all_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    #count how many times each day appears
    day_counter = Counter(entry["Day"] for entry in data)

    for day, count in day_counter.items():
        #if any day appears more than once it returns false
        if count > 1 and day["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] == all_days:
            print(f"Duplicate entries found for {day}: {count} times.")
            return False
        #if it's just once, everything's okay
        elif count == 1:
            print("No duplicates")
            return True


def overlapping_time(data):
    #sorts all the items by their Start value
    data.sort(key=lambda x: x['Start'])

    # checks for any overlaps
    for i in range(len(data) - 1):
        if data[i]['End'] > data[i + 1]['Start']:
            print("Overlap")
            return False
        else:
            return True
    
    
@app.route('/')
def index():
    return render_template('index.html')
    
    
if __name__ == '__main__':
    app.run(debug=True)