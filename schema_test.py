import json
import requests
from cerberus import Validator
from assertpy import assert_that

BASE_URI = 'http://127.0.0.1:5000/api/people'

schema = {
    'fname': {'type': 'string'},
    'lname': {'type': 'string'},
    'person_id': {'type': 'number'},
    'timestamp': {'type': 'string'}
}

def test_one_operation_has_expected_schema():
    response = requests.get(f'{BASE_URI}/1')
    person = json.loads(response.text)

    validator = Validator(schema, require_all=True)
    is_valid = validator.validate(person)

    assert_that(is_valid, description=validator.errors).is_true()

def test_all_operation_has_expected_schema():
    response = requests.get(f'{BASE_URI}')
    persons = json.loads(response.text)

    validator = Validator(schema, require_all=True)

    for person in persons:
        is_valid = validator.validate(person)
        assert_that(is_valid, description=validator.errors).is_true()