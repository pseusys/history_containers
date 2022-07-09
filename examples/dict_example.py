from history_containers import HistoryDict

leg_database = {
    'cat': 4,
    'dog': '4',
    'fish': None,
    42: 78
}

if __name__ == '__main__':
    print("Let's wrap a simple dict with HistoryDict!")
    hict = HistoryDict(leg_database)
    print(hict.print(), end='\n\n')

    print("Let's assume fins are legs - both new and old values should remain in history!")
    hict['fish'] = 6
    print(hict.print(), end='\n\n')

    print("Let's assume there are mere-cats - cats should be defined as nested dict then!")
    hict['cat'] = {
        'regular': 4,
        'mere': 2
    }
    print(hict.print(), end='\n\n')

    print("Let's take a closer look at cat dict - it's become wrapped too!")
    print(hict['cat'].print(), end='\n\n')

    print("Let's remove useless numeric value from dict - the key will be marked as DELETED in history!")
    hict.pop(42)
    print(hict.print(), end='\n\n')

    print("Let's clear wrapped dict - the history should remain!")
    hict.clear()
    print(hict.print(), end='\n\n')

    print("Let's finally clear history!")
    hict.clear_history()
    print(hict.print(), end='\n\n')
