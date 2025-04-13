import time
import streamlit as st
from  streamlit_option_menu import option_menu
import streamlit as st
# --- Optional: Inject dark theme CSS ---

style="background-color:#1c1c1c; color:white; padding:15px; border-radius:10px;"

import streamlit as st
from datetime import datetime

# --- Set Page Config ---


import streamlit as st
from datetime import datetime

# --- Page Config ---


# --- Credentials ---
AUTHORIZED_USERNAME = "akshad"
AUTHORIZED_PASSWORD = "1234"

# --- Store Info Function ---
def store_user_info(name, address, open_time):
    with open("user_website_info.txt", "a") as f:
        f.write(f"{name},{address},{open_time}\n")

# --- Session State Initialization ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- SIDEBAR: Profile + Login ---
with st.sidebar:
    # Profile Section
    st.markdown('<div style="background-color:#d0e8ff; padding:15px; border-radius:10px;">', unsafe_allow_html=True)
    st.image("https://avatars.githubusercontent.com/u/9919?s=200&v=4", width=100)
    st.markdown("### 👤 Akshad Sunil Yeole")
    st.markdown("**Role:** Python Learner")
    st.markdown('</div>', unsafe_allow_html=True)

    # Login Section
    st.markdown('<div style="background-color:#fce8f2; padding:15px; border-radius:10px;">', unsafe_allow_html=True)
    st.markdown("### 🔐 Login")

    # Avatar Above Contact Input
    st.image("https://avatars.githubusercontent.com/u/9919?s=200&v=4", width=150)

    contact = st.text_input("📱 Email or Mobile (required)")
    username = st.text_input("🧑 Username")
    password = st.text_input("🔒 Password", type="password")
    login_btn = st.button("Login")

    st.markdown('</div>', unsafe_allow_html=True)

# --- Login Logic ---
if login_btn:
    if username == AUTHORIZED_USERNAME and password == AUTHORIZED_PASSWORD:
        st.session_state.logged_in = True
        st.success("✅ Login successful!")
    else:
        st.error("❌ Incorrect username or password.")

# --- MAIN AREA ---
if st.session_state.logged_in:
    st.title("📘 Akshad's Python Learning Portal")

    st.subheader("🧾 Please enter your details:")
    name = st.text_input("Your Full Name")
    address = st.text_input("Your Address")
    submit_btn = st.button("Submit Info")

    if submit_btn:
        if name and address:
            open_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            store_user_info(name, address, open_time)
            st.success("✅ Your information has been recorded.")

            # --- Structured Columns for Info ---
            st.markdown("### 📄 Website Visitor Info")
            st.markdown("#### 🧍‍♂️ Opener Details")

            # Header Row
            head1, head2, head3 = st.columns([1, 2, 2])
            head1.markdown("**Name**")
            head2.markdown("**Address**")
            head3.markdown("**Time of Opening**")

            # Data Row
            col1, col2, col3 = st.columns([1, 2, 2])
            col1.markdown(f"{name}")
            col2.markdown(f"{address}")
            col3.markdown(f"{open_time}")

            # --- Website Info Section ---
            st.markdown("---")
            st.markdown("### 🌐 Website Details")

            c1, c2, c3 = st.columns(3)
            c1.metric("Website Name", "Akshad's Python Portal")
            c2.metric("Rating", "⭐️⭐️⭐️⭐️⭐️")
            c3.metric("Status", "Live")
        else:
            st.warning("⚠️ Please fill out both Name and Address.")
else:
    st.info("🔐 Please login from the sidebar to access the main page,write there the information given below .")
with st.spinner('Wait for it...'):
    time.sleep(3)










st.info("Username :- akshad")
st.info("Password :- 1234")
st.subheader("Let's Learn Python !")
st.header("What is Python ?")
st.write("""
Python is a programming language that is used for a variety of tasks, including web development, data science, and software development. It is a general-purpose language that is easy to learn and use. 

         
         """)
VIDEO_URL = "https://www.youtube.com/watch?v=xkZMUX_oQX4&list=PLP9IO4UYNF0UgPfkTBECSKIJGdc_9FYZ9.mp4"
st.video(VIDEO_URL,"subtitles.vtt")

st.header("Features of Python :-")
st.write("""
Easy to learn : Python is a beginner-friendly language with easy-to-read syntax. 

Versatile : Python can be used for a variety of tasks, including scientific computing, web development, and automation. 

Open-source : Python is an open-source community language, so many independent programmers are constantly building libraries and functionality for it. 


""")
st.header("Uses of Python:-")
st.write("""


         
Web development : Python is used to create websites and web applications. 

Data science : Python is used for data analysis, data visualization, and machine learning. 

Software development  : Python is used to develop software, including software testing, bug tracking, and build control. 

Automation : Python is used to automate tasks, such as organizing finances. 



""")
st.subheader("Now! we will take a few examples of Python:")
st.code("""
        
        print("Hello World")
        
        """)
