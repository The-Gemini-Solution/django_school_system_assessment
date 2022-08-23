Python/Django assessment.

Feel free to consult me and any documentation/sites you need. This is more about how you would do
things rather than testing that you know the exact syntax and functions off the top of your head.

Most of the relevant code lives in the school app.

A database with some data has been included in the repository. The sample dataset should have enough
data to demonstrate correctness in all of the tasks below.

Tasks to focus on:

- Implement the property function (first_name) to get the teacher's first name
- Implement the property function (surname) to get a teacher's surname
- Fix the model code so that the school.tests.TeacherModelTests.test_string_representation test
  passes.
- Identify the tests for the grade property function of the enrollment class. Any bugs?
- Allow the student, teacher, class and enrollment models to be administered by the admin backend.
  (Admin backend user: admin,password = admin1)
- Complete the school/view_class.html template. Specifically the section that would generate the
  student table. The enrollment score should only show if the student has completed the course,
  otherwise just show '-'.
- Currently we perform quite a few queries per execution of the view_class function. Optimize this
  code to be more efficient on db lookups. (Look at school/classes/1 as an example)
- Restrict the view class view to be login-only.
- Log in via the admin backend.
- Update the teacher named John Smith's specialty subject to 'English'
- How could the specialty subject be done better? We have a similar concept in the Class model.
- Implement the function get_students_for_teacher in the services.
- Implement the function get_math_or_english_students in the services.
- What are class based views and why would you use them (in general)?

Bonus Tasks:

- Implement the property function (middle_name) to get the teacher's middle name (assuming one exists)
- Implement the tests for the grade property function of the enrollment class. Fix the bugs that
  pop up.
