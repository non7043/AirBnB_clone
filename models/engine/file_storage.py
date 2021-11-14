#!/usr/bin/python3
'''
File storage class
'''

from models.base_model import BaseModel
from models.user import User
import json
from datetime import datetime
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity

class FileStorage():

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dictionary'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        type(self).__objects[type(obj).__name__+'.'+obj.id] = obj

    def save(self):
        '''Serializes __objects to the JSON file'''
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w",
                  encoding='utf-8') as write_file:
            json.dump(new_dict, write_file)

    def reload(self):
        '''
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        '''
        try:
            with open(FileStorage.__file_path, "r",
                      encoding='utf-8') as read_file:
                type(self).__objects = json.load(read_file)
            for key, value in type(self).__objects.items():
                obj = eval(type(self).__objects[key]['__class__'])(**value)
                type(self).__objects[key] = obj

        except FileNotFoundError:
            pass