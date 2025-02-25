# cs50finalproject
TODO list program

# Daniel's ToDo List Program

## 📌 Video Demo
URL:https://youtu.be/rw9SAbu2-Jw


## 📝 Description
This console-based task management application allows users to:
- Create new tasks with auto-incremental IDs
- View/Edit task details in tabular format
- Track task completion status
- Permanently store tasks in CSV files
- Enjoy responsive UI with ANSI color coding


## 🛠️ Key Features
| Feature Category       | Supported Operations                  | Technical Implementation             |
|------------------------|-------------------------------------  |--------------------------------------|
| Task Management        | Add/remove/view/mark tasks            | CSV file persistence                 |
| User Interface         | Table display with sorting/filtering  | `tabulate` library integration       |
| Input Validation       | Numeric checks/range validation       | Custom exception handling system     |


## 🎯 Technology Stack
```mermaid
graph LR
A[Programming Language] --> B[Python 3.8+]
A --> C[CSV File Storage]
B --> D[tabulate Table Library]
B --> E[ANSI Color Encoding]
B --> F[csv.DictReader]
