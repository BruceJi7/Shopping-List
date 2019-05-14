#! Python 3
# Shopping List.py - Stores a shopping list. Allows deletion.


import shelve

def getFromShelf(shelveName='Shopping'):
    with shelve.open('ShoppingList') as shelfFile:
        data = list(shelfFile[shelveName])
        print(f'Items: {data} on the shopping list' )
        return data


def storeOnShelf(data, shelveName='Shopping'):
    with shelve.open('ShoppingList') as shelfFile:
        shelfFile[shelveName] = data
    print('Items saved in shelf')    
    return True

def removeFrom(listObj):
    # Func closure to preload shoppingList as listObj
    def remove(deleteObj):
        if deleteObj in listObj:
            listObj.remove(deleteObj)
            print (f'{deleteObj} removed from the list')
            print(f'List now contains: {listObj}')
            return True
        else:
            print (f'Could not remove {deleteObj}: It was not in {listObj}')
            return False
    return remove

def clearList(listObj):
    # Func closure to preload shoppingList as listObj
    def clear():
        listObj.clear()
        print(f'All items removed from {listObj}')
        return True
    return clear

#def addToListClassic(listObj, addObj): # Adds an item to the list
#    if addObj not in listObj:
#        listObj.append(addObj)
#        print(f'Added {addObj} to the list')
#        print(f'List now contains: {listObj}')
#        return True
#    else:
#        print(f'{addObj} is already on the list')
#        return False
    
def addTo(listObj):
    #Func closure to preload shoppingList as listObj
    
    def add(addObj):
        if addObj not in listObj:
            listObj.append(addObj)
            print(f'Added {addObj} to the list')
            print(f'List now contains: {listObj}')
            return True
        else:
            print(f'{addObj} is already on the list')
            return False
    return add
        
       
def whatOnList(listObj):
    # Func closure to preload shoppingList as listObj
    def whatOn():
        for item in listObj:
            print(item)
    return whatOn
        

shoppingList = getFromShelf()

# Use closure to preload shoppingList variable into function. Call as: addItem('item')        
addItem = addTo(shoppingList)
removeItem = removeFrom(shoppingList)
readListToMe = whatOnList(shoppingList)
emptyList = clearList(shoppingList)




