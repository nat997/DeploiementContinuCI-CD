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

@app.route('/degree')
def degree():
    try:
        degree_data = fetch_degree_data()
    except mysql.connector.Error as err:
        # Return a mock response or error message if the database is unreachable
        degree_data = 'Database connection failed'

    return jsonify({'Degree Data': degree_data})

@app.route('/timestamp')
def timestamp():
    try:
        timestamp_data = fetch_timestamp_data()
    except mysql.connector.Error as err:
        # Return a mock response or error message if the database is unreachable
        timestamp_data = 'Database connection failed'

    return jsonify({'Timestamp Data': timestamp_data})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
