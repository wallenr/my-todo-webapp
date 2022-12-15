FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ This reads a text file and returns the list of to-do items.
    Can receive a filepath but also has a default path listed.
    """
    with open(filepath, 'r') as file:
        result = file.readlines()
    return result


def write_todos(todos_list, filepath=FILEPATH):
    """ Accepts a to-do list and a filepath and writes the list to the file listed."""
    # Don't need to close the file when using the 'with' context manager
    with open(filepath, 'w') as file:
        file.writelines(todos_list)


# This conditional block will not execute when functions.py is imported
if __name__ == "__main__":
    print("Do not run this script independently")
