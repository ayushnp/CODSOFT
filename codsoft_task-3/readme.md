# Password Generator

## Description

This is a simple Password Generator application built using Python's Tkinter library. The application allows users to generate random, secure passwords by specifying the desired length. The generated password includes a combination of uppercase and lowercase letters, digits, and special characters.

## Features

-   Specify the desired length of the password.
-   Generate a secure password with a mix of characters.
-   Display the generated password on the screen.

## Requirements

-   Python 3.x
-   Tkinter (usually included with Python)
-   `random` and `string` libraries (included in the Python standard library)


## Usage

1.  **Enter the desired length** in the input box.
2.  Click the **"Generate"** button to create a random password.
3.  The generated password will be displayed on the screen.

## Code Overview

-   **Genpwd(length):** This function generates a password of the specified length using a mix of letters, digits, and punctuation.
-   **generate():** This function gets the length from the entry box, validates it, and updates the result label with the generated password.



## Error Handling

-   If the user enters a non-integer value, an error message is displayed.
-   If the length is less than or equal to zero, a warning is shown.