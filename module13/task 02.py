from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = "airports.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/airport/<icao>", methods=["GET"])
def get_airport(icao):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT ident, name, municipality FROM airport WHERE ident = ?",
        (icao.upper(),)
    )

    airport = cursor.fetchone()
    conn.close()

    if airport is None:
        return jsonify({"error": "Airport not found"}), 404

    response = {
        "ICAO": airport["ident"],
        "Name": airport["name"],
        "Location": airport["municipality"]
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)