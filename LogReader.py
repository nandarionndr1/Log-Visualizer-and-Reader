from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)




@app.route('/')
def index():

    sensor_types = ['Mag Switch S1', 'Mag Switch S2']
    total_ave = {}

    with open('wew.txt') as f:
        lines = f.read().splitlines()

    for sensor in sensor_types:
        prev_stamp = ""
        reading = False
        sum = 0.0
        ctr = 0.0
        for line in lines:
            sensor_name, stamp, val = line.split(",")
            if sensor_name == sensor:
                if val == '0':
                    reading = True
                if reading is True:
                    prev_stamp = stamp
                    reading = False
                else:
                    s1 = datetime.strptime(stamp, "%Y-%m-%d %H:%M:%S")
                    s2 = datetime.strptime(prev_stamp, "%Y-%m-%d %H:%M:%S")
                    date_diff = s1 - s2
                    date_diff = (date_diff).seconds
                    sum += int(date_diff)
                    ctr += 1
        print(sensor)
        print(sum,ctr)
        total_ave[sensor] = (sum/ctr)
        print (sum/ctr)

    return render_template('index.html', dick='dick', tite='tite', logs=lines,ave=total_ave)

if __name__ == '__main__':
    app.run(debug=True)
