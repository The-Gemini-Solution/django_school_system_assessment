from school.models import Class, Student


def get_class(class_pk: int) -> Class:
    """Return the class for the id"""
    return Class.objects.get(pk=class_pk)

def get_students_for_teacher(teacher_pk: int) -> "QuerySet[Student]":
    """Return all students that this teacher has taught or is teaching"""
    raise NotImplementedError

def get_math_or_english_students() -> "QuerySet[Student]":
    """Return all students that are in the math or english classes"""
    raise NotImplementedError
