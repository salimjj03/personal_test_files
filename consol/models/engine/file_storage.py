#!/usr/bin/python3
""" file storage """

import json
from models.base_model import BaseModel

class FileStorage:
    """ file storage """

    __file_path = "file.json"
    __objects = {}


    def all(self):
        """ return s all object """

        return self.__objects

    def new(self, obj):
        """ set the object """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ to json file """

        data = {}
        for key in self.__objects:
            data[key] = self.__objects[key].to_dict()

        with open(self.__file_path, "w") as my_file:
            json.dump(data, my_file)

    def reload(self):
        """ from json """

        try:
            with open(self.__file_path, "r") as my_file:
                data = json.load(my_file)
                for key, value in data.items():
                    class_n, o_id = key.split(".")
                    ob_class = globals()[class_n]
                    obj = ob_class(**value)
                    self.new(obj)
        except Exception:
            pass

