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

Console Basic.
```sh
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb) quit
```
Commands all, show, create, destroy, update, EOF
```sh
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel Holberton
** no instance found **
(hbnb) create BaseModel
add0ca18-e2e4-45d5-91ab-42ab7da678be
(hbnb) all BaseModel
["[BaseModel] (79a16716-15dc-4c08-b152-e6ff89d72d57) {'id': '79a16716-15dc-4c08-b152-e6ff89d72d57', 'name': 'Devon'
, 'created_at': datetime.datetime(2019, 7, 3, 21, 5, 28, 8071), 'updated_at': datetime.datetime(2019, 7, 3, 21, 5, 
28, 8086)}", "[BaseModel] (add0ca18-e2e4-45d5-91ab-42ab7da678be) {'id': 'add0ca18-e2e4-45d5-91ab-42ab7da678be', 'cr
eated_at': datetime.datetime(2019, 7, 4, 4, 59, 22, 178191), 'updated_at': datetime.datetime(2019, 7, 4, 4, 59, 22,
 178227)}", "[BaseModel] (cc464ded-3497-4294-a091-b893aaf6b114) {'my_num': 89, 'id': 'cc464ded-3497-4294-a091-b893a
af6b114', 'name': 'Holberton', 'created_at': datetime.datetime(2019, 7, 3, 21, 5, 28, 5850), 'updated_at': datetime
.datetime(2019, 7, 3, 21, 5, 28, 6399)}"]
(hbnb) show BaseModel add0ca18-e2e4-45d5-91ab-42ab7da678be
[BaseModel] (add0ca18-e2e4-45d5-91ab-42ab7da678be) {'id': 'add0ca18-e2e4-45d5-91ab-42ab7da678be', 'created_at': dat
etime.datetime(2019, 7, 4, 4, 59, 22, 178191), 'updated_at': datetime.datetime(2019, 7, 4, 4, 59, 22, 178227)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel add0ca18-e2e4-45d5-91ab-42ab7da678be
** attribute name missing **
(hbnb) update BaseModel add0ca18-e2e4-45d5-91ab-42ab7da678be first_name "Betty"
(hbnb) show BaseModel add0ca18-e2e4-45d5-91ab-42ab7da678be
[BaseModel] (add0ca18-e2e4-45d5-91ab-42ab7da678be) {'id': 'add0ca18-e2e4-45d5-91ab-42ab7da678be', 'first_name': '"B
etty"', 'created_at': datetime.datetime(2019, 7, 4, 4, 59, 22, 178191), 'updated_at': datetime.datetime(2019, 7, 4,
 5, 0, 43, 407162)}
(hbnb) create BaseModel
7d19aa43-c771-42cb-acef-2b84d3fe6e09
(hbnb) all BaseModel
["[BaseModel] (79a16716-15dc-4c08-b152-e6ff89d72d57) {'id': '79a16716-15dc-4c08-b152-e6ff89d72d57', 'name': 'Devon'
, 'created_at': datetime.datetime(2019, 7, 3, 21, 5, 28, 8071), 'updated_at': datetime.datetime(2019, 7, 3, 21, 5, 
28, 8086)}", '[BaseModel] (add0ca18-e2e4-45d5-91ab-42ab7da678be) {\'id\': \'add0ca18-e2e4-45d5-91ab-42ab7da678be\',
 \'first_name\': \'"Betty"\', \'created_at\': datetime.datetime(2019, 7, 4, 4, 59, 22, 178191), \'updated_at\': dat
etime.datetime(2019, 7, 4, 5, 0, 43, 407162)}', "[BaseModel] (7d19aa43-c771-42cb-acef-2b84d3fe6e09) {'id': '7d19aa4
3-c771-42cb-acef-2b84d3fe6e09', 'created_at': datetime.datetime(2019, 7, 4, 5, 1, 12, 956992), 'updated_at': dateti
me.datetime(2019, 7, 4, 5, 1, 12, 957032)}", "[BaseModel] (cc464ded-3497-4294-a091-b893aaf6b114) {'my_num': 89, 'id
': 'cc464ded-3497-4294-a091-b893aaf6b114', 'name': 'Holberton', 'created_at': datetime.datetime(2019, 7, 3, 21, 5, 
28, 5850), 'updated_at': datetime.datetime(2019, 7, 3, 21, 5, 28, 6399)}"]
(hbnb) EOF
```
