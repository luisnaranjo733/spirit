from django.db import models

class Generation(models.Model):
    graduation = models.CharField(max_length=4, primary_key=True) # 2013
    points = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return 'Class of %s' % self.graduation


class Student(models.Model):
    firstName = models.CharField(max_length=80)
    lastName = models.CharField(max_length=80)
    studentID = models.CharField(max_length=6)
    cp = models.CharField(max_length=20)
    generation = models.ForeignKey(Generation)

    def __unicode__(self):
        info = self.firstName, self.lastName, self.generation
        return '%s %s from the class of %s' % info
