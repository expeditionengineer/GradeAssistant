from django.test import TestCase
from django.contrib.auth.models import User

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
        adminUser = User.objects.filter(username="admin")
        classInstance = Class.objects.create(
            className="3a",
            user=adminUser[0],
        )
        studentLea = Student.objects.create(
            firstName="Lea",
            lastName="Muster",
            classRelation=classInstance,
            user=adminUser[0],
        )
        studentMax = Student.objects.create(
            firstName="Max",
            lastName="Müller",
            classRelation=classInstance,
            user=adminUser[0],
        )

        gradeLea1 = Grade.objects.create(
            points=5,
            weight=0.333,
            user=adminUser[0],
        )
        gradeLea2 = Grade.objects.create(
            points=4,
            weight=0.333,
            user=adminUser[0],
        )
        gradeLea3 = Grade.objects.create(
            points=3,
            weight=0.333,
            user=adminUser[0],
        )
        studentLea.grades.add(gradeLea1, gradeLea2, gradeLea3)

        self.assertEqual(studentLea.grades.all().count(), 3)
        self.assertEqual(studentMax.grades.all().count(), 0)
        self.assertEqual(classInstance.student_set.all().count(), 2)
        self.assertEqual(classInstance.student_set.all()[0].grades.all().count(), 3)