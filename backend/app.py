from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('weather.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    #mock response for simplicity's sake
    data = {"city": city, "temperature": "25°C", "condition": "Clear"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)