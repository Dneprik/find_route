from django.db import models

from cities.models import City



class Route(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Name of route')
    travel_times = models.PositiveSmallIntegerField(verbose_name='Travel time')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='route_from_city_set', verbose_name='City from')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='route_to_city_set', verbose_name='City to')
    trains = models.ManyToManyField('trains.Train', verbose_name='List of trains')

    def __str__(self):
        return f'Route  {self.name} from city {self.from_city} to city {self.to_city}'

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'
        ordering = ['travel_times']


