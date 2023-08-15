from django.db import models
import time, datetime
from datetime import timedelta


class BaseMonitoringObject(models.Model):
    id_number = models.IntegerField(unique=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    create_date = models.DateField(editable=False, )
    update_date = models.DateField(editable=False, blank=True, null=True)
    start_date_use = models.DateField(blank=True, null=True)
    #days_warranty = models.DateField(blank=True, null=True, verbose_name = "Ост. дней гарантии")

    def save(self, *args, **kwargs) -> None:
        if not self.id_number:
            self.id_number = time.time()
            self.create_date = datetime.datetime.today()
        else:
            self.update_date = datetime.datetime.today()
        super(BaseMonitoringObject, self).save(*args, **kwargs)

    def calculation_days_warranty(self):
        if self.start_date_use:
            days_warranty = self.start_date_use + timedelta(days=365)
            return days_warranty

    def __str__(self):
        return self.name
    
    days_warranty = property(calculation_days_warranty)
    



class VibratingTamper(BaseMonitoringObject):
    pass