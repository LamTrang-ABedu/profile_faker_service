from faker import Faker

def generate_profile(locale='en_US'):
    fake = Faker(locale)
    profile = fake.profile()
    parent = fake.profile()
    return {
        'first_name': profile['name'].split()[0],
        'last_name': profile['name'].split()[-1],
        'name': profile['name'],
        'gender': profile['sex'],
        'dob': profile['birthdate'].isoformat(),
        'email': profile['mail'],
        'cell_phone': fake.phone_number(),
        'phone': fake.phone_number(),
        'ssn': fake.ssn(),
        'street': fake.street_address(),
        'city': fake.city(),
        'country': fake.country(),
        'zip_code': fake.postcode(),
        'parent': {
            'first_name': parent['name'].split()[0],
            'last_name': parent['name'].split()[-1],
            'email': parent['mail']
        }
    }
