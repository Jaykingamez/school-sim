from room import Room
from student import Student
from generator import Generator

class Game():
    """
    This is a tech demo for a school sim

    Starting room will be the classroom
    Starting time will be 8, representing 8 am. 0 will represent 12 am.
    Time will be based of the 24 hour system
    People being generated are fellow students
    Teachers are WIP
    """
    def __init__(self):
        self.classroom  = Room("classroom")
        self.time = 8
        people = []
        for _ in range(10):
            people.append(Generator.generateStudent())
        for student in people:
            print(student.name)
            print(student.age)
            print(student.gender)
            print(student.personality)
            print(student.relationships)
        self.classroom = people
    
    def action_completed(self):
        self.time += 1