from django.db import models


class Information(models.Model):
    u_name = models.CharField(max_length=200, blank=True, null=True)
    short_name = models.CharField(max_length=50, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.u_name


class Cost(models.Model):
    u_inf = models.ForeignKey(Information)
    subject = models.CharField(max_length=50,blank=True,null=True)
    cost = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.subject


# pass:tuhin123
# c = Cost.objects.filter(subject='CSE') i.u_inf.u_name,i.u_inf.city,i.cost
# inf = Information.objects.filter(city='dhaka')
# a = cost.objects.filter(pk__in=li)
