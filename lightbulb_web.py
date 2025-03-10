from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Sample data - in a real application, this would likely come from a database
lightbulbs = [
    {
        "type": "LED",
        "efficiency": "High",
        "lifespan": "50,000 hours",
        "cost": "Higher initial, lower long-term"
    },
    {
        "type": "Incandescent",
        "efficiency": "Low",
        "lifespan": "1,200 hours",
        "cost": "Low initial, higher long-term"
    },
    {
        "type": "CFL",
        "efficiency": "Medium",
        "lifespan": "8,000 hours",
        "cost": "Medium initial, medium long-term",
        "description": "Compact Fluorescent Lamp - An energy-efficient alternative to incandescent bulbs"
    }
]

@app.route('/')
def home():
    return render_template('lightbulbs.html', 
                         lightbulbs=lightbulbs,
                         current_year=datetime.now().year)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/types')
def bulb_types():
    return render_template('types.html', lightbulbs=lightbulbs)

if __name__ == '__main__':
    app.run(debug=True)

