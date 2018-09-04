from django.db import models


class Province(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=6)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=6)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=6)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
