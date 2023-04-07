'''
Module for testing classes.
'''
from main import *
def test_StudentsClass():
    '''
    Tests classes.
    '''
    #First we'll test simple class to create person:
    person = Person('Bohdan', 'Borkivskyy')
    assert str(person) == 'Hello, Bohdan!'

    #Than let`s create a student - a person, who also has subjects:
    student1 = Student('Marta', 'Sumyk')
    assert student1.subjects == dict()
    #Now let`s add some subjects and grades:
    student1.subjects['OP'] = 80
    student1.subjects['Math'] = 59
    student1.subjects['History'] = 55
    assert len(student1.subjects) == 3
    #Now we will test if student has talons:
    assert student1.test_talon() == 'Marta has 2 talons.'

    #Also we can add subjects to the student`s list:
    student1.add_subject('Svitoglyadne yadro', 30)
    assert len(student1.subjects) == 4


    print('Done!')



if __name__ == '__main__':
    test_StudentsClass()