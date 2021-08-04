from os import listdir
from os.path import join, isfile

import aiofiles.os

from service.utils.get_tmp_data_path import get_tmp_data_path

def exist_in_tmp_folder(file, folder_path):
    files_in_folder_path = listdir(folder_path)

    return any((file == join(folder_path, i) for i in files_in_folder_path))

async def remove_files (files, path_to_svg):
    files['svg'] = path_to_svg

    for file in files.values():
        if isfile(file) and exist_in_tmp_folder(file, get_tmp_data_path()):
            await aiofiles.os.remove(file)
