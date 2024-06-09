from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField()
    date_of_applying = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "musicians"
        constraints = [models.CheckConstraint(check=models.Q(age__gte=14),
                                              name="age_gte_14")]

    @property
    def is_adult(self):
        return self.age > 20

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
