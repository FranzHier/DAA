# Latihan Linear Search

def linSearch(list, item):
    for i in range(len(list)):
        if list[i] == item:
            return True
    return False

list = ['y', 'u', 'i', 'w', 'o', 'a', 'q', 'u', 'j', 'p']
print(linSearch(list, 'a'))
