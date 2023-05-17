from django.db import models


class BookNumber(models.Model):
  isbn_10 = models.CharField(max_length=10, blank=True)
  isbn_13 = models.CharField(max_length=13, blank=True)

  def __str__(self) -> str:
    return f"{self.isbn_10}"


class Author(models.Model):
  name = models.CharField(max_length=30)
  surname = models.CharField(max_length=30)

  def __str__(self) -> str:
    return f"{self.name} {self.surname}"


class Character(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self) -> str:
    return self.name


class Book(models.Model):
  title =         models.CharField(max_length=36)
  description =   models.TextField(max_length=256, blank=True)
  price =         models.DecimalField(default=0, decimal_places=2, max_digits=5)
  published =     models.DateField(blank=True, null=True, default=None)
  is_published =  models.BooleanField(default=False)
  cover =         models.ImageField(upload_to='covers/', blank=True)

  characters =    models.ManyToManyField(Character, null=True, blank=True, related_name='books')
  number =        models.OneToOneField(BookNumber, null=True, blank=True, on_delete=models.CASCADE)
  author =        models.ForeignKey(Author, null=True, blank=True, default=None, 
                                    on_delete=models.CASCADE, related_name='books')
  def __str__(self) -> str:
    return self.title


# class BookAuthor(models.Model):
#   author = models.ForeignKey(Author, on_delete=models.CASCADE)
#   books = models.ManyToManyField(Book, null=True, blank=True)
  
#   class Meta: 
#     unique_together = [['author', 'book']]
