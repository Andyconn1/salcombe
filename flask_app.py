from flask import Flask, render_template

app = Flask(__name__)

# Dummy data for demonstration purposes
dummy_data = {
    "host": {
        "name": "Your Host Name",
        "phone": "123-456-7890",
        "email": "host@email.com",
    },
    "emergency": {
        "police": "999",
        "medical": "999",
    },
    "salcombe": {
        "overview": "Nestled in the heart of the South Hams...",
        "points_of_interest": ["Salcombe Harbour", "South Sands Beach", "Overbeck's Garden"],
        "activities": ["Sailing", "Coastal walks", "Water sports"],
    },
    # Add more dummy data for other sections
}

# Define routes for each section
@app.route('/')
def index():
    return render_template('index.html', host=dummy_data['host'])

@app.route('/welcome')
def welcome():
    return render_template('welcome.html', host=dummy_data['host'])

@app.route('/emergency')
def emergency():
    return render_template('emergency.html', emergency=dummy_data['emergency'])

@app.route('/salcombe')
def salcombe():
    return render_template('salcombe.html', salcombe=dummy_data['salcombe'])

# Add more routes for other sections

if __name__ == '__main__':
    app.run(debug=True)
