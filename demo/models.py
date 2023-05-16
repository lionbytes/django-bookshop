from django.db import models
class BookNumber(models.Model):
  isbn_10 = models.CharField(max_length=10, blank=True)
  isbn_13 = models.CharField(max_length=13, blank=True)

  def __str__(self) -> str:
    return f"{self.isbn_10} – {self.book.title}"
  

class Book(models.Model):
  title =         models.CharField(max_length=36)
  description =   models.TextField(max_length=256, blank=True)
  price =         models.DecimalField(default=0, decimal_places=2, max_digits=5)
  published =     models.DateField(blank=True, null=True, default=None)
  is_published =  models.BooleanField(default=False)
  cover =         models.ImageField(upload_to='covers/', blank=True)

  number =        models.OneToOneField(BookNumber, null=True, blank=True, on_delete=models.CASCADE)

  # Convert book object to its title when called in the UI as a
  def __str__(self) -> str:
      return self.title

class Character(models.Model):
  name = models.CharField(max_length=30)
  book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='characters')

  def __str__(self) -> str:
    return self.name

class Author(models.Model):
  name = models.CharField(max_length=30)
  surname = models.CharField(max_length=30)
  books = models.ManyToManyField(Book, related_name='authors')

  def __str__(self) -> str:
    return f"{self.name} {self.surname}"
