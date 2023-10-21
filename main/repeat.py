import glob


def chek_repeat(text: str, data_folder: str, group_folder: str) -> bool:
    filename_list = glob.glob(f'text\{data_folder}\{group_folder}\*.txt')
    # Return True if text in filename_list else False
    for i in filename_list:
        if text in i:
            return True
    return False

