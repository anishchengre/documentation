from django.http import HttpResponse
from .models import Blog, Entry


def blogs_queryset(request):
    # blogs = Blog.objects.filter(entry__headline__contains="Lennon", entry__pub_date__year=2008)
    blogs = Blog.objects.exclude(entry__in=Entry.objects.filter(headline__contains="Lennon", pub_date__year=2008))

    sec_blogs = Blog.objects.filter(entry__headline__contains="Lennon").filter(entry__pub_date__year=2008)

    # Printing the results for the first query
    print("Blogs with headline containing 'Lennon' and published in 2008 (Single Query):")
    if blogs.exists():
        for blog in blogs:
            print(f"Blog Name: {blog.name}, Tagline: {blog.tagline}")
    else:
        print("No blogs found in the first query.")

    print("\n------------\n")

    # Printing the results for the second query
    print("Blogs with headline containing 'Lennon' and published in 2008 (Chained Qukeries):")
    if sec_blogs.exists():
        for blog in sec_blogs:
            print(f"Blog Name: {blog.name}, Tagline: {blog.tagline}")
    else:
        print("No blogs found in the second query.")

    return HttpResponse("Success")



# Filters can reference fields on the model¶

from django.db.models import F
from django.db.models import Min
from django.db.models import OuterRef, Subquery, Sum
# def filter_referencing_fields(request):
#     # entries = Entry.objects.filter(number_of_comments=F("number_of_pingbacks") * 2)
#     # entries = Entry.objects.filter(pub_date__year=F("mod_date__year"))
#     entries = Entry.objects.aggregate(first_published_year=Min("pub_date__year"))
#     print(entries)
#     return HttpResponse("Success")





def filter_using_outer_ref_and_sub_query(request):
   
    entries = Entry.objects.values("pub_date__year").annotate(
        top_rating=Subquery(
            Entry.objects.filter(
                pub_date__year=OuterRef("pub_date__year"),
            )
            .order_by("-rating")
            .values("rating")[:1]
        ),
        total_comments=Sum("number_of_comments"),
    )
    
    print(entries)
    return HttpResponse("sucess")

