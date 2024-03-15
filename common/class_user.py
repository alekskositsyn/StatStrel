class User:
    def __init__(self, first_name, last_name, user_id=None, group_id=None, is_operator=0,
                 middle_name=None, personal_number=None, birth_date=None,
                 identity_number=None, degree=None):
        self.user_id = user_id
        self.group_id = group_id
        self.is_operator = is_operator
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.personal_number = personal_number
        self.birth_date = birth_date
        self.identity_number = identity_number
        self.degree = degree
