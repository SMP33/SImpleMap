from flask import Flask, render_template, jsonify

i=0
app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('map.html')



@app.route('/current_position/', methods=['GET', 'POST'])
def _get_data():
    global i
    data='{"geometry": {"type": "Point", "coordinates": [133.24957409602325, -28.913106652318188]}, "type": "Feature", "properties": {}}'
    return data


if __name__ == "__main__":
    app.run(debug=False)