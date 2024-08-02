from django.db import models

class TaskDetails(models.Model):
    username = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    category = models.CharField(max_length=50, blank=True, null=True)  # New field

    def __str__(self):
        return self.title

















# from django.db import models

# class TaskDetail(models.Model):
#     username = models.CharField(max_length=50)
#     title = models.CharField(max_length=100)
#     description = models.TextField(blank=True, null=True)
#     due_date = models.DateField(blank=True, null=True)
#     completed = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title


# from django.db import models

# # Create your models here.
# from django.db import models

# class User(models.Model):
#     username = models.CharField(max_length=50, unique=True)
#     password = models.CharField(max_length=255)

#     def __str__(self):
#         return self.username

# class Task(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     description = models.TextField(blank=True, null=True)
#     due_date = models.DateField(blank=True, null=True)
#     completed = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title

#     @property
#     def username(self):
#         return self.user.username

