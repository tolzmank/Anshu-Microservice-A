# Kent Tolzmann
# CS361 - Microservice A
# 12/02/24


def lms_microservice():
    print('LMS MICROSERVICE is running....')
    import zmq
    import json
    try:
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://*:5554")

        users = []
        books = []
        messages = []

        while True:
            message = socket.recv_string()
            data = json.loads(message)
            print(f"Received: {message}")
            operation = data[0]
            user_operations = ['sign_up',
                               'sign_in',
                               'delete_user_id'
                               ]
            book_operations = ['store_book',
                               'borrow_book',
                               'delete_book_id',
                               'return_book',
                               'delete_all_books'
                               ]

            # User Authentication
            if operation in user_operations:
                user_data = data[1]
                reply = user_authentication(operation, user_data, users)

            # Books CRUD Operations
            elif operation in book_operations:
                book_data = data[1]
                reply = book_ops(operation, book_data, books)

            # Message storing
            else:
                new_message = data[1]
                messages.append(new_message)
                reply = messages

            response = json.dumps(reply)
            socket.send_string(response)
            print(f'Response: {response}')
            print(f"users:\n {users}")
            print(f"books:\n {books}")
            print(f"messages:\n {messages}")
            print()

    except zmq.ZMQError as e:
        print(f"ZMQ Error: {e}")
    except json.JSONDecodeError:
        print("Error decoding JSON response")
    except Exception as e:
        print(f"Unexpected Error: {e}")
    return None


def user_authentication(operation, user_data, users):
    # Add user
    if operation == 'sign_up':
        print(f'USER SIGN UP')
        new_user = user_data
        for user in users:
            if new_user['username'] == user['username']:
                return [{'sign_up': 'username already exists'}]
        else:
            users.append(new_user)
            print(f'user login successful: {new_user['username']}')
            return users

    # Authenticate user
    elif operation == 'sign_in':
        print('USER SIGN IN')
        auth_user = user_data
        for user in users:
            if auth_user['username'] == user['username'] and auth_user['password'] == user['password']:
                return [{'sign_in': True}]
        else:
            return [{'sign_in': False}]

    # Delete user
    elif operation == 'delete_user_id':
        print('DELETE USER')
        user_id = user_data
        for user in users:
            if user['id'] == user_id:
                users.remove(user)
                return users
        return [{'delete_user_id': 'user id not found'}]


def book_ops(operation, book_data, books):
    # Add book
    if operation == 'store_book':
        print('STORE BOOK')
        new_book = book_data
        for book in books:
            if new_book['title'] == book['title']:
                return [{'store_book': 'book name already exists'}]
        else:
            books.append(new_book)
            return books

    # Borrow book
    elif operation == 'borrow_book':
        print('BORROW BOOK')
        book_id = book_data
        for book in books:
            if book['id'] == book_id:
                book['available'] = False
                return books
        return [{'borrow_book': 'book id not found'}]

    # Delete book
    elif operation == 'delete_book_id':
        print('DELETE BOOK ID')
        book_id = book_data
        for book in books:
            if book['id'] == book_id:
                books.remove(book)
                return books
        return [{'delete_book_id': 'book id not found'}]

    elif operation == 'delete_all_books':
        print('DELETE ALL BOOKS')
        books.clear()
        return books

    elif operation == 'return_book':
        book_id = book_data
        for book in books:
            if book['id'] == book_id:
                book['available'] = True
                return books
        return [{'borrow_book': 'book id not found'}]


if __name__ == "__main__":
    lms_microservice()
