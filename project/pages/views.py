from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def home_page_view(request):
    context = {
        'title': 'Home Page',
        'inventory_list': [
            {'name': 'Item 1', 'price': 10.00, 'quantity': 5},
            {'name': 'Item 2', 'price': 20.00, 'quantity': 3},
            {'name': 'Item 3', 'price': 15.00, 'quantity': 8},
        ],
        'greeting': 'Welcome to the Home Page!',
    }
    return render(request, 'pages/home.html', context)

#def about_page_view(request):
   # context = {
   #     'title': 'About Page',
   #     'description': 'This is the about page.'
   # }
   # return render(request, 'pages/about.html', context)


class about_page_view(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Page'
        context['description'] = 'This is the about page.'
        context['contract_address'] = "12234556667 downUp UNlinkLink Road "
        context['phone_number'] = "123-456-7890"
        return context