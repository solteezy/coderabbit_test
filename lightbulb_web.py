from flask import Flask, render_template
from datetime import datetime
import json

app = Flask(__name__)

def load_lightbulb_data():
    try:
        file = open('lightbulb_data.json', 'r')
        data = json.load(file)
        file.close()
        return data['lightbulbs']
    except FileNotFoundError:
        print("Warning: lightbulb_data.json not found")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON in lightbulb_data.json")
        return []

@app.route('/')
def home():
    return render_template('lightbulbs.html',
                         current_year=datetime.now().year)

@app.route('/about')
def about():
    return render_template('about.html',
                         current_year=datetime.now().year)

@app.route('/types')
def bulb_types():
    lightbulbs = load_lightbulb_data()
    return render_template('types.html',
                         lightbulbs=lightbulbs,
                         current_year=datetime.now().year)

if __name__ == '__main__':
    app.run(debug=True)

