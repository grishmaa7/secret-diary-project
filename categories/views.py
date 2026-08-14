from django.shortcuts import render, redirect
from .models import Category
from django.contrib.auth.decorators import login_required

@login_required
def categories_page(request):
    categories = Category.objects.all()

    return render(
        request,
        'categories.html',
        {'categories': categories}
    )

@login_required
def create_category(request):
    if request.method == 'POST':
        Category.objects.create(
            name=request.POST['name'],
            description=request.POST['description']
        )

        return redirect('categories')

    return render(request, 'category_form.html')