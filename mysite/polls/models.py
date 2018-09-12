# add 20180821 m_miyamoto
import datetime
from django.db import models
# add 20180821 m_miyamoto
from django.utils import timezone
# Create your models here.
# add 20180821 m_miyamoto
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    # add 20180821 m_miyamoto
    def __str__(self):
        return self.question_text

    # add 20180821 m_miyamoto
    def was_published_recently(self):
        # add 20180823 m_miyamoto
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        # add 20180823 m_miyamoto
        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # add 20180821 m_miyamoto
    def __str__(self):
        return self.choice_text
