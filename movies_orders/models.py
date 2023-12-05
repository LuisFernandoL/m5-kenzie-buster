from django.db import models


# Create your models here.
class MovieOrder(models.Model):
    purchased_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="pivot_movie_order"
    )
    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        related_name="pivot_movie_order",
    )
