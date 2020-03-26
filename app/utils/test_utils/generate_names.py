import names
name = names.get_full_name()
users = []
from faker import Faker
faker = Faker()
import pdb

def parse_address(address_string):
    address_string_split = address_string.split('\n')
    address = address_string_split[0]
    city = address_string_split[1].split(',')[0]
    state_and_zip = address_string_split[1].split(',')[1][1:]
    state = state_and_zip.split(' ')[0]
    zipcode = state_and_zip.split(' ')[1]
    address_dict = {'address':address , 'city':city , 'state':state, 'zip':zipcode }
    return address_dict

for i in range(100):
    try:
        users.append({'first_name': names.get_first_name(gender='male'), 'last_name': names.get_last_name()}.update(parse_address(faker.address())))
    except Exception as e:
        pass
    try:
        users.append({'first_name': names.get_first_name(gender='female'), 'last_name': names.get_last_name()}.update(parse_address(faker.address())))
    except Exception as e:
        pass
