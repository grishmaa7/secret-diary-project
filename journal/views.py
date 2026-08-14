

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Entry, Reflection
from .serializers import EntrySerializer, ReflectionSerializer
from django.shortcuts import render, redirect
from categories.models import Category
from django.shortcuts import get_object_or_404
from .models import Reflection

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

def entry_edit(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id, owner=request.user)

    if request.method == 'POST':
        entry.title = request.POST['title']
        entry.content = request.POST['content']
        entry.mood = request.POST['mood']
        entry.category_id = request.POST['category']
        entry.save()

        return redirect('entries')

    categories = Category.objects.all()

    return render(
        request,
        'entry_edit.html',
        {'entry': entry, 'categories': categories}
    )


def entry_delete(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id, owner=request.user)

    if request.method == 'POST':
        entry.delete()
        return redirect('entries')

    return render(
        request,
        'entry_confirm_delete.html',
        {'entry': entry}
    )

def entry_reflection(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id, owner=request.user)
    reflection = Reflection.objects.filter(entry=entry).first()

    if request.method == 'POST':
        content = request.POST['content']

        if reflection:
            reflection.content = content
            reflection.save()
        else:
            Reflection.objects.create(entry=entry, content=content)

        return redirect('entries')

    return render(
        request,
        'reflection_form.html',
        {'entry': entry, 'reflection': reflection}
    )