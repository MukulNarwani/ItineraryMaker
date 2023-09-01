import mysql.connector
from mysql.connector import Error
import pandas as pd
import abc
import csv


class Location(metaclass=abc.ABCMeta):
    def __init__(self,location,coordinates):
        self.location=location
        self.coordinates=coordinates
    @abc.abstractmethod
    def get_csv_line(self):
        return f'{self.location}, {self.coordinates}'
    
    
class City(Location):
    #TODO CATCH ERRORS
    def __init__(self,location,coordinates,**loActivity):
        super().__init__(location,coordinates)
        if(type(loActivity)==list):
            self.loActivity=loActivity
        else:
            self.loActivity=list()
            
    def append_activity(self,activity):   
        self.loActivity.append(activity)

                        
class Activity(Location):
    #TODO CATCH ERRORS
    def __init__(self,title,coordinates,cost,):
        super().__init__(title,coordinates)
        self.cost=cost

    @staticmethod
    def from_csv(csv_line):
        #Throw catche rrror here
        line=[x.strip() for x in csv_line.split(', ')]
        try:
            return Activity(*line)
        except Exception as e:
            print(f'Failed loading {line}')
            print(e)
        