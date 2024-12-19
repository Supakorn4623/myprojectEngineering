from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def field_detail(request):
    field_info = {
        'name': 'Football Field1',
        'location': '123 Football Avenue, City',
        'price_per_hour': 300,
        'description': 'A high-quality football field with night lighting and great facilities.',
    }
    return render(request, 'field_detail.html', {'field': field_info})