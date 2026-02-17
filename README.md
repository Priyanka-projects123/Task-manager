# Task management and To do application

## Project Description
A to-do and task management application where users can create tasks, mark tehm complete, set priorities(High,Medium,Low), set due dates, categorize tasks,(Work,Personal,Study), and generate productivity reports showing completed vs pending tasks.
This is a simple command-line based Task Manager application developed using Python.
It allows users to manage tasks by adding, editing, deleting, and viewing tasks.
The project also provides analytics such as task completion percentage and overdue task alerts.


**This is similar to applications like Todoist, Microsoft To Do, or Jira at a basic level.**

## Features

- Create and manage tasks
- Set priority (High,Medium,Low) and due dates 
- Add, edit, and delete tasks
- Mark tasks as completed
- View tasks with filtering and sorting options
- Filter by :- Status, Category, Priority
- Sort by :- Due date, Creation date, Priority
- View analytics (completed, pending, completion percentage)
- Categorize tasks (Work,Personal,Study)
- Overdue tasks alert
- Input validation
- Unit testing using unittest
- Persistent task storage

## Tech Stack 

- Python 3.8+
- CLI-based application
- JSON for persistent storage
- unittest for unit testing
- Git for version control
- VS Code as IDE
- No external dependencies

## Usage

To start the Task Manager application, open a terminal in the project directory and run:
bash 
'''
python main.py
'''

- Example :- Main Menu

==== Task Manager Menu ====
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Edit Task
5. Delete Task
6. View Analytics
7. Exit

- Example 1 :- Add a task

- Enter your choice (1-7): 1
- Enter task title: Complete Assignment
- Enter task description: Finish BCA project report
- Enter priority (High / Medium / Low): High
- Enter category: Study
- Enter due date (YYYY-MM-DD): 2026-03-15
- Task added successfully.

- Example 2 :- View Analytics

Enter your choice (1-7): 6

--- Analytics Report ---   </br>
Total tasks: 1            </br>
Completed tasks: 1        </br>
Pending tasks: 0          </br>
Completion Percentage: 100.00%       </br>
No overdue tasks.                    

## Tests usage

bash
'''
 cd Task-manager   </br>
 python -m unittest discover -s tests -p "test_*.py" -v
 
'''


## Libraries used

- json (built-in) – for reading and writing task data in JSON format
- datetime (built-in) – for date handling and overdue task calculations

## tools used

- JSON  for persistence
- Git version Control
- CLI Interface

## Skills and concepts used 

- Python programming fundamentals
- Object-Oriented Programming (OOP) concepts :- Task, TaskManager classes
- File handling using JSON
- Date and time handling using datetime
- Command Line Interface (CLI) based application development
- Input validation and error handling
- Menu-driven program design
- Basic data structures (lists, dictionaries)
- Unit testing using unittest
- Exception handling :-
    1. try–except blocks
    2. ValueError handling
    3. Index validation
    4. Input validation
 
## Why This Project Matters (Real-World Relevance)

Task management is a common real-world problem faced by students and professionals.
This project demonstrates how a simple software solution can help users organize,
track, and analyze their daily tasks.

The application handles real-life scenarios such as:
- Managing deadlines
- Tracking completed and pending work
- Identifying overdue tasks
- Storing data persistently using files

These concepts are directly applicable to productivity tools, scheduling systems,
and basic backend applications.

## Why recruiters value this

**It shows understanding of task lifecycle management, filtering, sorting, date handling, and priority-based logic-common in many applications.**

## Ouput
## Screenshots / Demo

📄 [View Project Screenshots (PDF)](screenshots.pdf)

## Author Information

- Name: Priyanka Dharmaram Choudhary
- Batch: ITC Infotech - Python Developer
- Submission Date: 17 February 2026
- Email: choudhary200202@gmail.com
  










