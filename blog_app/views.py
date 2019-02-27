from django.shortcuts import render


# from django.http import HttpResponse
# Create your views here.
from blog_app.forms import BlogPostForm

# default page user gets to when loads
def index(request):
    return render(request, 'blog_app/index.html')

# page for user ti enter info into the form
def blog_entry(request):
    entryOfBlog = BlogPostForm()
    # post submit retrieves all info from form and stores it
    if request.method == "POST":
        print("Your data has been received")

        entryOfBlog = BlogPostForm(request.POST)
        if entryOfBlog.is_valid():
            entryOfBlog.save(commit=True)
            return index(request)
        else:
            print("The data you entered is incorrect. So please try again.")

    return render(request, "blog_app/blog_entry.html", {'blogentry': entryOfBlog})
