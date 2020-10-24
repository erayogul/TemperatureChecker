# -*- coding: utf-8 -*-
import requests
import json
import mysql.connector
import time
import datetime

now = datetime.datetime.now();
time = now.strftime("%d/%m/%Y %H:%M:%S");

try:
 mydb = mysql.connector.connect(
    host="localhost",
    user="DBUsername",
    passwd="DBPassword",
    database="DBNAme",
    charset='utf8',
    autocommit=True,
 )
finally:

th1_temp_max = 45;
th1_temp_min = 5;
th1_hum_max = 75;
th1_hun_min = 47;

th2_temp_max = 35;
th2_temp_min = 18;
th2_hum_max = 75;
th2_hun_min = 47;

Room1 = 0
Room2 = 0

temperature1 = 0
temperature2 = 0
humidity1 = 0
humidity2 = 0

try:

  s1 = requests.get('Room1_IPAdress')
  values1 = s1.text
  x = values1.split("/")
  temperature1 = float(x[0])
  humidity1 = float(x[1])
  Room2 = 1

except:

  Room1 = 0


try:

  s2 = requests.get('Room2_IPAdress')
  values2 = s2.text
  y = values2.split("/")
  temperature2 = float(y[0])
  humidity2 = float(y[1])
  Room1 = 1

except:
  Room2 = 0



mycursor = mydb.cursor()
sql_log = "INSERT INTO temperature_logs (sensor_1,time_1,temperature_1,hum_1,sensor_2,time_2,temperature_2,hum_2) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" %("Room2 Room",time,temperature1,humidity1,"Room1 Area",time,temperature2,humidity2)
mycursor.execute(sql_log)

if (Room2 == 1):

 if((temperature1 < th1_temp_min  or temperature1 > th1_temp_max  ) or (humidity1 < th1_hun_min or humidity1 > th1_hum_max)):
	uri = 'https://RocketChatAdress.com/hooks/rocketchatToken'
	data={}
	data = {
	    "username": "TemperatureChecker",
	    "icon_url":"user image url",
	    "attachments": [
	        {
	            "title": "Temperature Allert! Temperature:"+str(temperature1)+"/Humidity:"+str(humidity1),
	            "color":"#8d0000"
	        }
	    ]
	}
	request_sys = requests.post(uri, json.dumps(data)).content

 else:


if(Room1 == 1):
 if((temperature2 < th2_temp_min  or temperature2 > th2_temp_max  ) or (humidity2 < th2_hun_min or humidity2 > th2_hum_max)):
  uri = 'https://RocketChatAdress.com/hooks/rocketchatToken'
  data={}
  data = {
      "username": "TemperatureChecker",
      "icon_url":"user image url",
      "attachments": [
          {
              "title": "Temperature Allert! Temperature:"+str(temperature1)+"/Humidity:"+str(humidity1),
              "color":"#8d0000"
          }
      ]
  }
  request_sys = requests.post(uri, json.dumps(data)).content

 else:

