from django.db import models

class Message(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    content = models.TextField()

    def __str__(self):
        return "{0} <{1}>: {2}".format(self.name,
                                       self.email,
                                       self.content_annotation())

    def content_annotation(self):
        """
        Short representation of a message contntet field
        """
        if self.content:
            return self.content[0:25]
        else:
            return 'No content'
