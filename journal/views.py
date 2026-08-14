

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Entry, Reflection
from .serializers import EntrySerializer, ReflectionSerializer
from django.shortcuts import render, redirect
from categories.models import Category


class EntryViewSet(viewsets.ModelViewSet):
    serializer_class = EntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Entry.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReflectionViewSet(viewsets.ModelViewSet):
    serializer_class = ReflectionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reflection.objects.filter(entry__owner=self.request.user)


def home(request):
    return render(request, 'home.html')


def entries_page(request):
    entries = Entry.objects.filter(owner=request.user)

    return render(
        request,
        'entries.html',
        {'entries': entries}
    )
def create_entry(request):
    if request.method == 'POST':
        Entry.objects.create(
            owner=request.user,
            title=request.POST['title'],
            content=request.POST['content'],
            mood=request.POST['mood'],
            category_id=request.POST['category']
        )

        return redirect('entries')

    categories = Category.objects.all()

    return render(
        request,
        'entry_form.html',
        {'categories': categories}
    )