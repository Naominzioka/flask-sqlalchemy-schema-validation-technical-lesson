# lib/validate_unknown.py 

from marshmallow import Schema, fields, post_load, ValidationError, INCLUDE
from pprint import pprint

# model

class Dog:
    def __init__(self, name, breed, tail_wagging=False, **kwargs):
        self.name = name
        self.breed = breed
        self.tail_wagging = tail_wagging
        self.__dict__.update(kwargs)
        
# schema

class DogSchema(Schema):
    name = fields.Str()
    breed = fields.Str()
    tail_wagging = fields.Boolean()

    @post_load
    def make_dog(self, data, **kwargs):
        return Dog(**data)

# validate during deserialization

friendly_dog = '{"name": "Snuggles","breed": "Beagle", "tail_wagging": true, "is_friendly" : true}'

try:
    result = DogSchema(unknown=INCLUDE).loads(friendly_dog)
    pprint(result.__dict__)

except ValidationError as err:
    print(err.messages)    # {'is_friendly': ['Unknown field.']}
    print(err.valid_data)  # {'name': 'Snuggles', 'breed': 'Beagle', 'tail_wagging': True}
    
