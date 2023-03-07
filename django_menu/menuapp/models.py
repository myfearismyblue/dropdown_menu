from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)


class MenuNode(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, related_name='nodes')
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, related_name='nodes')
    value = models.CharField(max_length=100)
    named_url = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=100, blank=True)

    def get_url(self):
        if self.named_url:
            return reverse(self.named_url)
        elif self.url:
            return self.url
        return '/no_url'

    def __str__(self):
        return f'Value = {self.value}, \n parent = {self.parent}'
