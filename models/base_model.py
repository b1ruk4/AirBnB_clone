#!/usr/bin/python3
"""all common attributes/methods for other classes"""
from datetime import datetime
from uuid import uuid4


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
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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

    def to_dict(self):
        """
            returns a dictionary containing all
            keys/values of __dict__ of the instance
        """
        new_dict = self.__dict__
        new_dict['__class__'] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
