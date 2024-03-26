from demoApp.celery import app
from django.core.cache import cache

from .models import TxtFile, TxtFileInfo
from .services import get_number_of_lines_in_file


@app.task()
def create_txt_file_info(txt_file_id: int, owner_id: int) -> int:
    """create TxtFileInfo """
    txt_file = TxtFile.objects.select_related('owner').get(id=txt_file_id)
    txt_file_info = TxtFileInfo()
    txt_file_info.txt_file = txt_file
    txt_file_info.number_of_lines = get_number_of_lines_in_file(txt_file.file.path)
    txt_file_info.save()

    """set cache for lass created user txt file info"""
    cache.set(f'txt_file_info_latest_{owner_id}', txt_file_info, 600)
