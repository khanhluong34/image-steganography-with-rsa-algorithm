import os

def read_key(filepath, filetype='public'):
    filename = os.path.basename(filepath).split('/')[-1]

    key_dict = {}
    with open(filepath, 'r') as file:
        for line in file:
            key_list = line.split(':')
            key_dict[key_list[0]] = key_list[1]
    
    print('Key {} read successfully!'.format(filename))
    return key_dict