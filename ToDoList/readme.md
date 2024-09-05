# To-Do List Application

This is a simple To-Do List application built using Python's Tkinter library. The application allows users to add tasks, view them in a list, and delete tasks once they are completed. Tasks are stored in a text file, ensuring they persist even after the application is closed.

## Features

-   **Add Tasks:** Enter a task in the input field and click "ADD" to add it to the list.
-   **Delete Tasks:** Select a task from the list and click the delete button to remove it.
-   **Persistent Storage:** Tasks are saved in a text file (`tasklist.txt`) and automatically loaded when the application starts.


## How to Use

1.  **Add a Task:**
    
    -   Enter your task in the input field provided.
    -   Click the "ADD" button to add the task to your list.
2.  **Delete a Task:**
    
    -   Select the task you want to delete from the list.
    -   Click the delete button (trash icon) to remove the selected task.
3.  **Persistent Task List:**
    
    -   All tasks are saved to a file named `tasklist.txt` in the specified directory.
    -   When you reopen the application, it will load tasks from this file automatically.

## File Structure

-   **todo_list.py:** The main script containing the code for the To-Do List application.
-   **tasklist.txt:** A text file where tasks are stored (automatically created if it doesn't exist).
-   **Images:** The directory where all image files used in the application are stored (e.g., `task.png`, `topbar.png`, `dock.png`, `delete.png`).

## Customization

-   **Change the File Path:**
    
    -   The file path for saving and loading tasks is hardcoded as `tasklist.txt`. You can change the path by modifying the file path in the `addTask`, `deleteTask`, and `openTaskfile` functions.
-   **GUI Customization:**
    
    -   You can modify the appearance of the GUI (e.g., colors, fonts) by adjusting the parameters in the Tkinter widgets.

## Dependencies

-   Python 3.x
-   Tkinter (comes pre-installed with Python)


## Acknowledgments

-   This project is a basic implementation to help users learn about Tkinter and file handling in Python.
-   Special thanks to any tutorial or guide that provided inspiration for this project.
