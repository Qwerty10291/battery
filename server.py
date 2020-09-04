from flask import Flask, request, render_template
import requests

app = Flask(__name__)
coords = []

def get_adress(ip):
    return requests.get('http://ip-api.com/json/' + ip).json()

@app.route('/auth')
def auth():
    global coords
    coord = get_adress(request.remote_addr)
    coords.append([coord['lat'], coord['lon']])
    print(coords)

@app.route('admin')
def admin():
    return render_template('test.html', lat=coords[-1][0], lon=coords[-1][1])

if __name__ == '__main__':
    app.run(host='0.0.0.0')