from flask import Flask, request, jsonify
import os
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    host="database-1.ctcmgywsktm4.ap-south-1.rds.amazonaws.com",
    user="admin",
    password="admin12345",
    database="travel_booking"
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

@app.route('/')
def home():
    return jsonify({"message": "Travel Booking API running"})


@app.route('/book', methods=['POST'])
def book():

    data = request.get_json()

    name = data['name']
    email = data['email']
    phone = data['phone']

    cursor = db.cursor()

    sql = """
    INSERT INTO users(name,email,password,phone)
    VALUES(%s,%s,%s,%s)
    """

    cursor.execute(sql, (name, email, "password123", phone))
    db.commit()

    return jsonify({"message": "Booking Successful"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
