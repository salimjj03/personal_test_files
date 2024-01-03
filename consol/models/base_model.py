#!/usr/bin/python3
""" This is the baseModel """


import uuid
import datetime
import models


class BaseModel:
    """ The base class """

    def __init__(self, *args, **kwargs):
        """ This method create the class
        constructors """
        
        if kwargs:
            for i, j in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    j = datetime.datetime.strptime(j, '%Y-%m-%dT%H:%M:%S.%f')
                if i != "__class__":
                    setattr(self, i, j)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.utcnow()
            self.updated_at = datetime.datetime.utcnow()
            models.storage.new(self)

    def __str__(self):
        """ This mothod print the str rep of the object
        """

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute
        updated_at with the current datetime """

        self.updated_at = datetime.datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """  returns a dictionary containing all
        keys/values of __dict__ of the instance """

        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
    
