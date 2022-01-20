import os

def make_path(*args):
    """function to make an absolute path

    Returns:
        data_dir(str):a path with the input arguments 
    """    """"""
    current_dir=os.getcwd()
    new_dir= os.path.join(current_dir,os.pardir,*args)
    return new_dir

def make_item_list(*args):
    """return the items in a specified path in this

    Returns:
        item(list): a list with all absolute file path in the specified folder
    """
    data_dir = make_path(*args)
    items_list=[os.path.join(data_dir,item) for item in os.listdir(data_dir) if os.path.isfile(item)]
    return items_list


def make_directories_list(*args):
    """return the directories in a specified path

    Returns:
        item(list): a list with all absolute directorie paths in the specified folder
    """
    data_dir = make_path(*args)
    dir_list = [os.path.join(data_dir, item)
                  for item in os.listdir(data_dir) if os.path.isdir(item)]
    return dir_list
