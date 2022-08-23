from django.contrib.admin.options import TemplateResponse
from django.http import HttpResponse
from django.shortcuts import render

import school.services as school_services

# Create your views here.


def view_class(request, class_pk: int):
    class_object = school_services.get_class(class_pk=class_pk)

    return TemplateResponse(
        request=request,
        template="school/view_class.html",
        context={"class_object": class_object},
    )
