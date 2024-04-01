from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map.png')
def map_image():
    # Here you can call your map.py logic to generate the map image
    map_image_path = 'image.png'
    return send_file(map_image_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
