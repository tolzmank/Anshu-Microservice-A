# Author: Kent Tolzmann
# CS361 Course Project - Emphasis Selector App
# 11/4/2024
import json

from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

messages = []   # [ [{},{},{}], [{}] ]
id_counter = 0


@app.route('/')
def index():
    return render_template('index.html', messages=messages)


@app.route('/text_entry', methods=['POST'])
def text_entry():
    print('TEXT ENTRY action triggered')
    global id_counter
    segments = json.loads(request.form['all_text_segments'])  # [{},{},{}]
    export_message = {
        'segments': segments,
        'id': id_counter
    }
    print('message exported: ', [export_message])

    global messages
    messages = get_micro_response([export_message])
    id_counter += 1
    return redirect(url_for('index'))


@app.route('/edit_message/<int:message_id>', methods=['POST'])
def edit_message(message_id):
    print('EDIT Message triggered')
    updated_message = {
        'text': request.form['user_input'],
        'font_size': request.form['font_size'],
        'font_weight': request.form['font_weight'],
        'font_style': request.form['font_style'],
        'text_decoration': request.form['text_decoration'],
        'id': message_id
    }
    edit_request = [{'edit_message_id': True}, message_id, updated_message]
    global messages
    messages = get_micro_response(edit_request)
    return redirect(url_for('index'))


@app.route('/delete_message/<int:message_id>', methods=['POST'])
def delete_message(message_id):
    print(f'DELETE message action triggered: {message_id}')
    delete_request = [{'delete_message_id': True}, message_id]
    global messages
    messages = get_micro_response(delete_request)
    global id_counter
    return redirect(url_for('index'))


@app.route('/clear_messages')
def clear_messages():
    print('CLEAR action triggered')
    global messages
    global id_counter
    messages = get_micro_response([{'clear_message_log': True}])
    id_counter = 0
    return redirect(url_for("index"))


def get_micro_response(json_obj):
    import zmq
    import json
    context = zmq.Context()

    print("Connecting to Emphasis Selector microservice server...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    response = json.dumps(json_obj)
    socket.send(response.encode())

    message = socket.recv()
    print(f"Received Reply:\n {message.decode()}")
    json_obj_message = json.loads(message.decode())
    return json_obj_message


def live_text_stage():
    return


if __name__ == "__main__":
    app.run(debug=True)
