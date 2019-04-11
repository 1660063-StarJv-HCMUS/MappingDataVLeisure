import mysql.connector
from mysql.connector import Error
import math
from math import radians, sin, cos, acos
import csv
from difflib import SequenceMatcher
import time


#################### def #######################################

# chuẩn hóa chuỗi


def standardizedString(str):
    str = str.replace("WSAS", "")
    return str


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


# distance between 2 point


def dist(point1, point2):
    R = 6371
    try:
        dLat = (float(point2[7]) - float(point1[7])) * (math.pi / 180)
        dLon = (float(point2[8]) - float(point1[8])) * (math.pi / 180)
        la1ToRad = float(point1[7]) * (math.pi / 180)
        la2ToRad = float(point2[7]) * (math.pi / 180)
        a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(la1ToRad) * \
            math.cos(la2ToRad) * math.sin(dLon / 2) * math.sin(dLon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = R * c
    except ValueError:
        d = -1
    return d


################### main ################################
start = time.time()
try:
    mySQLconnection = mysql.connector.connect(
        host='localhost', database='test', user='root', password='')

    # query1: SELECT `Hotelid`AS`HOTELID`, `Hotelname` as `HOTELNAME`, `CountryCode` as `COUNTRYCODE`,`CountryName`as`COUTRYNAME`, `Citycode` as `CITYCODE`, `Cityname` as `CITYNAME`,`Address` as `ADDRESS`, `Latitude` as `LATITUDE`, `Longtitude` as `LONGTITUDE` FROM `sup1` WHERE `COUNTRYCODE` like '%VN' and `CITYCODE` like '%SG%'
    # query2: SELECT `PRODUCT CODE`,`PRODUCT NAME`,`COUNTRY NAME`,`DESTINATION CITY`,`CITY NAME`, concat(`ADDRESS 1`,`ADDRESS 2`) as 'ADDRESS', `LATITUDE`,`LONGITUDE` FROM `sup2` WHERE 1

    sql_select_Query = "SELECT `Hotelid`AS`HOTELID`, `Hotelname` as `HOTELNAME`, `CountryCode` as `COUNTRYCODE`,`CountryName`as`COUTRYNAME`, `Citycode` as `CITYCODE`, `Cityname` as `CITYNAME`,`Address` as `ADDRESS`, `Latitude` as `LATITUDE`, `Longtitude` as `LONGTITUDE` FROM `sup1` "
    cursor = mySQLconnection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    sql_select_Query2 = "SELECT `PRODUCT CODE`,`PRODUCT NAME`,`COUNTRY NAME`,`DESTINATION CITY`,`CITY NAME`, concat(`ADDRESS 1`,`ADDRESS 2`) as 'ADDRESS', `LATITUDE`,`LONGITUDE` FROM `sup2` "
    cursor2 = mySQLconnection.cursor()
    cursor2.execute(sql_select_Query2)
    records2 = cursor2.fetchall()

    # print("Total number of rows in categories", cursor.rowcount)
    # print("Printing each row's column value i.e. categories")

    i = 0
    Hotels = []

    # Hotelid, Hotelname, CountryCode, CountryName, CityCode, CityName, Address, Latitude, Longtitude
    for row in records:
        tmp = []
        tmp.append(row[0])
        tmp.append(row[1])
        tmp.append(standardizedString(row[2]))
        tmp.append(row[3])
        tmp.append(standardizedString(row[4]))
        tmp.append(row[5])
        tmp.append(row[6])
        tmp.append(row[7])
        tmp.append(row[8])
        tmp.append("sup1")

        Hotels.append(tmp)
        i += 1
    cursor.close()

    Hotels2 = []
    for row in records2:
        tmp = []
        tmp.append(row[0])
        tmp.append(row[1])
        # tmp["CountryCode"] = ChuanHoa(row[2])
        tmp.append("")
        tmp.append(row[2])
        tmp.append(row[3])
        tmp.append(row[4])
        tmp.append(row[5])
        tmp.append(row[6])
        tmp.append(row[7])
        tmp.append("sup2")

        Hotels2.append(tmp)
        i += 1
    cursor2.close()

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (mySQLconnection.is_connected()):
        mySQLconnection.close()
        print("MySQL connection is closed")

    file = open("Record.txt", "w+", encoding="utf-8")

    for Hotel in Hotels:
        file.write(str(Hotel))
        for Hotel2 in Hotels2:
            if dist(Hotel, Hotel2) <= 1 and dist(Hotel, Hotel2) != -1:
                if similar(Hotel[1], Hotel2[1]) > 0.5:
                    file.write(str(Hotel2))
                    Hotels2.remove(Hotel2)
        file.write("\n")

    for Hotel2 in Hotels2:
        file.write(str(Hotel2) + "\n")

    file.close()

    print(time.time() - start)
#########################################################
