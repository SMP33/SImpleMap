from flask import Flask, render_template, jsonify

i=0
app = Flask(__name__)
coords=[]

coord_file=open("coord.txt")

@app.route('/')
def index():
    
    return render_template('map.html')



@app.route('/current_position/', methods=['GET', 'POST'])
def _get_data():
    global i
    global coords

    if i>len(coords)-1:
        i=0

    
    data='{"geometry": {"type": "Point", "coordinates": ['+coords[i]+']}, "type": "Feature", "properties": {}}'
    i=i+1
    return data


if __name__ == "__main__":

    data=coord_file.readline()
    while data:
        coords.append(str(data))
        data=coord_file.readline()

    app.run(host = '0.0.0.0',port=5000)