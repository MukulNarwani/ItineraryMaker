import mysql.connector
from mysql.connector import Error
import csv 

def cityCSVSaver(city):
    city_csv_line=city.get_csv_line()
    city_activities=city.loActivity
    with open(city.location,'w') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow([city_csv_line])
        for activity in city_activities:
            writer.writerow([activity.get_csv_line()])