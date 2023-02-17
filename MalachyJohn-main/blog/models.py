from django.db import models
from django.urls import reverse
from django.db.models import Model


class Post(models.Model):
    title = models.CharField(max_length=200)
    author =models.ForeignKey("auth.User", on_delete=models.CASCADE,)
    body=models.TextField()


    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

# Create your models here.
class Film(models.Model):
    title=models.CharField(max_length=200)
    duration = models.DurationField()
    poster = models.ImageField()
    trailer = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.title}: {self.duration}"


class Screen(models.Model):
     capacity = models.IntegerField()
     price_per_seat = models.DecimalField(max_digits=5,decimal_places=2)

     def __str__(self):
        return f"Screen {self.id}"


class Screening(models.Model):
    start_time = models.DateTimeField()
    film_id = models.ForeignKey(Film,on_delete=models.CASCADE)
    screen_id = models.ForeignKey(Screen,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.film_id.title} {self.screen_id}"

class Booking(models.Model):
    #booking_id = models.AutoField(primary_key=True)
    number_of_seats = models.IntegerField()
    cost = models.DecimalField(max_digits=5,decimal_places=2)
    customer_email = models.EmailField(max_length=254)
    screening_id = models.ForeignKey(Screening,on_delete=models.CASCADE)
    film_id=models.ForeignKey(Film,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer_email}: {self.film_id.title} {self.screening_id.screen_id}"

    def get_absolute_url(self):
        #check this part again
       return reverse("post_detail",kwargs={"pk":self.pk})

   