st.write("In the above example the statement PRINT is used to display , if we write firstly PRINT and then add brackets , add double quotes and write Hello World in it , it will display Hello World in terminal box ")
st.subheader("Python Indentation")
st.write("""
Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python uses indentation to indicate a block of code.

""")
st.code("""

if 5 > 2:
  print("Five is greater than two!")
""")
st.write("Python will give you an error if you skip the indentation:")
st.subheader("Python Syntax")
st.write("""



Comments can be used to explain Python code.

Comments can be used to make the code more readable.

Comments can be used to prevent execution when testing code.
         """)
st.code("""
#This is a comment
print("Hello, World!")


""")
st.subheader("Variable")
st.write("""
Variables are containers for storing data values.

""")
st.subheader("Creating a Variable")
st.write("""
         
Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it. 
         
         """)
st.code("""

a = 4
A = "Sally"
#A will not overwrite a
""")
st.subheader("Python Data Types")
st.write("""

In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type :	str
         
Numeric Types :	int, float, complex
         
Sequence Types :	list, tuple, range
         
Mapping Type :	dict
         
Set Types :	set, frozenset
         
Boolean Type :	bool
         
Binary Types :	bytes, bytearray, memoryview
         
None Type :	NoneType
         



""")
st.code("""




x = 5
print(type(x))
        """)
st.subheader("Python Numbers")
st.write("""There are three numeric types in Python:

int
float
complex
Variables of numeric types are created when you assign a value to them
         """)
st.subheader("Example :")
st.code("""




x = 1    # int
        
y = 2.8  # float
        
z = 1j   # complex
        
        """)
st.subheader("Int")
st.write("""



Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
         """)
st.subheader("Example :")
st.write("""

x = 1
         
y = 35656222554887711
         
z = -3255522
         

print(type(x))
         
print(type(y))
         
print(type(z))
         
         """)
st.subheader("Float")
st.write("""

Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
         """)
st.subheader("Examples :")
st.code("""


x = 1.10
        
y = 1.0
        
z = -35.59
        

print(type(x))
        
print(type(y))
        
      
print(type(z))

        """)
st.subheader("Random")
st.write("""


Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:""")
st.subheader("Example :")
st.code("""


import random

print(random.randrange(1, 10))
        """)
st.subheader("Python Arithmetic Operators")
st.write("""



Arithmetic operators are used with numeric values to perform common mathematical operations:

Operator	Name	Example	Try it
         
+	Addition	x + y	 
         
-	Subtraction	x - y	
         
*	Multiplication	x * y	
         
/	Division	x / y	
         
%	Modulus	x % y	
         
**	Exponentiation	x ** y	
         
//	Floor division	x // y	
         

         """)
st.subheader("Python List")
st.write("""


Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:
         """)
st.code("""


thislist = ["apple", "banana", "cherry"]
print(thislist)
        """)
st.subheader("Python Tuples")
st.write("""

Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
         """)
st.code("""
thistuple = ("apple", "banana", "cherry")
print(thistuple)
        """)
st.subheader("Python Loops")
st.write("""

Python has two primitive loop commands:

1 . While loops
         
2 . For loops
         
3 . The while Loop
         
With the while loop we can execute a set of statements as long as a condition is true.
         """)
st.code("""
        i = 1
      
while i < 6:
        
  print(i)
        
  i += 1
        
  """)
st.subheader("The Break Statement")
st.write("""
With the break statement we can stop the loop even if the while condition is true
  """)
st.code("""
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
""")
import streamlit as st



# 1. continue
st.subheader(" Continue")
st.write("Skips the current loop iteration and continues with the next one.")
st.code("""
for i in range(5):
    if i == 2:
        continue
    print(i)
# Output: 0 1 3 4
""")

# 2. pass
st.subheader(" Pass")
st.write("Does nothing  used as a placeholder when code is required syntactically.")
st.code("""
for i in range(3):
    if i == 1:
        pass
    print(i)
# Output: 0 1 2
""")

# 3. while loop
st.subheader(" While Loop")
st.write("Repeats a block of code while a condition is true.")
st.code("""
i = 0
while i < 3:
    print(i)
    i += 1
""")

# 4. Nested loop
st.subheader(" Nested Loops")
st.write("Loops inside loops useful for multi-level iteration.")
st.code("""
for i in range(2):
    for j in range(2):
        print(i, j)
""")

# 5. Functions
st.subheader(" Functions")
st.write("Reusable blocks of code defined using `def`.")
st.code("""
def greet(name):
    print("Hello", name)

greet("Akshad")
""")

# 6. Lambda function
st.subheader(" Lambda Function")
st.write("A short anonymous function using `lambda` keyword.")
st.code("""
square = lambda x: x * x
print(square(5))
""")

# 7. List
st.subheader(" List")
st.write("Ordered, changeable collection.")
st.code("""
fruits = ["apple", "banana"]
print(fruits[0])
""")

