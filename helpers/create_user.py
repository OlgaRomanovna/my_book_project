from faker import Faker
from faker.generator import random

fake = Faker()

email = fake.email()
password = fake.password(length=random.randint(10, 12))
