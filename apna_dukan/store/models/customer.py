import django.db
from django.core.validators import MinLengthValidator


class Customer(django.db.models.Model):
    first_name = django.db.models.CharField(max_length=10)
    last_name = django.db.models.CharField(max_length=10)
    email = django.db.models.EmailField()
    password = django.db.models.CharField(max_length=500)

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False

    def register(self):
        self.save()

    @staticmethod
    def get_customer_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
