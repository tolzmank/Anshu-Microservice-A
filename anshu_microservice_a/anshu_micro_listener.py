# Kent Tolzmann
# CS361 - Assignment 4 - ZeroMQ Spike - Listener
# 10/28/24

# lms_microservice_a():
# authentic_user():
#

def message_logger():

    print('message_logger MICROSERVICE is running....')
    import zmq
    import json

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")


    message_log = []    # [  [ {'segments': [{},{},{}], 'id': 0} ], [ {'segments': [{},{},{}] , 'id': 1} ]  ]
    while True:
        message = socket.recv()    # [ {'segments': [{},{},{}], 'id': 0} ]
        data = json.loads(message.decode())
        print(f"Received: {message}")

        # delete all messages
        if data[0] == {'clear_message_log': True}:
            print('CLEAR message log')
            message_log = []

        # delete target id message
        elif data[0] == {'delete_message_id': True}:
            print('DELETE TARGET message')
            message_id = data[1]
            for message in message_log:
                if message[0]['id'] == message_id:
                    message_log.remove(message)
                    break

        # edit target id message
        elif data[0] == {'edit_message_id': True}:
            print('EDIT message')
            message_id = data[1]
            updated_message = data[2]
            for i in range(len(message_log)):
                if message_log[i][0]['id'] == message_id:
                    message_log[i] = updated_message
                    break

        # create new message
        else:
            print('CREATE message')
            message_log.append(data)

        response = json.dumps(message_log)
        socket.send(response.encode())
        print(f"updated message log:\n {message_log}")


message_logger()

