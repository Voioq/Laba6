def insert_index(list, line, number):
    if len(list) < number:
        print("Operation is not possible")
    else:
        list.insert(number,line)
        print(list)
