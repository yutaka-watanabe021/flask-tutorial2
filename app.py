from flask import Flask, render_template, request
import random
app = Flask(__name__)

import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("API_KEY")
print("API_KEY=",API_KEY)

@app.route('/')
def hello():
    unsei_list = ["大吉", "中吉", "小吉"]
    uranai = random.choice(unsei_list)
    return render_template('index.html', fortune=uranai, fortune_list=unsei_list)

@app.route('/fortune', methods=["GET", "POST"])
def fortune():
    unsei_list = ["大吉", "中吉", "小吉"]
    if request.method == 'POST':
        postedComment = request.form["comment"]
        num_of_days = int(request.form["num_of_days"])
        uranai_list = []

        for i in range(num_of_days):
            uranai_list.append({"day": str(i+1)+"日目", "fortune": random.choice(unsei_list)})

        return render_template('fortune.html', fortune_list=uranai_list, comment=postedComment)

    else: 

        uranai_list = [
            {"day": "今日", "fortune": random.choice(unsei_list)},
            {"day": "明日", "fortune": random.choice(unsei_list)},
            {"day": "明後日", "fortune": random.choice(unsei_list)},
        ]
    
        return render_template('fortune.html', fortune_list=uranai_list)

if __name__ == "__main__":
    app.run(debug=True)
    