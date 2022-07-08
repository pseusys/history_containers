from history_containers.dict import DictWrapper

leg_database = {
    'cat': 4,
    'dog': '4',
    'fish': None
}

if __name__ == '__main__':
    hict = DictWrapper(leg_database)
    print(hict)
