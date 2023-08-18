import mysql.connector
from mysql.connector import Error
import csv 
import os
import glob
from model import *

class ItineraryDB():
    def __init__(self,path=os.getcwd()):
        self.db_path=path

    def cityCSVSaver(self,city):
        lines=[]
        if not(f'{city.location}_City' in os.listdir(os.getcwd())):
            city_csv_line=city.get_csv_line()
            lines.append(city_csv_line)
        city_activities=city.loActivity
        # csvfile.write(os.linesep)
        for activity in city_activities:
            lines.append(activity.get_csv_line())
            # csvfile.write(os.linesep)
        print(lines)
        with open(f'{self.db_path}/{city.location}_City','a') as csvfile:
            writer=csv.writer(csvfile,delimiter='\n')
            writer.writerow(lines)
    
    @staticmethod
    def get_cities():
        return  glob.glob(os.getcwd()+'/*_City')
    @staticmethod
    def load(city):
        return City.city_from_csv(city)