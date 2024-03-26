from django.db import models
from users.models import CustomUser


class TxtFile(models.Model):
    """model for file .txt"""
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to='user_txt_files/')
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self, using=None, keep_parents=False):
        self.file.storage.delete(self.file.path)
        super().delete()

    # def __str__(self):
    #     return f'{self.owner} + {self.file.name}'


class TxtFileInfo(models.Model):
    """model for .txt file information"""
    txt_file = models.ForeignKey(TxtFile, on_delete=models.CASCADE)
    number_of_lines = models.IntegerField()
