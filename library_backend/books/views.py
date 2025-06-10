from django.shortcuts import render
from django.views.generic import ListView
from .models import Books

# Create your views here.
class booksListView(ListView):
    model = Books
    template_name = 'templates/books/books_list.html'  # Specify your template name here
    context_object_name = 'books'  # This will be the context variable in the template

    def get_queryset(self):
        return Books.objects.all()  # You can customize this to filter or order the books as needed
