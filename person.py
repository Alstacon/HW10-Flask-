class Person:
    def __init__(self, database):
        self.id = database['id']
        self.name = database['name']
        self.picture = database['picture']
        self.position = database['position']
        self.gender = database['gender']
        self.age = database['age']
        self.skills = database['skills']

    def __repr__(self):
        return f"<p>Кандидат - {self.name}</p><p>Позиция - {self.position}</p><p>Скиллы - {self.skills}</p>"

    def index(self, database):
        """ Returns the full list of candidates"""
        for i in database:
            return f"<p>Кандидат - {self.name}</p>" \
                   f"<p>Позиция - {self.position}</p>" \
                   f"<p>Скиллы - {self.skills}</p>"

