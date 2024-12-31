
from django.db.models.fields.json import KT
from django.http import HttpResponse

from making_queries.models import Dog


# def using_kt(request):
#     dogs = Dog.objects.annotate(first_breed = KT("data__breed__1"), owner_name = KT("data__owner__name")).filter(first_breed__startswith='lhasa', owner_name="Bob")

#     return HttpResponse('success')