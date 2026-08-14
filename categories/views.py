from django.shortcuts import render, redirect
from .models import Category


def categories_page(request):
    categories = Category.objects.all()

    return render(
        request,
        'categories.html',
        {'categories': categories}
    )


def create_category(request):
    if request.method == 'POST':
        Category.objects.create(
            name=request.POST['name'],
            description=request.POST['description']
        )

        return redirect('categories')

    return render(request, 'category_form.html')