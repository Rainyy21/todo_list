
# might need to move these somewhere else
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

def todo():
    # might use a different storage
    todoList = {}
    # keep track of length 
    n = len(todoList)
    
    print("welcome, I'm here to keep track of your todo list")
    print("what would you like to do")

    while True:
        menu()
        try:
            user = input()
            
            match user:
                case "1":
                    # add a case for adding
                    print("what would you like to add")
                    userTxt = input()
                    todoList[n] = userTxt
                    n += 1
                    linebreak()
                    continue
                case "2":
                    # add case for deleting
                    print("not added")
                case "3":
                    # add case for modify
                    print("which one do you want to modify")
                    userIdx = int(input())
                    if userIdx < 0 or userIdx > n:
                        print("Sorry you choose a number that isn't in the list")
                        continue
                    
                case "4":
                    # add case for printing
                    print("Your current todo list")
                    printTodo(todoList)
                    linebreak()
                    continue
                case "5":
                    # add case for clearing
                    todoList.clear()
                    n = 0 
                    continue
                case "6":
                    # add case for quiting
                    save(todoList)
                    quit()

                # if user enter int value that isn't listed
                case _ :
                    print("there is no int value for that")
                    continue
        # what if user enter a string 
        except ValueError:
            print("please enter a number value")
            





# this is what trigger it to start
if __name__ =="__main__":
    # add the main method name
    todo()