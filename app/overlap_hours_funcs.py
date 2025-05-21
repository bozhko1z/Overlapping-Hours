from flask import Flask, render_template, request
from collections import Counter

app = Flask(__name__, template_folder='../templates')

days = {"Working days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "Weekend": ["Saturday", "Sunday"],
        "All days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    }

def find_day(day):
    return days.get(day, [day])

def overlapping_days(data):
    #count how many times each day appears
    day_counter = Counter(day for entry in data for day in entry["Day"])

    for day, count in day_counter.items():
        #if any day appears more than once it returns false
        if count > 1:
            print(f"Duplicate entries found for {day}: {count} times.")
            return False
        else:
            print("No overlap")
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
    
    
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        
        days = request.form.getlist('Day')
        starts = request.form.getlist('Start')
        ends = request.form.getlist('End')
    
        inputs = []
    
        for i in range(len(days)):
            find_day = find_day(days[i])
            inputs.append({
                "Day": find_day,
                "Start": starts[i],
                "End": ends[i]
        })

        if(overlapping_days(inputs)):
            return "No overlap"
        else:
            return "Overlap"
    
    
    return render_template('index.html')
    
    
if __name__ == '__main__':
    app.run(debug=True)