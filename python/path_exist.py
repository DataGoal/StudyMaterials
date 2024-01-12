import os

def path_test(path):
    if os.path.exists(path) == True:
        print('Available')
    else:
        raise ValueError(f"Not avaialble")