FILEPATH = "todos.txt"


#  Functions
def load_todos(filepath=FILEPATH):
    """ Loads text file based on given path. """
    with open(filepath, 'r') as file_local:
        todo_list_local = file_local.readlines()
    return todo_list_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Saves to text file based on given path. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
