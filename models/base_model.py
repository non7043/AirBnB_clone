#!/usr/bin/python3
'''
'base_model'
'''

import uuid
from datetime import datetime

import models

class BaseModel():

    def __init__(self, *args, **kwargs):
        '''
        class constructor for class 'BaseModel'
        '''

        if kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''
        String representation of the class name, the id and the dict
        '''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''
        updates the public instance attribute
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
        a dictionary containing all keys/values of __dict__ of the instance
        :return: a dictionary containing all keys/values of __dict__ of the instance
        '''
        instance_dict = dict.__dict__
        instance_dict['created_at'] = self.__dict__['created_at'].isoformat()
        instance_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        instance_dict['__class__'] = self.__class__.__name__
        return instance_dict

