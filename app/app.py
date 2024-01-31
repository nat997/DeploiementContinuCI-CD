from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def connect_to_labdata_database():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'labdata'  # Use the 'labdata' database
    }
    return mysql.connector.connect(**config)

def fetch_degree_data():
    connection = connect_to_labdata_database()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM degree')
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

def fetch_timestamp_data():
    connection = connect_to_labdata_database()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM timestamp')
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

@app.route('/')
def index():
    degree_data = fetch_degree_data()
    timestamp_data = fetch_timestamp_data()
    response = {
        'Degree Data': degree_data,
        'Timestamp Data': timestamp_data
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0')