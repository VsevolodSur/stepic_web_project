from django.db import models


class QuestionManager(models.Manager):

    def get_new(self):
        from datetime import datetime, timedelta, time
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        return super(QuestionManager, self).get_queryset(). \
        order_by('-added_at').filter(added_at__gte=today_start). \
        filter(added_at__lt=today_end)
    
    def get_popular(self):
        return super(QuestionManager, self).get_queryset()

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField(default=0)
    author = models.CharField(max_length=255)
    likes = models.CharField(max_length=255)
    objects = models.Manager() # The default manager
    stp_objects = QuestionManager()

    # def __unicode__(self):
    #     return self.title
    class META:
        ordering = ['-rating']

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.TextField() 
    author = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    # class META:
    #     db_table = 'answer'
    #     ordering = ['-creation_date']
