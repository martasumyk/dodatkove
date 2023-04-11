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
        self.talons = 0

    def test_talon(self):
        '''
        Tests if person has talons.
        '''
        for i in self.subjects.items():
            if i[1] < 60:
                self.talons += 1
        if self.talons == 0:
            return f'Congratulations! {self.name} closed all the subjects!'
        return f'{self.name} has {self.talons} talons.'

    def add_subject(self, subject, grade=0):
        '''
        Adds subject to the student`s list.
        '''
        self.subjects[subject] = grade

    def add_task(self, task):
        '''
        Adds the task to a student - if it`s correct student gain points.
        '''
        if task.correct:
            self.subjects[task.subject] += task.weight
        else:
            return f'The task was done incorrect.'


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


class Group:
    '''
    Class to create group of students.
    '''
    def __init__(self):
        '''
        Initializes the data.
        '''
        #At first group is an empty list:
        self.students = []

    def add_student(self, student: Student):
        '''
        Method that allows adding student to the group list.
        '''
        if isinstance(student, Student):
            self.students.append(student)

    def delete_students(self):
        '''
        Method to check if we have students that are going to be fired.
        '''
        if self.students:
            for student in self.students:
                student.test_talon()
                if student.talons >= 3:
                    self.students.remove(student)
        return f'We have {len(self.students)} students left.'