# 8. Tuple
st.subheader(" Tuple")
st.write("Ordered, unchangeable collection.")
st.code("""
point = (10, 20)
print(point)
""")

# 9. Dictionary
st.subheader(" Dictionary")
st.write("Key-value pairs, like a real-world dictionary.")
st.code("""
student = {"name": "Akshad", "age": 20}
print(student["name"])
""")

# 10. Set
st.subheader(" Set")
st.write("Unordered collection with no duplicates.")
st.code("""
nums = {1, 2, 2, 3}
print(nums)  # {1, 2, 3}
""")

# 11. Exception handling
st.subheader(" Exception Handling")
st.write("Catches and handles errors gracefully.")
st.code("""
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
""")

# 12. List comprehension
st.subheader(" List Comprehension")
st.write("Short way to create a list.")
st.code("""
squares = [x*x for x in range(5)]
print(squares)
""")

# 13. File handling
st.subheader("File Handling")
st.write("Read/write files using `open()`.")
st.code("""
with open("demo.txt", "w") as f:
    f.write("Hello!")
""")

# 14. Modules
st.subheader("Modules")
st.write("Reusable code libraries using `import`.")
st.code("""
import math
print(math.sqrt(16))
""")

# 15. if __name__ == "__main__"
st.subheader("__name__ Guard")
st.write("Ensures code runs only when the file is executed directly.")
st.code("""
def main():
    print("This runs directly")

if __name__ == "__main__":
    main()
""")

# Define simple quiz questions for beginners



st.title("🐍 Python Basics Quiz")


score = 0

questions = [
    {
        "question": "1. Who developed Python Programming Language?",
        "options": ["Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene Stom"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "2. Which type of programming does Python support?",
        "options": ["Object-oriented", "Structured", "Functional", "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "3. What is the correct extension of a Python file?",
        "options": [".pyth", ".pt", ".py", ".pyt"],
        "answer": ".py"
    },
    {
        "question": "4. What will be the output of: `print(2 ** 3)`?",
        "options": ["6", "8", "9", "Error"],
        "answer": "8"
    },
    {
        "question": "5. Which keyword is used for function in Python?",
        "options": ["define", "func", "def", "function"],
        "answer": "def"
    },
    {
        "question": "6. How do you insert COMMENTS in Python code?",
        "options": ["// comment", "# comment", "/* comment */", "<!-- comment -->"],
        "answer": "# comment"
    },
    {
        "question": "7. Which of the following is used to take input from the user?",
        "options": ["input()", "get()", "cin", "read()"],
        "answer": "input()"
    },
    {
        "question": "8. What is the output of `type(5)`?",
        "options": ["int", "<class 'int'>", "Integer", "number"],
        "answer": "<class 'int'>"
    },
    {
        "question": "9. Which of the following is a valid variable name?",
        "options": ["2var", "var_1", "var-2", "var.3"],
        "answer": "var_1"
    },
    {
        "question": "10. What is the output of: `print('Python' * 2)`?",
        "options": ["PythonPython", "Python*2", "Error", "2Python"],
        "answer": "PythonPython"
    },
    {
        "question": "11. What is used to define a block of code in Python?",
        "options": ["Brackets", "Curly braces", "Indentation", "Quotes"],
        "answer": "Indentation"
    },
    {
        "question": "12. Which loop is used when we don't know how many times to iterate?",
        "options": ["for", "while", "do-while", "foreach"],
        "answer": "while"
    },
    {
        "question": "13. What will be the output of this code?\n\nx = 0\nwhile x < 5:\n    print(x)\n    x += 1",
        "options": ["1 2 3 4 5", "0 1 2 3 4", "0 1 2 3 4 5", "1 2 3 4"],
        "answer": "0 1 2 3 4"
    },
    {
        "question": "14. What does the `break` statement do?",
        "options": ["Skips to next iteration", "Ends the loop", "Pauses the loop", "Restarts the loop"],
        "answer": "Ends the loop"
    },
    {
        "question": "15. Which keyword is used to skip the current iteration in a loop?",
        "options": ["break", "skip", "continue", "pass"],
        "answer": "continue"
    },
]

user_answers = []
submitted = st.button("Submit Quiz")

for idx, q in enumerate(questions):
    st.subheader(q["question"])
    user_answers.append(st.radio(f"Choose an option:", q["options"], key=idx))

if submitted:
    score = sum([1 for i, q in enumerate(questions) if user_answers[i] == q["answer"]])
    st.success(f"✅ You scored {score} out of {len(questions)}!")

    # Show correct answers
    st.markdown("---")
    st.subheader("📘 Correct Answers:")
    for i, q in enumerate(questions):
        st.markdown(f"**{i+1}. {q['question']}**")
        st.markdown(f"**Correct:** {q['answer']} | **Your Answer:** {user_answers[i]}")
        if user_answers[i] != q["answer"]:
            st.error("Incorrect")
        else:
            st.success("Correct")
