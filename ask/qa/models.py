from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):

    def get_new(self):
        from datetime import datetime, timedelta, time
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        # return super(QuestionManager, self).get_queryset(). \
        # order_by('-added_at').filter(added_at__gte=today_start). \
        # filter(added_at__lt=today_end)
        return self.order_by('-added_at')

    def get_popular(self):
        # return super(QuestionManager, self).get_queryset()
        return self.order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(null=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="%(app_label)s_%(class)s_related")
    objects = models.Manager() # The default manager
    stp_objects = QuestionManager()

    # def __unicode__(self):
    #     return self.title
    class META:
        ordering = ['-rating']

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # class META:
    #     db_table = 'answer'
    #     ordering = ['-creation_date']
