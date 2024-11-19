# Author: Kent Tolzmann
# CS361 Microservice A
# 11/18/2024


def get_micro_response(json_obj):
    import zmq
    import json
    context = zmq.Context()

    print("Connecting to Microservice A server...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5554")

    response = json.dumps(json_obj)
    socket.send(response.encode())
    print(f'Sent Request:\n {response}')

    message = socket.recv()
    print(f"Received Reply:\n {message.decode()}")
    json_obj_message = json.loads(message.decode())
    return json_obj_message



if __name__ == "__main__":
    # example requests
    reply = []
    while True:
        print()
        item_type = input('user, book, or message? ')

        if item_type == 'user':
            operation = input('Enter operation request: ')
            if operation != 'delete_user_id':
                username = input('Username: ')
                password = input('Password: ')
                email = input('Email: ')
                user_id = int(input('ID: '))
                item = {
                    'username': username,
                    'password': password,
                    'email': email,
                    'id': user_id
                }
                reply = [{operation: True}, item]
            else:
                user_id = int(input('user ID: '))
                reply = [{operation: True}, user_id]

        elif item_type == 'book':
            operation = input('Enter operation request: ')
            if operation == 'store_book':
                title = input('Title: ')
                author = input('Author: ')
                book_id = int(input('ID: '))
                isbn = input('ISBN: ')
                available = True
                item = {
                    'title': title,
                    'author': author,
                    'id': book_id,
                    'isbn': isbn,
                    'available': available
                }
                reply = [{operation: True}, item]

            else:
                book_id = int(input('Book ID: '))
                reply = [{operation: True}, book_id]


        else:
            print('New message input: \n')
            key1 = input('Key 1: ')
            valueA = input('Value A: ')
            key2 = input('Key 2: ')
            valueB = input('Value B: ')
            message_id = int(input('ID: '))
            item = {
                key1: valueA,
                key2: valueB,
                'id': message_id
            }
            reply = [item]


        get_micro_response(reply)




