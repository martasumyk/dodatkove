'''
UCU student module.
'''
class Person:
    '''
    Class to create typical person.
    '''
    def __init__(self, name: str, surname: str):
        '''
        Initializes the data.
        '''
        self.name = name
        self.surname = surname

    def __str__(self):
        '''
        Returns the string to greet with the person.
        '''
        return f'Hello, {self.name}!'

class Student(Person):
    '''
    Class to create a student.
    '''
    def __init__(self, name, surname):
        '''
        Initialize the data.
        '''
        super().__init__(name, surname)
        self.subjects = dict()

    def test_talon(self):
        '''
        Tests it person has talons.
        '''
        talons = 0
        for i in self.subjects.items():
            if i[1] < 60:
                talons += 1
        if talons == 0:
            return f'Congratulations! {self.name} closed all the subjects!'
        return f'{self.name} has {talons} talons.'

    def add_subject(self, subject, grade=0):
        '''
        Adds subject to the student`s list.
        '''
        self.subjects[subject] = grade

class Task:
    '''
    Class to create task.
    '''
    def __init__(self, subject, weight):
        '''
        Initializes the data.
        '''
        self.subject = subject
        self.weight = weight
        self.correct = False

    def check_task(self, correct: bool):
        '''
        Checks task.
        '''
        if correct:
            self.correct = True


