import os
from flask import Flask, render_template
import json

app = Flask(__name__)

# Construct the full path to profile_data.json
profile_data_path = "C:\\Users\\DELL\\Desktop\\portfolio\\static\\data\\profile_data.json"

# Load profile data from JSON file
with open(profile_data_path, 'r') as f:
    profile_data = json.load(f)

@app.route('/')
def home():
    return render_template('index.html', profile=profile_data)

@app.route('/about')
def about():
    return render_template('about.html', profile=profile_data)

@app.route('/projects')
def projects():
    return render_template('projects.html')

if __name__ == '__main__':
    app.run(debug=True)
