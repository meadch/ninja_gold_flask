from flask import Flask, render_template, request, redirect, session
from random import randrange
app = Flask(__name__)
app.secret_key = "goldgoldgold"
search_settings = {
    'farm': {'min': 10 , 'max': 20},
    'cave': {'min': 5, 'max': 10},
    'house': {'min': 2, 'max': 5},
    'casino': {'min': -50, 'max': 50},
}

@app.route('/', methods=["GET"])
def index():
    if not 'total_gold' in session:
        session['total_gold'] = 0
    
    return render_template('index.html')

@app.route('/get_coins', methods=["POST"])
def gold_search():
    location = request.form['location']
    range_max = search_settings[location]['max']
    range_min = search_settings[location]['min']

    # generate random integer between particular range
    rand_gold = randrange(range_min, range_max + 1)

    session['total_gold'] += rand_gold

    print "TOTAL GOLD: ", session['total_gold']



    # Figure out gold logic according to the location

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
