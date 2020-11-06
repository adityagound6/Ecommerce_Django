import django.db
from django.core.validators import MinLengthValidator



class Category(django.db.models.Model):
    name = django.db.models.CharField(max_length=50)

    @staticmethod
    def get_all_category():
        return Category.objects.all()

    def __str__(self):
        return self.name