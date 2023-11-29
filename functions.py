FILEPATH = 'todos.txt'


def get_todos(file_path=FILEPATH):
    """
    Read a text file and return the list of 
    to-do items.
    """
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """write a to-do items list in the file. """
    with open(filepath, 'w') as file_local:
            file_local.writelines(todos_arg)


# the value of __name__ is "__main__" only when we execute the functions.py directly but if we executed other function and called it  the value will be functions
# print('I am __name__',__name__)
# it will only run if we run this file directly otherwise everything inside if condition will not run
if __name__ == "__main__":
     print("Hello")
     print(get_todos())