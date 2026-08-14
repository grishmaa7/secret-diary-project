from django.contrib import admin
from django.urls import path, include
from journal.views import home, entries_page, create_entry, entry_edit, entry_delete
from categories.views import categories_page, create_category

urlpatterns = [
    path('admin/', admin.site.urls),

    # API
    path('api/', include('journal.urls')),
    path('api/', include('accounts.urls')),

    # Frontend
    path('', home, name='home'),
    path('entries/', entries_page, name='entries'),
    path('entries/new/', create_entry, name='create_entry'),
    path('entries/<int:entry_id>/edit/', entry_edit, name='entry_edit'),
    path('entries/<int:entry_id>/delete/', entry_delete, name='entry_delete'),
    path('categories/', categories_page, name='categories'),
    path('categories/new/', create_category, name='create_category'),

    # Authentication pages
    path('', include('accounts.urls')),
]