import mysql.connector
from mysql.connector import Error
try:
    mySQLconnection = mysql.connector.connect(host='localhost', database='test', user='root', password='')
    sql_select_Query = "SELECT * FROM `sup1` WHERE Hotelname like '%Catina%'"
    cursor = mySQLconnection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    print("Total number of rows in categories", cursor.rowcount)
    print("Printing each row's column value i.e. categories")
    i = 1
    for row in records:
        print(i)
        print("Hotelname = ", row[0])
        print("Hotelid = ", row[1])
        print("Address = ", row[2])
        print("Cityname = ", row[3])
        print("Citycode = ", row[4])
        print("CountryCode = ", row[5])
        print("CoutryName = ", row[6])
        print("Payment = ", row[7])
        print("Tel No. = ", row[8])
        print("FAX No. = ", row[9])
        print("Latitude = ", row[10])
        print("Longtitude = ", row[11])
        print("Star = ", row[12])
        print("#room = ", row[13])
        print("Email = ", row[14], "\n")
        i += 1
    cursor.close()



except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if(mySQLconnection .is_connected()):
        #connection.close()
        print("MySQL connection is closed")


"""
 class DataProvider(object):
    def __init__(self, *args):
        super(DataProvider, self).__init__(*args))
"""        