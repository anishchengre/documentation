from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Avg, Max
from aggregation.models import Book, Publisher
from django.db.models import FloatField
from django.db.models import Count
from django.db.models import Q
# Create your views here.


def cheat_sheet(request):
    # Total number of books.
    books = Book.objects.count()

    # Total number of books with publisher=BaloneyPress
    books = Book.objects.filter(publisher__name="Asmita  Publication").count()
    
    #Average price across all books, provide default to be returned instead of None if no books exist.
    books = Book.objects.aggregate(Avg("price", default=0))


    # Max price across all books, provide default to be returned instead of  None if no books exist.
    books = Book.objects.aggregate(Max("price", default=0))

    # Difference between the highest priced book and the average price of all books.
    books  = Book.objects.aggregate(price_difference=Max('price', output_field=FloatField()) - Avg('price', output_field=FloatField()))
    # print(books)


    # All the following queries involve traversing the Book<->Publisher
    # foreign key relationship backwards.

    # Each publisher, each with a count of books as a "num_books" attribute.
    publishers = Publisher.objects.annotate(num_books = Count('book'))
    # print(publishers[0].num_books)

    # Each publisher, with a separate count of books with a rating above and below 5
    above_4point5 = Count("book", filter=Q(book__rating__gt=4.5))
    below_5 = Count("book", filter=Q(book__rating__lte=5))
    pubs = Publisher.objects.annotate(below_5=below_5).annotate(above_5=above_4point5)
    # print(pubs[0].above_5)


    # The top 5 publishers, in order by number of books.
    pubs = Publisher.objects.annotate(num_books=Count("book")).order_by("-num_books")[:5]
    print(pubs)
    return HttpResponse("success")