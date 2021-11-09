import random

import pytest
import requests
from assertpy.assertpy import assert_that, soft_assertions
from uuid import uuid4
from json import dumps

BASE_URI = 'http://127.0.0.1:5000/api/people'


def test_db_has_user_kent():
    response = requests.get(BASE_URI)
    response_text = response.json()
    print(response_text)
    with soft_assertions():  #soft asserions above assert
        assert_that(response.status_code).is_equal_to(200)
        first_name = [people['fname'] for people in response_text]
        assert_that(first_name).contains('Kent')

# ILI via assertpy(https://github.com/assertpy/assertpy)
#     response = requests.get(BASE_URI)
#     response_text = response.json()
#     assert_that(response.status_code).is_equal_to(200)
#     assert_that(response_text).extracting('fname').is_not_empty().contains('Kent')


def test_new_person_can_be_added():
    unique_last_name = f'User {str(uuid4())}'
    payload = dumps({
        'fname': 'New',
        'lname': unique_last_name
    })

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.post(url=BASE_URI, data=payload, headers=headers)
    assert_that(response.status_code).is_equal_to(204)

    peoples = requests.get(BASE_URI).json()
    new_user = [person for person in peoples if person['lname'] == unique_last_name]
    assert_that(new_user).is_not_empty()


#delete
def search_users_by_last_name(peoples, unique_last_name):
    return [person for person in peoples if person['lname'] == unique_last_name]


def test_user_can_be_deleted():
    new_user_last_name = new_person_added()
    all_users, _ = get_all_users()
    new_user = search_users_by_last_name(all_users, new_user_last_name)[0]
    print(new_user)
    person_to_be_deleted = new_user['person_id']
    url = f'{BASE_URI}/{person_to_be_deleted}'
    response = requests.delete(url)
    assert_that(response.status_code).is_equal_to(200)


def get_all_users():
    response = requests.get(BASE_URI)
    peoples = response.json()
    return peoples, response


def new_person_added():
    unique_last_name = f'User {str(uuid4())}'
    payload = dumps({
        'fname': 'New',
        'lname': unique_last_name
    })

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.post(url=BASE_URI, data=payload, headers=headers)
    assert_that(response.status_code).is_equal_to(204)
    return unique_last_name

# @pytest.fixture
# def create_data():
#     payload = read_file("create_person.json")
#     random_no = random.randint(0, 1000)
#     last_name = f'0labini{random_no}'
#     payload['lname'] = last_name
#     yield payload
#
#
# def test_person_can_be_added_with_json_template(create_data):
#     create_person_with_unique_last_name(create_data)
#     response = requests.get(BASE_URI)
#     peoples = loads(response.text)