import mysql.connector
from geopy.distance import geodesic

def get_codes(icao):
    sql = f" SELECT latitude_deg,longitude_deg FROM airport WHERE ident = %s "
    cursor = connection.cursor()
    cursor.execute(sql,(icao,))
    result = cursor.fetchone()
    return result


connection = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='new_flight',
    user='root',
    password='maria1321',
    autocommit=True
)

icao1 = str(input("enter ICAO 1: "))
icao2 = str(input("enter ICAO 2: "))


def distance():
    pr1 = get_codes(icao1)
    pr2 = get_codes(icao2)
    distance_km = float(geodesic(pr1, pr2).kilometers)
    print(f"\nDistance between {icao1} and {icao2}: {distance_km:.2f} km")

distance()




