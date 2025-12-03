# i would also need ot encode the save file
def save(todoList):
    print("Saving your file")
    with open('save.txt', 'w') as file_object:
        for i in todoList.values():
            print(i , file=file_object)
    print("Your todo list have been save")

def printTodo(todolist):
    counter = 0
    for i in todolist.values():
        print(f"{counter}: {i}")
        counter += 1

def linebreak():
    print("-----------------------------------------------------")

def menu():
    # modify delete to complete but need to indecate what is complete
    # maybe make one in progress and add what the percentage is done
        # maybe make this part in js on a website for better lay out
    print("1: add")
    print("2: delete")
    print("3: modify")
    print("4: printing")
    print("5: clear all")
    print("6: quit")
    

# not sure if we should change the way of delete
# it work but might take a while
def delete(todolist):
    printTodo(todolist)
    idx = input("which one would you like to delete:")
    text = todolist[int(idx)]
    del todolist[int(idx)]
    print(f"you have delete {text}")