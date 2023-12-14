from django.test import TestCase

from .models import (
    Class,
    Grade,
    Student
)

class DatabaseStructureTest(TestCase):
    """Test the basic structure of the relational database.

    This Class holds a number of tests, which should test if the database structure is sufficient
    for the use-case of a Grade-System 

    """
    def test_insert_class_and_students(self):
        """Test if a Class can be created and Students can be added to that Class-instance.

        """
        classInstance = Class.objects.create(
            className="3a",
        )
        studentLea = Student.objects.create(
            firstName="Lea",
            lastName="Muster",
            classRelation=classInstance,
        )
        studentMax = Student.objects.create(
            firstName="Max",
            lastName="Müller",
            classRelation=classInstance,
        )

        gradeLea1 = Grade.objects.create(
            points=5,
            weight=0.333,
        )
        gradeLea2 = Grade.objects.create(
            points=4,
            weight=0.333,
        )
        gradeLea3 = Grade.objects.create(
            points=3,
            weight=0.333,
        )
        studentLea.grades.add(gradeLea1, gradeLea2, gradeLea3)