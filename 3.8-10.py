places = []

while True:
    newPlace = input('Give me the name of a new place. Type done to finish. Type pop to remove previous entry. ')
    if newPlace == 'done':
        break
    elif newPlace == 'pop':
        if len(places) == 0:
            pass
        else:
            places.pop(len(places)-1)
    else:
        places.append(newPlace)

print(places)
print(sorted(places))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
print(len(places))
