from student import Student
from gender import Gender
from personality import Personality
import names
import random

class Generator():
    @staticmethod
    def generate_name(gender = Gender.OTHERS) -> str:
        
        if gender is Gender.MALE:
            return names.get_full_name(gender=Gender.MALE.value)
        elif gender is Gender.FEMALE:
            return names.get_full_name(gender=Gender.FEMALE.value)
        else:
            return names.get_full_name()
    @staticmethod
    def generate_age() -> int:
        return 18
    @staticmethod
    def generate_gender() -> Gender:
        return random.choice(list(Gender))
    @staticmethod
    def generate_personality() -> Personality:
        return random.choice(list(Personality))
    @staticmethod
    def generate_relationship() -> dict:
        return {}
    @staticmethod
    def generateStudent() -> Student:
        return Student(Generator.generate_name(), Generator.generate_age(), Generator.generate_gender(),
                Generator.generate_personality(), Generator.generate_relationship())