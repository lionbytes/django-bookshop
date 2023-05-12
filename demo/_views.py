from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book

def first(request):
  return HttpResponse('<h1>Hello, world!</h1>')

class Second(View):
  allbooks = Book.objects.all() # Gets all records
  freebooks = Book.objects.filter(price=0) # Gets all records that meet filter condition
  latest_book = Book.objects.get(id=len(allbooks)) # Gets one record 

  output = f"<p>We have <b>{len(allbooks)}</b> books in our database:</p><ul>"

  for book in allbooks:
    output += f"<li><b>{book.title}</b></li>"

  output += f"</ul><p>We have <b>{len(freebooks)}</b> free book(s):<br><b>{freebooks[0].title}</b>.</p>"
  output += f"<p>Our latest books is: <br><b>{latest_book.title}</b></p>"

  
  def get(self, request):
    return HttpResponse(self.output)

def third(request):
  books = Book.objects.all()
  return render(request, 'third.html', {'books': books})
  