from service.utils.get_root_path import get_root_path

def get_tmp_data_path ():
    root_path = get_root_path()

    return f'{root_path}/tmp_data'
