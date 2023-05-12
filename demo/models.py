from django.db import models

class Book(models.Model):
  title = models.CharField(max_length=36)
  description = models.TextField(max_length=256, blank=True)
  price = models.DecimalField(default=0, decimal_places=2, max_digits=5)
  published = models.DateField(blank=True, null=True, default=None)
  is_published = models.BooleanField(default=False)
  cover = models.ImageField(upload_to='covers/', blank=True)

  # Convert book object to its title when called in the UI as a
  def __str__(self) -> str:
      return self.title
