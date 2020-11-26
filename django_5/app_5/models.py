from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICE = (
    (0, "New"),
    (1, "Doing"),
    (2, "Done"),
)
# Create your models here.
class NewTask(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICE, default="0")
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
