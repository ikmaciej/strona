from django.db import models

IDEA_STATUS = (
    ('pending', 'Waiting for review'),
    ('accepted', 'Accepted'),
    ('done', 'Done')
)

class Idea(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    youtube_url = models.URLField(null=True, blank=True)
    status = models.CharField(choices=IDEA_STATUS, default='pending', max_length=30)

    def __str__(self):
        return  self.title


class Vote(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    reason = models.TextField()

