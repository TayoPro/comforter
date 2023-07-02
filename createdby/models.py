from django.db import models

# Create your models here.

class CreatedBy(models.Model):
    copyright_year = models.CharField(max_length=4, blank=True, null=True)
    crafted_by = models.CharField(max_length=250, default='')
    crafted_by_whatsapp = models.CharField(max_length=250, default='', blank=True, null=True)
    crafted_by_website = models.URLField(default='', blank=True, null=True)


    def __str__(self):
        return self.crafted_by
    

    class Meta:
        db_table = 'createdby'
        managed = True
        verbose_name = 'CreatedBy'
        verbose_name_plural = 'CreatedBys'

        