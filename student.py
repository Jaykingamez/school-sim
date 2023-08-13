class Student:
    """
    name:           Name of the student
    age:            Age of the student
    gender:         Gender of the student
    personality:    Personality of the student
    relationships:  Relationships students have with other students
    """
    def __init__(self, name, age, gender, personality, relationships = {}):
        self.name = name
        self.age = age
        self.gender = gender
        self.personality = personality
        self.relationships = relationships