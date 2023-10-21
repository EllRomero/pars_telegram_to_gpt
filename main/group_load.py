def load_txt():
    with open('group/group_name.txt', 'r') as file:
        text = file.read().replace(' ', '')  # Delete space
        word = text.split(sep=',')
        return word


if __name__ == '__main__':
    load_txt()
