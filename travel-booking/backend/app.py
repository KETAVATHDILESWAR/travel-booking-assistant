from flask import Flask, request, jsonify
import os
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    host=os.getenv("DB_HOST", "database-1.ctcmgywsktm4.ap-south-1.rds.amazonaws.com"),
    user=os.getenv("DB_USER", "admin"),
    password=os.getenv("DB_PASSWORD", "admin12345"),
    database=os.getenv("DB_NAME", "travel_booking")
)

@app.route("/")
def home():
    return jsonify({"message": "Travel Booking API running"})


@app.route("/book", methods=["POST"])
def book():

    data = request.get_json()

    name = data["name"]
    email = data["email"]
    phone = data["phone"]

    cursor = db.cursor()

    sql = """
    INSERT INTO users(name,email,password,phone)
    VALUES(%s,%s,%s,%s)
    """

    cursor.execute(sql, (name, email, "password123", phone))
    db.commit()

    cursor.close()

    return jsonify({"message": "Booking Successful"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
