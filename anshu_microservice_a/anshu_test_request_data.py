# Author: Kent Tolzmann
# CS361 Test program for Microservice A
# 11/18/2024


def get_micro_response(op_list):
    import zmq
    import json
    context = zmq.Context()

    print("Connecting to Microservice A server...")
    print()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5554")

    response = json.dumps(op_list)
    socket.send_string(response)
    print(f'Sent Request:\n {response}')
    print()

    message = socket.recv_string()
    op_list_message = json.loads(message)
    print(f"Received Reply:\n {message}")

    return op_list_message



if __name__ == "__main__":
    import time
    delay = 0
    # example requests
    print("Test program running...")
    print("Press enter to run test commands...")
    input()
    print('SIGN UP NEW USER')
    operation1 = ['sign_up',
                  {'username': 'John_Doe',
                   'password': 'password123',
                   'email': 'user@example.com',
                   'id': 4
                   }]
    get_micro_response(operation1)

    input("Press ENTER to continue...")
    time.sleep(delay)
    print('SIGN UP NEW USER')
    operation2 = ['sign_up',
                  {'username': 'John_Deer',
                   'password': 'password890',
                   'email': 'Deer@example.com',
                   'id': 5
                   }]
    get_micro_response(operation2)

    input("Press ENTER to continue...")
    time.sleep(delay)
    print('SIGN IN USER with wrong password')
    operation3 = ['sign_in',
                  {'username': 'John_Doe',
                   'password': 'wrong password'
                   }]
    get_micro_response(operation3)

    input("Press ENTER to continue...")
    time.sleep(delay)
    print('SIGN IN USER')
    operation4 = ['sign_in',
                  {'username': 'John_Doe',
                   'password': 'password123'
                   }]
    get_micro_response(operation4)

    input("Press ENTER to continue...")
    time.sleep(delay)
    print('DELETE USER ID')
    operation4a = ['delete_user_id', 4]
    get_micro_response(operation4a)

    input("Press ENTER to continue...")
    time.sleep(delay)
    print('STORE BOOK')
    operation5 = ['store_book',
                  {'title': 'New Book',
                   'author': 'Author Name',
                   'id': 4,
                   'isbn': 'ISBN004',
                   'available': True
                   }]
    get_micro_response(operation5)

    input("Press ENTER to continue...")
    time.sleep(delay)
    print('STORE BOOK')
    operation6 = ['store_book',
                  {'title': 'Another Book',
                   'author': 'Author B',
                   'id': 5,
                   'isbn': 'ISBN005',
                   'available': True
                   }]
    get_micro_response(operation6)

    input("Press ENTER to continue...")
    time.sleep(delay)
    print('STORE BOOK That already exists')
    operation7 = ['store_book',
                  {'title': 'New Book',
                   'author': 'Author Name',
                   'id': 4,
                   'isbn': 'ISBN004',
                   'available': True
                   }]
    get_micro_response(operation7)

    input("Press ENTER to continue...")
    time.sleep(delay)
    print('BORROW BOOK')
    operation8 = ['borrow_book', 4]
    get_micro_response(operation8)

    input("Press ENTER to continue...")
    time.sleep(delay)
    print('RETURN BOOK')
    operation9 = ['return_book', 4]
    get_micro_response(operation9)

    input("Press ENTER to continue...")
    time.sleep(delay)
    print('DELETE BOOK ID')
    operation10 = ['delete_book_id', 4]
    get_micro_response(operation10)

    input("Press ENTER to continue...")
    time.sleep(delay)
    print('DELETE ALL BOOKS')
    operation10 = ['delete_all_books', None]
    get_micro_response(operation10)

    input("Press ENTER to continue...")
    time.sleep(delay)
    print('CREATE MESSAGE')
    operation11 = [None, {'key1': 'valueA', 'key2': 'valueB', 'id': 100}]
    get_micro_response(operation11)
