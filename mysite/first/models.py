from django.db import models


    


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField()
    #poster = models.ImageField(upload_to='posters/')
    def __str__(self):
        return self.title

class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    room_number = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.movie} at {self.start_time}'

# class Ticket(models.Model):
#     screening = models.ForeignKey(Screening, on_delete=models.CASCADE)
#     seat_number = models.PositiveIntegerField()
#     price = models.DecimalField(max_digits=5, decimal_places=2)

#     def __str__(self):
#         return f'{self.screening} - Seat {self.seat_number}'