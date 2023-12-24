import dataclasses


@dataclasses.dataclass
class User:
    email: str
    password: str


olga = User(email='o.lgaromanovna@yandex.ru', password='5sWQmGDHzeDv3+x')
