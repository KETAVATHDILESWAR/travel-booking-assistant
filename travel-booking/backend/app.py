from flask import Flask, render_template, request, jsonify
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    host="database-1.ctcmgywsktm4.ap-south-1.rds.amazonaws.com",
    user="admin",
    password="YOUR_RDS_PASSWORD",
    database="travel_booking"
)

@app.route('/')
def home():
    return render_template('index.html')

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
