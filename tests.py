'''
Module for testing classes.
'''
from main import *

def test_StudentsClass():
    '''
    Tests classes.
    '''
    print('Testing UCU classes...')
    #First we'll test simple class to create person:
    person = Person('Bohdan', 'Borkivskyy')
    assert str(person) == 'Hello, Bohdan!'

    #Let's create some programs!
    #All subjects have points 0 by default:
    cs = Program('CS', {'Discrete Math' : 0, 'Math Analysis' : 0, 'OP' : 0})
    ba = Program('BA', {'Econom analysis' : 0, 'Math Analysis' : 0, 'OP' : 0})

    assert str(ba) == "BA program has such subjects: ['Econom analysis', 'Math Analysis', 'OP']."

    #Than let`s create a student - a person, who also has subjects of different program:
    student1 = Student('Marta', 'Sumyk', cs)

    assert isinstance(student1, Person) == True
    assert isinstance(student1, Student) == True
    #Now let`s add some subjects and grades:
    student1.program.subjects['OP'] = 80
    student1.program.subjects['Discrete Math'] = 59

    #Also we can add subjects that are not from a program`s list:
    student1.program.subjects['History'] = 55
    assert len(student1.program.subjects) == 4
    #Now we will test if student has talons:
    assert student1.test_talon() == 'Marta has 3 talons.'

    #Also we can add subjects to the student`s list:
    student1.add_subject('Svitoglyadne yadro', 30)
    assert len(student1.program.subjects) == 5

    op_task = Task('OP', 4)
    op_task.check_task(True)
    student1.add_task(op_task)

    assert student1.program.subjects[op_task.subject] == 84
    math_analysis_task = Task('Math Analysis', 2)
    math_analysis_task.check_task(False)
    assert student1.add_task(math_analysis_task) == 'The task was done incorrect.'

    cs_group = Group()
    student2 = Student('Nazar', 'secret_surname', cs, 3)
    student3 = Student('Kostya', 'secret_surname', cs, 3)
    student4 = Student('Bohdan', 'secret_surname', cs, 4)
    student5 = Student('Vlad', 'secret_surname', cs, 2)
    student6 = Student('Tetyana', 'secret_surname', cs, 1)
    student7 = Student('secret_name', 'Shamanskiy', cs, 2)
    student8 = Student('Ivan', 'secret_surname', cs)

    cs_group.add_student(student1)
    cs_group.add_student(student2)
    cs_group.add_student(student3)
    cs_group.add_student(student4)
    cs_group.add_student(student5)
    cs_group.add_student(student6)
    cs_group.add_student(student7)
    cs_group.add_student(student8)

    assert len(cs_group.students) == 8

    #By method 'delete_students()' we can delete students that have 3 or more talons:
    cs_group.delete_students()
    assert len(cs_group.students) == 4
    print('Done!')


if __name__ == '__main__':
    test_StudentsClass()
