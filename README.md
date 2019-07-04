## AirBnB Console

A project for:

<img src="https://www.holbertonschool.com/holberton-logo-twitter-card.png">

### Description "The console"

Create your data model 
Manage (create, update, destroy, etc) objects via a console / command interpreter 
Store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects anteractive modere stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine.

<p><img src="https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step0.png" alt="Console" width="629" height="335"></p>

### Usage

First `git clone` this repository `https://github.com/alexadeveloper/AirBnB_clone` 

then you can run the console in your terminal, the console can be executed in two ways, in interactive mode and non-interactive mode:

#### Interactive 

```sh
./console.py

(hbnb) help

Documented commands (type help <topic>):

========================================

EOF  all  create  destroy  help  quit  show  update

(hbnb) 
```
#### Non-interactive

```sh
echo "help" | ./console.py

(hbnb)

Documented commands (type help <topic>):

========================================

EOF  all  create  destroy  help  quit  show  update

(hbnb) 
```

## Examples

```sh
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb) quit
```
