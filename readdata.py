import mysql.connector
from mysql.connector import Error
import nltk
from nltk.corpus import stopwords
from string import(punctuation)
from nltk.tokenize import word_tokenize, sent_tokenize
import re

def RemoveStopWords(str):
    my_stopwords = set(stopwords.words('english')+list(punctuation))
    words = word_tokenize(str)
    words = [word.lower() for word in words]
    words = [word for word in words if word not in my_stopwords]
    return words

def RemoveSpecialKeys(str):
    string = re.sub('[^A-Za-z0-9]+', '', str)
    return string
def RemoveCityInHotelname(hotel, city):
    str= hotel.replace(city,'')
    return str
def formatHotelname(name, city):
    str=RemoveStopWords(name)
    str=RemoveSpecialKeys(str)
    str = RemoveCityInHotelname(str, city)
    return str
def formatCityName(name):
    str=RemoveStopWords(name)
    str=RemoveSpecialKeys(str)
    return str

def formatCountyName(name):
    str = RemoveStopWords(name)
    str = RemoveSpecialKeys(str)
    return str

class Hotel:
    def __init__(self, id, code, latitude,longtitude):
        self.id = id
        self.code = code
        self.latitude = latitude
        self.longtitude = longtitude
    def showInfo(self):
        print("id: ", self.id)
        print("code: ", self.code)
        print("Latitude: ", self.latitude, "Longtitude: ", self.longtitude) 
try:
    mySQLconnection = mysql.connector.connect(host='localhost', database='test', user='root', password='')
    sql_select_Query = "SELECT * FROM `sup1`"
    cursor = mySQLconnection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    print("Total number of rows in categories", cursor.rowcount)
    print("Printing each row's column value i.e. categories")
    i = 0
    ListHotel = []
    for row in records:
        ##############################
        
        id = row[1]
        code = formatHotelname(row[0],formatCityName(row[3]))+formatCityName(row[3])+formatCountyName(row[6])
        latitude = row[10]
        longtitude = row[11]
        tmp = Hotel(id,code,latitude,longtitude)
        ListHotel.append(tmp)
        ListHotel[i].showInfo()
        i+=1
        """
        print("Hotelname = ", row[0])
        print("Hotelid = ", row[1])
        #print("Address = ", row[2])
        print("Cityname = ", row[3])
        #print("Citycode = ", row[4])
        #print("CountryCode = ", row[5])
        print("CoutryName = ", row[6])
        #print("Payment = ", row[7])
        #print("Tel No. = ", row[8])
        #print("FAX No. = ", row[9])
        print("Latitude = ", row[10])
        print("Longtitude = ", row[11])
        #print("Star = ", row[12])
        #print("#room = ", row[13])
        #rint("Email = ", row[14], "\n")
        """
        i += 1
    cursor.close()

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if(mySQLconnection .is_connected()):
        #connection.close()
        print("MySQL connection is closed")