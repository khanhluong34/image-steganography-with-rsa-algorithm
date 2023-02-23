import os

def read_key(filetype='public'):
    filename = '{}.key'.format(filetype)
    filepath = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        filename
    )

    key_dict = {}
    with open(filepath, 'r') as file:
        for line in file:
            key_list = line.split(':')
            key_dict[key_list[0]] = key_list[1]
    
    print('Key {} read successfully!'.format(filename))
    return key_dict