from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
class account_info(models.Model):
    account_name = models.CharField(max_length= 10)
    account_email = models.EmailField()
    account_order = models.DateField(default = datetime.now())
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE,primary_key=True)

    class Meta:
        db_table = 'account'