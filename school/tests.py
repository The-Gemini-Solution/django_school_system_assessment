from django.test import SimpleTestCase

from school.models import Teacher

# Create your tests here.
class TeacherModelTests(SimpleTestCase):
    def test_first_name_calculated_correctly(self):
        """
        Test that the first name is pulled from the full name correctly when the full name
        is populated.
        """

        expected = "John"

        full_name = "John Smith"

        teacher = Teacher(full_name=full_name)

        result = teacher.first_name

        self.assertEqual(result, expected)

    def test_first_name_with_no_full_name(self):
        """
        Test that the first name is returned as None when the full name has not been populated.
        """

        expected = None

        full_name = None

        teacher = Teacher(full_name=full_name)

        result = teacher.first_name

        self.assertEqual(result, expected)

    def test_surname_calculated_correctly(self):
        """
        Test that the surname is pulled from the full name correctly when the full name
        is populated.
        """

        expected = "Smith"

        full_name = "John Smith"

        teacher = Teacher(full_name=full_name)

        result = teacher.surname

        self.assertEqual(result, expected)

    def test_surname_with_no_full_name(self):
        """
        Test that the surname is returned as None when the full name has not been populated.
        """

        expected = None

        full_name = None

        teacher = Teacher(full_name=full_name)

        result = teacher.surname

        self.assertEqual(result, expected)

    def test_middle_name_calculated_correctly(self):
        """
        Test that the middle name(s) is pulled from the full name if the full name has been
        populated.
        """

        expected = "M1 M2"

        full_name = "John M1 M2 Smith"

        teacher = Teacher(full_name=full_name)

        result = teacher.middle_name

        self.assertEqual(result, expected)

    def test_string_representation(self):
        """
        Test that the teacher's string representation is correctly built from the full full_nam
        and subject specialty.
        """

        expected = "John Smith [Maths]"

        full_name = "John M1 M2 Smith"
        subject_specialty = "Maths"

        teacher = Teacher(full_name=full_name, subject_specialty=subject_specialty)

        result = str(teacher)

        self.assertEqual(result, expected)
