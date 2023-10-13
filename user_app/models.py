from django.db import models

# Create your models here.


class UserInformation(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=100)
    role = models.CharField(max_length=10)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self) -> str:
        return self.username


class PaymentGatewaySettings(models.Model):
    store_id = models.CharField(max_length=500, blank=True, null=True)
    store_pass = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = "PaymentGatewaySetting"
        verbose_name_plural = "PaymentGatewaySettings"
        db_table = "paymentgatewaysettings"
