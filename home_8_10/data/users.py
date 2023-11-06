import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    month_birth: str
    year_birth: str
    day_birth: str
    subject: str
    hobby: str
    picture: str
    current_address: str
    state: str
    city: str