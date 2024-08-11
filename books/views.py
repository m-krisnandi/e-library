from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm, RegisterForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create (Tambah Buku)
@login_required
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

# Read (Daftar Buku)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

# Read (Detail Buku)
def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'book_detail.html', {'book': book})

# Update (Edit Buku)
@login_required
def book_update(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form})

# Delete (Hapus Buku)
@login_required
def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.delete()
        return redirect('book-list')
    return render(request, 'book_confirm_delete.html', {'book': book})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book-list')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {"form": form})