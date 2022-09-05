#!/usr/bin/python3
"""all common attributes/methods for other classes"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """
    id: assign with an uuid when an instance is created.
    created_at: datetime - assign with the current datetime
                when an instance is created
    updated_at: datetime - assign with the current datetime
                when an instance is created
                and it will be updated every time
    """
    def __init__(self, *args, **kwargs):
        """
        public instance attributes initialization
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """
            print: [<class name>] (<self.id>) <self.__dict__>
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def save(self):
        """
            updates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all
            keys/values of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        return new_dict
