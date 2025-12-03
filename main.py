from todoTool import *

# this is the main method

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
                    print("which one would you like to delete")
                    delete(todoList)
                case "3":
                    # add case for modify
                    print("which one do you want to modify")
                    userIdx = int(input())
                    if userIdx < 0 or userIdx > n:
                        print("Sorry you choose a number that isn't in the list")
                    else:
                        print("What text would you like it replace it with")
                        userTxt = input()
                        todoList[userIdx] = userTxt
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
