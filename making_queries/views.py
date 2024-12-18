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
