# lib/required.py

from marshmallow import Schema, fields, ValidationError
from pprint import pprint

# schema

class HamsterSchema(Schema):
     name = fields.Str(required=True)
     breed = fields.Str()

hamster_data = [
    {"name": "Hammy", "breed": "Syrian"},   # valid  
    {"name": "Wiggles"},                    # valid, breed is not required
    {"breed": "Winter White"},              # invalid, name is required
    {}                                      # invalid, name is required
]

try:
    HamsterSchema(many=True).load(hamster_data)  #raises ValidationError
except ValidationError as err:
    print("Valid data:")
    print(err.valid_data)  # displays all valid data
    print("Invalid data:")
    print(err.messages)  # displays all validation errors