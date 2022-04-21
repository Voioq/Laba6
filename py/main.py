def insert_mid(list, line):
    i = len(list) // 2
    list.insert(i,line)
    print(list)


def insert_index(list, line, number):
    if len(list) < number:
        print("Operation is not possible")
    else:
        list.insert(number,line)
        print(list)


def delete_index(list, number):
    if len(list) <=  number:
        print("Delete operation is not possible")
    else:
        list.pop(number)
        print(list)