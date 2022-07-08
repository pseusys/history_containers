from history_containers.dict import DictWrapper

leg_database = {
    'cat': 4,
    'dog': '4',
    'fish': None
}

if __name__ == '__main__':
    hict = DictWrapper(leg_database)
    print(f"Wrapped dict: {hict}")

    print("\nLet's count fins as legs!")
    hict['fish'] = 6
    print(f"Wrapped dict new value: {hict}")
    print(f"Wrapped dict history: {hict.history}")
