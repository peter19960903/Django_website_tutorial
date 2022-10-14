from django.db import models
from datetime import datetime
# Create your models here.
class account_info(models.Model):
    account_name = models.CharField(max_length= 10,primary_key=True)
    account_email = models.EmailField()
    account_order = models.DateField(default = datetime.now())

    class Meta:
        db_table = 'account'