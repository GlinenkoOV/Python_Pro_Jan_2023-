from django.db import models
class About(models.Model):
    heading = models.CharField(max_length=50, unique=True)
    desc_history = models.TextField(max_length=3000)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = "Abouts"

    def __str__(self):
        return f'{self.heading}\t{self.desc_history}'


class Service(models.Model):
    title = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField()
    desc = models.TextField(max_length=3000, verbose_name='about services')
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('position',)
        verbose_name = 'Service'
        verbose_name_plural = "Services"

    def __str__(self):
        return f'{self.title}'

class Gallery(models.Model):
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return f'{self.title}'