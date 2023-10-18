import bson
import pandas as pd
import json
from dataclasses import dataclass
from db import ItineraryDB
from typing import List


class Location():
    # TODO add coord limitations
    min_coord = 0

    def __init__(self, title: str, coordinates: tuple[int, int]):
        if title == "" or title == None:
            raise TypeError("Title can't be empty")
        if any(coord < self.min_coord for coord in coordinates):
            raise ValueError("Invalid Coordinates")
        self.title = title
        self.coordinates = coordinates

    def __iter__(self):
        tmp = {'title': self.title, 'coordinates': self.coordinates}
        for key, value in tmp.items():
            yield key, value

    def __dict__(self):
        return {'title': self.title, 'coordinates': self.coordinates}

    def __str__(self):
        return f'Location: {self.title}, coordinates:{self.coordinates}'

    def to_json(cls) -> str:
        return json.loads(json.dumps(dict(cls)))


class Activity():
    # TODO allow lists of location

    def __init__(self, title, coordinates, cost,):
        if cost == None:
            raise TypeError('Need a value for cost')
        if cost < 0:
            raise ValueError('Cost can\'t be negative')
        self.cost = cost
        self.location = Location(title, coordinates)

    def __repr__(self):
        return f'{self.location}, cost:{self.cost}'

    def __iter__(self):
        tmp = {'location': dict(self.location), 'cost': self.cost}
        for key, value in tmp.items():
            yield key, value

    def __dict__(self):
        return {'title': self.location, 'cost': self.cost}

    def to_json(cls) -> str:
        return json.loads(json.dumps(dict(cls)))

    @staticmethod
    def from_dic(doc):
        return Activity(doc['location']['title'],
                        doc['location']['coordinates'],
                        doc['cost'])


class City():

    def __init__(self, title, coordinates, loActivity):
        self.loActivity = loActivity
        if type(loActivity) != type(list()):
            self.loActivity = [loActivity]
        self.location = Location(title, coordinates)
        # print(type(loActivity))
        # print(type(self.loActivity))

    def append_activity(self, activity):
        self.loActivity.append(activity)

    def __repr__(cls):
        activities_str = ', '.join([str(activity)
                                    for activity in cls.loActivity])
        return f'City: {cls.location}, Activities: [{activities_str}]'

    def __dict__(cls):
        return {'City': {'Location': dict(cls.location),
                         'Activities': [dict(activity)
                                        for activity in cls.loActivity]}}

    def __iter__(self):
        for key, value in self.__dict__().items():
            yield key, value

    @staticmethod
    def from_dic(doc) -> object:
        activities = []
        doc = doc['City']
        loc = doc['Location']
        for activity in doc['Activities']:
            activities.append(Activity.from_dic(activity))
        return City(loc['title'], loc['coordinates'], activities)

    def to_json(cls) -> str:
        return json.loads(json.dumps(dict(cls)))


class Country:

    def __init__(self, cities: str) -> None:
        self.cities = []
        self.parse_json(cities)

    def parse_json(self, json_str):
        json_cities = json.loads(json_str)
        for city in json_cities:
            self.cities.append(City.from_dic(city))


class Model():

    def __init__(self) -> None:
        self.db = ItineraryDB()
        self.activeCountry = None

    def set_active_country(cls, country) -> None:
        if (country in cls.db.get_countries()):
            # load country
            cities = cls.db.get_cities(country)
            Country(cities)
        else:
            cls.db.add_country(country)

    def list_handler(cls, country=None, city=None):
        if not country:
            return cls.db.get_countries()
        elif city:
            cls.db.get_city(country, city)
        else:
            cls.db.get_cities(country)

    def add_handler(cls, city):
        cls.db.add_city(cls.activeCountry, city)

    def update_handler(cls, cityName, field: dict):
        cls.db.update_city(cls.activeCountry, cls.db.get_city(
            cls.activeCountry, cityName).title)

    def delete_handler(cls, city=None):
        if city:
            cls.db.delete_handler()
