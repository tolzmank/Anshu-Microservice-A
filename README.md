# Anshu-Microservice-A
Microservice to run operations for Anshu's main program

Microservice access instructions:
Anshu’s main program needs Kent’s Microservice-A to do the following:
Receive:
● A list through ZeroMQ
● Within the list, there will be JSON objects representing the necessary data for the
operation (e.g., book details, member information) alongside variables that specify
which operation is being requested.
● Indicating the CRUD operation to be executed, as specified by the main program.

Operations:
[{'delete_book_id': True}, book_id]
- Performs operations to delete all items from the database or stored list.

[{'borrow_book': True}, book_id}]
- Perform operations to borrow the specific book.

[{'sign_up': True}, {'username': 'John_Doe, 'password': 'password123', 'email':
'user@example.com'}]
- Perform the operations to add a new member to the library system with a
username, password, and email.

[{'sign_in': True}, {'username': 'existing_user', 'password': 'password123'}]
- Perform the operations to authenticate an existing member by verifying their
username and password.

[{'key1': 'valueA', 'key2': 'valueB', ..., 'id': int}]
- Perform operation to the storage of a new message represented by the
provided JSON object.

[{'store_book': True}, {'title': 'New Book', 'author': 'Author Name', 'id': 4, 'isbn': 'ISBN004',
'available': True}]
- Perform operation to store the new book's JSON object to the local list.

[{'store_member': True}, {'username': 'john_doe', 'password': 'hashedpassword', 'email':
'member@example.com', 'id': 4}]
- Perform operation to store the new member's JSON object to the local list.

Return:
● The system can be designed to store and retrieve data objects (such as books or
members) in a list format. When a request is received via ZeroMQ, the system will return
the complete list of all stored JSON objects.


UML Sequence Diagram:




