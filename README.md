# Python-Miniprojects -  
1.Simple Clock
Clock README
This code is an example of a simple clock implemented using the Tkinter library in Python. It displays the current time in the format of hours, minutes, seconds, and AM/PM.

Prerequisites
To run this code, you need to have Python installed on your system. The code is written in Python 3.

Dependencies
The following dependencies are required for this code:

Tkinter library: It provides the graphical user interface components for Python. It is usually included with Python installation.
Tkinter.ttk module: It provides themed widgets that can be used to enhance the appearance of the GUI.
time module: It provides various functions to work with time-related tasks, such as retrieving the current time.
You can install the required dependencies using pip, the package installer for Python, by running the following command:

Copy code
pip install tk
How to Run
Open a text editor and create a new Python file.
Copy the code into the file and save it with a .py extension, for example, clock.py.
Open a terminal or command prompt and navigate to the directory where you saved the file.
Run the script by executing the following command:
lua
Copy code
python clock.py
Code Explanation
Import the necessary modules:

javascript
Copy code
from tkinter import *
from tkinter.ttk import *
from time import strftime
Create the main Tkinter window:

scss
Copy code
root = Tk()
root.title('My Clock')
Define a function time() that updates the time displayed on the clock:

Get the current time in the desired format using strftime() function:
c
Copy code
string = strftime('%H:%M:%S %p')
Configure the text of the label widget (label) to the current time:
lua
Copy code
label.config(text=string)
Schedule the time() function to be called again after 1000 milliseconds (1 second) using the after() method of the label widget:
css
Copy code
label.after(1000, time)
Create a label widget (label) to display the time:

less
Copy code
label = Label(root, font=('ds-digital', 90), background='black', foreground='cyan')
label.pack(anchor='center')
Call the time() function to start updating the time:

css
Copy code
time()
Enter the Tkinter event loop to start the GUI:

scss
Copy code
mainloop()
Customization
You can customize the appearance of the clock by modifying the following parts of the code:

root.title('My Clock'): Change the title of the main window.
font=('ds-digital', 90): Change the font and size of the displayed time.
background='black': Change the background color of the label widget.
foreground='cyan': Change the text color of the label widget.
Feel free to experiment and adjust the code to suit your preferences.

Contributions
Contributions to this code are welcome. If you find any issues or would like to add new features, please submit a pull request or open an issue on the GitHub repository.


2.QR Code Generator
This code generates a QR code using the pyqrcode library, which allows you to encode data into QR codes. It also utilizes the pyzbar library to decode QR codes, and the PIL (Python Imaging Library) library to handle images.

Installation
To run this code, you need to have the following dependencies installed:

pyqrcode
pyzbar
PIL
You can install these dependencies using pip:

bash
Copy code
pip install pyqrcode
pip install pyzbar
pip install Pillow
Usage
Import the required libraries:
python
Copy code
import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
Generate a QR code:
python
Copy code
qr = pyqrcode.create('This is an awesome tutorial!!')
qr.png('qrcode.png', scale='10')
The code above creates a QR code with the content "This is an awesome tutorial!!" and saves it as a PNG image file named qrcode.png with a scale of 10.

Decoding QR Codes
To decode a QR code, you can use the decode function from the pyzbar.pyzbar module. This function takes an image file as input and returns a list of decoded QR codes.

python
Copy code
decoded_codes = decode(Image.open('qrcode.png'))
for code in decoded_codes:
    print(code.data)
The code above opens the qrcode.png image file and decodes any QR codes present in the image. It then prints the decoded data.

Note: Make sure you have an image file with a valid QR code before attempting to decode it.

3.Calculator
This code implements a simple calculator in Python. It allows users to perform basic mathematical operations such as addition, subtraction, division, and multiplication.

Usage
Define the mathematical operations:
python
Copy code
def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b
Prompt the user to enter two numbers:
python
Copy code
a = int(input('Please enter your first number: '))
b = int(input('Please enter your second number: '))
Display the menu and prompt the user to select an operation:
python
Copy code
option = int(input('''
1. Add
2. Subtract
3. Divide
4. Multiply
5. Exit
'''))
Perform the selected operation and repeat the process until the user chooses to exit:
python
Copy code
while option != 5:
    if option == 1:
        print(plus(a, b))
        # Prompt the user for new inputs and the next operation
    elif option == 2:
        print(minus(a, b))
        # Prompt the user for new inputs and the next operation
    elif option == 3:
        print(divide(a, b))
        # Prompt the user for new inputs and the next operation
    elif option == 4:
        print(multiply(a, b))
        # Prompt the user for new inputs and the next operation
    else:
        print("Invalid option. Please try again.")
    
    a = float(input('Please enter your first number: '))
    b = float(input('Please enter your second number: '))
    option = int(input('''
1. Add
2. Subtract
3. Divide
4. Multiply
5. Exit
'''))
