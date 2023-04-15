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

    @property
    def fullname(self) -> str:
        ''' get persons full name '''
        return f"{self.name} {self.surname}"

    @fullname.setter
    def fullname(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Fullname must be str")

        if len(value.split(' ')) != 2:
            raise ValueError("Fullname must consist of 2 words: name and surname")

        self.name, self.surname = value.split(' ')

    def __str__(self):
        '''
        Returns the string to greet with the person.
        '''
        return f'Hello, {self.fullname}!'

class Program:
    '''
    Class of Program
    '''
    def __init__(self, name: str, subjects: list) -> None:
        self.name = name
        self.subjects = subjects

    def __str__(self) -> str:
        return f"{self.name} program has such subjects: {self.subjects}."

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

class Grades(dict):
    '''
    Create grades for 1 student
    '''
    def __init__(self, program: Program) -> None:
        super().__init__({subject: 0 for subject in program.subjects})

    def set_grade(self, subject: str, grade: int):
        '''
        Set grade for student
        '''
        self[subject] = grade

    def get_grade(self, subject: str):
        '''
        Get grade for subject
        '''
        if subject in self:
            return self[subject]

        raise ValueError(f"There's no subject {subject}")

    def add_task(self, task: Task):
        '''
        Add task for subject
        '''
        self[task.subject] += task.weight

    def get_average(self):
        '''
        get average grade
        '''
        return sum(self.values()) / len(self.values())


    @staticmethod
    def to_ECTS_grading(grade: int) -> str:
        '''
        Convert 1-100 grade to A-F
        '''
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be 0 <= grade <= 100")

        if grade >= 90:
            return "A"

        if grade >= 85:
            return "B"

        if grade >= 75:
            return "C"

        if grade >= 65:
            return "D"

        if grade >= 60:
            return "E"

        return "F"


class Student(Person):
    '''
    Class to create a student.
    '''
    def __init__(self, name, surname, program: Program, talons = 0):
        '''
        Initialize the data.
        '''
        super().__init__(name, surname)
        self.program = program
        self.grades = Grades(program)
        self.talons = talons

    def test_talon(self):
        '''
        Tests if person has talons.
        '''
        for grade in self.grades.values():
            if grade < 60:
                self.talons += 1

        if self.talons == 0:
            return f'Congratulations! {self.name} closed all the subjects!'

        return f'{self.name} has {self.talons} talons.'

    def add_subject(self, subject, grade = 0):
        '''
        Adds subject to the student`s list.
        '''
        self.grades.set_grade(subject, grade)

    def add_task(self, task):
        '''
        Adds the task to a student - if it`s correct student gain points.
        '''
        if task.correct:
            self.grades.add_task(task)
        else:
            return 'The task was done incorrect.'

    def get_average_grade(self) -> int:
        '''
        get student's average grade
        '''
        return round(self.grades.get_average(), 2)

    def get_ECTS_grades(self):
        '''
        convert student grades to ETCS grading system
        '''
        return {subject: Grades.to_ECTS_grading(grade) for (subject, grade) in self.grades.items()}


class Group:
    '''
    Class to create group of students.
    '''
    def __init__(self):
        '''
        Initializes the data.
        '''
        # At first group is an empty list:
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
