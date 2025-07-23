import streamlit as st
import random

def quiz_fun():
    questions = [
        {
            "type": "mcq",
            "question": "What is the output of print(2 ** 3)?",
            "options": ["6", "8", "9", "Error"],
            "answer": "8",
            "example": "Example:\n```python\nprint(2 ** 3)  # Output: 8\n```"
        },
        {
            "type": "mcq",
            "question": "Which keyword is used to define a function in Python?",
            "options": ["func", "define", "def", "function"],
            "answer": "def",
            "example": "Example:\n```python\ndef my_function():\n    print(\"Hello\")\n```"
        },
        {
            "type": "mcq",
            "question": "What data type is the object below?\n\nlist_example = [1, 2, 3]",
            "options": ["List", "Tuple", "Dictionary", "Set"],
            "answer": "List",
            "example": "Example:\n```python\nlist_example = [1, 2, 3]\nprint(type(list_example))  # Output: <class 'list'>\n```"
        },
        {
    "type": "mcq",
    "question": "Which function is used to read a CSV file into a Pandas DataFrame?",
    "options": ["read_csv()", "load_csv()", "import_csv()", "csv_read()"],
    "answer": "read_csv()",
    "example": "import pandas as pd\n\n# Read a CSV file\n# Assume 'data.csv' has columns: Name, Age\ndf = pd.read_csv('data.csv')\nprint(df.head())"
  },
  {
    "type": "mcq",
    "question": "What does the head() function return?",
    "options": ["The first 5 rows", "The last 5 rows", "Column names", "Shape of DataFrame"],
    "answer": "The first 5 rows",
    "example": "import pandas as pd\n\ndf = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank']})\nprint(df.head())  # Displays first 5 rows"
  },
  {
    "type": "mcq",
    "question": "Which method is used to get basic statistical details of a DataFrame?",
    "options": ["describe()", "info()", "summary()", "stats()"],
    "answer": "describe()",
    "example": "import pandas as pd\n\ndf = pd.DataFrame({'age': [25, 30, 22, 40, 28]})\nprint(df.describe())"
  },
  {
    "type": "mcq",
    "question": "What is the output of df.shape?",
    "options": ["Number of rows and columns", "Only rows", "Only columns", "Data types"],
    "answer": "Number of rows and columns",
    "example": "import pandas as pd\n\ndf = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})\nprint(df.shape)  # (2, 2)"
  },
  {
    "type": "text",
    "question": "Which method is used to display the last few rows of a DataFrame?",
    "answer": "tail",
    "example": "import pandas as pd\n\ndf = pd.DataFrame({'x': range(10)})\nprint(df.tail())  # Last 5 rows"
  },
  {
    "type": "text",
    "question": "How do you select a column named 'Age' from a DataFrame df?",
    "answer": "df['Age']",
    "example": "import pandas as pd\n\ndf = pd.DataFrame({'Age': [21, 25, 30]})\nprint(df['Age'])"
  },
  {
    "type": "text",
    "question": "What method is used to drop missing values from a DataFrame?",
    "answer": "dropna",
    "example": "import pandas as pd\n\ndf = pd.DataFrame({'A': [1, None, 3], 'B': [4, 5, None]})\nprint(df.dropna())"
  },
  {
    "type": "text",
    "question": "Which function provides data types of each column in a DataFrame?",
    "answer": "dtypes",
    "example": "import pandas as pd\n\ndf = pd.DataFrame({'name': ['Alice'], 'age': [30]})\nprint(df.dtypes)"
  },
    {
    "type": "mcq",
    "question": "Which of the following is used to handle exceptions in Python?",
    "options": ["try-except", "do-catch", "catch-throw", "handle-except"],
    "answer": "try-except",
    "example": "try:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print(\"Cannot divide by zero\")"
  },
  {
    "type": "mcq",
    "question": "What is the output of len('Python')?",
    "options": ["5", "6", "7", "Error"],
    "answer": "6",
    "example": "print(len('Python'))  # Output: 6"
  },
  {
    "type": "mcq",
    "question": "Which operator is used for floor division in Python?",
    "options": ["/", "//", "%", "**"],
    "answer": "//",
    "example": "print(7 // 2)  # Output: 3"
  },
  {
    "type": "mcq",
    "question": "What will be the output of: print(type([]))?",
    "options": ["<class 'list'>", "<class 'dict'>", "<class 'tuple'>", "<class 'set'>"],
    "answer": "<class 'list'>",
    "example": "print(type([]))  # Output: <class 'list'>"
  },
  {
    "type": "mcq",
    "question": "Which method can be used to remove items from a list?",
    "options": ["delete()", "remove()", "discard()", "erase()"],
    "answer": "remove()",
    "example": "my_list = [1, 2, 3]\nmy_list.remove(2)\nprint(my_list)  # Output: [1, 3]"
  },
  {
    "type": "mcq",
    "question": "What is the correct file extension for Python files?",
    "options": [".pt", ".pyt", ".py", ".p"],
    "answer": ".py",
    "example": "# Python files end with .py\n# Example: hello.py"
  },
  {
    "type": "mcq",
    "question": "Which statement is used to stop a loop in Python?",
    "options": ["stop", "exit", "break", "end"],
    "answer": "break",
    "example": "for i in range(5):\n    if i == 3:\n        break\n    print(i)"
  },
  {
    "type": "text",
    "question": "Which Python function is used to open a file?",
    "answer": "open",
    "example": "file = open('example.txt', 'r')"
  },
  {
    "type": "text",
    "question": "What is the default mode in which the open() function opens a file?",
    "answer": "r",
    "example": "file = open('example.txt')  # opens in read mode by default"
  },
   {
    "type": "text",
    "question": "Which keyword is used in Python to ensure a file is properly closed after its suite finishes, even if an exception is raised?",
    "answer": "with",
    "example": "with open('file.txt', 'r') as f:\n    data = f.read()"
  },
  {
    "type": "text",
    "question": "Which method is used to write a string to a file in Python?",
    "answer": "write",
    "example": "with open('file.txt', 'w') as f:\n    f.write('Hello, World!')"
  },
  {
    "type": "mcq",
    "question": "What is the output of: bool(0)?",
    "options": ["True", "False", "None", "0"],
    "answer": "False",
    "example": "print(bool(0))  # Output: False"
  },
  {
    "type": "mcq",
    "question": "Which keyword is used to create a class in Python?",
    "options": ["function", "class", "define", "object"],
    "answer": "class",
    "example": "class MyClass:\n    def __init__(self):\n        self.name = 'Example'"
  },
  {
    "type": "mcq",
    "question": "What is the result of: 'Hello' + 'World'?",
    "options": ["Hello World", "HelloWorld", "Hello+World", "Error"],
    "answer": "HelloWorld",
    "example": "print('Hello' + 'World')  # Output: HelloWorld"
  },
  {
    "type": "mcq",
    "question": "Which built-in function returns the number of items in an object?",
    "options": ["count()", "len()", "size()", "length()"],
    "answer": "len()",
    "example": "items = [1, 2, 3]\nprint(len(items))  # Output: 3"
  },
  {
    "type": "text",
    "question": "What is a Python decorator used for?",
    "answer": "modifying function behavior",
    "example": "def decorator(func):\n    def wrapper():\n        print('Before function')\n        func()\n        print('After function')\n    return wrapper\n\n@decorator\ndef say_hello():\n    print('Hello')\n\nsay_hello()"
  },
  {
    "type": "text",
    "question": "Which Python module is commonly used for asynchronous programming?",
    "answer": "asyncio",
    "example": "import asyncio\n\nasync def main():\n    print('Hello')\n    await asyncio.sleep(1)\n    print('World')\n\nasyncio.run(main())"
  },
  {
    "type": "text",
    "question": "What built-in function returns an iterator that aggregates elements from multiple iterables?",
    "answer": "zip",
    "example": "names = ['Alice', 'Bob']\nages = [25, 30]\nfor name, age in zip(names, ages):\n    print(name, age)"
  },
  {
    "type": "text",
    "question": "Which keyword is used to define a generator function?",
    "answer": "yield",
    "example": "def count_up_to(n):\n    i = 1\n    while i <= n:\n        yield i\n        i += 1\n\nfor num in count_up_to(3):\n    print(num)"
  },
  {
    "type": "text",
    "question": "What is the purpose of the __init__.py file in a Python package?",
    "answer": "marks directory as a package",
    "example": "# __init__.py can be empty or include initialization code for a package.\n# Example directory structure:\n# my_package/\n#     __init__.py\n#     module1.py"
  },
   {
    "type": "text",
    "question": "What does the 'with' statement manage in Python?",
    "answer": "context",
    "example": "with open('example.txt', 'r') as file:\n    content = file.read()\n# file is automatically closed after block"
  },
  {
    "type": "text",
    "question": "Which built-in function is used to get the memory address of an object?",
    "answer": "id",
    "example": "x = 10\nprint(id(x))  # prints memory address"
  },
  {
    "type": "text",
    "question": "What exception is raised when a variable is not found?",
    "answer": "NameError",
    "example": "try:\n    print(my_var)\nexcept NameError:\n    print(\"Variable not found\")"
  },
  {
    "type": "mcq",
    "question": "Which mode opens a file for writing and truncates the file if it already exists?",
    "options": ["r", "w", "a", "x"],
    "answer": "w",
    "example": "with open('example.txt', 'w') as file:\n    file.write('New content')  # replaces existing content"
  },
  {
    "type": "mcq",
    "question": "Which function is used to read a file line by line in Python?",
    "options": ["read()", "readline()", "readlines()", "nextline()"],
    "answer": "readline()",
    "example": "with open('example.txt', 'r') as file:\n    line = file.readline()\n    print(line)"
  },
  {
    "type": "mcq",
    "question": "What does the 'a' mode do when opening a file?",
    "options": ["Reads from the file", "Appends to the file", "Deletes the file", "Creates a directory"],
    "answer": "Appends to the file",
    "example": "with open('log.txt', 'a') as file:\n    file.write('New log entry\n')"
  },
  {
    "type": "text",
    "question": "Which method is used to convert a string to lowercase in Python?",
    "answer": "lower",
    "example": "text = 'HELLO'\nprint(text.lower())  # Output: 'hello'"
  },
  {
    "type": "text",
    "question": "What does the split() method do in Python strings?",
    "answer": "splits the string into a list",
    "example": "text = 'apple,banana,cherry'\nprint(text.split(','))  # ['apple', 'banana', 'cherry']"
  },
  {
    "type": "text",
    "question": "Which method is used to replace parts of a string in Python?",
    "answer": "replace",
    "example": "text = 'I like Java'\nprint(text.replace('Java', 'Python'))  # 'I like Python'"
  },
  {
    "type": "text",
    "question": "How do you get the length of a string in Python?",
    "answer": "len",
    "example": "text = 'Python'\nprint(len(text))  # Output: 6"
  },
    {
    "type": "mcq",
    "question": "What is the output of 'hello'.upper()?",
    "options": ["HELLO", "hello", "Hello", "Error"],
    "answer": "HELLO",
    "example": "print('hello'.upper())  # Output: 'HELLO'"
  },
  {
    "type": "mcq",
    "question": "Which method removes whitespace from the beginning and end of a string?",
    "options": ["strip()", "trim()", "remove()", "cut()"],
    "answer": "strip()",
    "example": "text = '  hello  '\nprint(text.strip())  # Output: 'hello'"
  },
  {
    "type": "mcq",
    "question": "What is the output of 'Python'[0]?",
    "options": ["P", "y", "n", "0"],
    "answer": "P",
    "example": "print('Python'[0])  # Output: 'P'"
  },
  {
    "type": "mcq",
    "question": "Which of the following is used to concatenate strings in Python?",
    "options": ["Plus +", "&", "Star *", "%"],
    "answer": "Plus +",
    "example": "print('Hello' + 'World')  # Output: 'HelloWorld'"
  },
  {
    "type": "mcq",
    "question": "Which of the following is a valid variable name in Python?",
    "options": ["2name", "_name", "@name", "name-1"],
    "answer": "_name",
    "example": "_name = 'Python'\nprint(_name)"
  },
  {
    "type": "mcq",
    "question": "Which of the following is a mutable data type in Python?",
    "options": ["tuple", "list", "str", "int"],
    "answer": "list",
    "example": "my_list = [1, 2, 3]\nmy_list.append(4)\nprint(my_list)  # Output: [1, 2, 3, 4]"
  },
  {
    "type": "mcq",
    "question": "What symbol is used for single-line comments in Python?",
    "options": ["//", "<!-- -->", "#", "/* */"],
    "answer": "#",
    "example": "# This is a single-line comment"
  },
  {
    "type": "mcq",
    "question": "Which method is used to add an element to a set?",
    "options": ["append()", "add()", "insert()", "extend()"],
    "answer": "add()",
    "example": "my_set = {1, 2}\nmy_set.add(3)\nprint(my_set)  # Output: {1, 2, 3}"
  },
  {
    "type": "mcq",
    "question": "Which module is used to interact with the file system and directories in Python?",
    "options": ["sys", "os", "shutil", "pathlib"],
    "answer": "os",
    "example": "import os\nprint(os.getcwd())  # Prints current working directory"
  },
  {
    "type": "mcq",
    "question": "Which of the following is an immutable data type in Python?",
    "options": ["list", "tuple", "set", "dictionary"],
    "answer": "tuple",
    "example": "my_tuple = (1, 2, 3)\n# my_tuple[0] = 10  # Raises TypeError"
  },
  {
    "type": "mcq",
    "question": "Which of these is used to define a function in Python?",
    "options": ["function", "define", "def", "fun"],
    "answer": "def",
    "example": "def greet():\n    print('Hello')\ngreet()"
  },
    {
    "type": "mcq",
    "question": "What does the keys() method return when used on a dictionary?",
    "options": ["A list of values", "A list of keys", "A list of items", "None"],
    "answer": "A list of keys",
    "example": "my_dict = {'a': 1, 'b': 2}\nprint(my_dict.keys())  # Output: dict_keys(['a', 'b'])"
  },
  {
    "type": "mcq",
    "question": "Which statement is used to handle exceptions in Python?",
    "options": ["try-catch", "try-except", "catch-throw", "do-except"],
    "answer": "try-except",
    "example": "try:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero')"
  },
  {
    "type": "mcq",
    "question": "Which method is used to remove an item from a list by index?",
    "options": ["remove()", "del", "pop()", "discard()"],
    "answer": "pop()",
    "example": "my_list = [1, 2, 3]\nmy_list.pop(1)\nprint(my_list)  # Output: [1, 3]"
  },
  {
    "type": "text",
    "question": "How do you create an empty list in Python?",
    "answer": "[] or list()",
    "example": "empty1 = []\nempty2 = list()"
  },
  {
    "type": "text",
    "question": "How can you access the value associated with a key in a dictionary?",
    "answer": "Using dict[key] syntax",
    "example": "my_dict = {'name': 'Alice'}\nprint(my_dict['name'])  # Output: Alice"
  },
  {
    "type": "text",
    "question": "Which function is used to import a module in Python?",
    "answer": "import",
    "example": "import math\nprint(math.sqrt(16))  # Output: 4.0"
  },
  {
    "type": "text",
    "question": "What function is used to read the entire contents of a file as a string?",
    "answer": "read()",
    "example": "with open('file.txt', 'r') as f:\n    data = f.read()"
  },
  {
    "type": "text",
    "question": "Which block of code is used for cleanup actions regardless of whether an exception occurred?",
    "answer": "finally",
    "example": "try:\n    print(1 / 0)\nexcept ZeroDivisionError:\n    print('Error')\nfinally:\n    print('Cleanup')"
  },
  {
    "type": "text",
    "question": "Which keyword is used to define a variable in Python?",
    "answer": "Python does not require a keyword; assignment is done with =",
    "example": "x = 10\nprint(x)"
  },
  {
    "type": "text",
    "question": "What data type is returned by the input() function?",
    "answer": "str",
    "example": "name = input('Enter your name: ')\nprint(type(name))  # Output: <class 'str'>"
  },
  {
    "type": "text",
    "question": "How do you create an empty set in Python?",
    "answer": "set()",
    "example": "empty_set = set()\nprint(empty_set)  # Output: set()"
  },
  {
    "type": "text",
    "question": "Which function is used to change the current working directory?",
    "answer": "os.chdir",
    "example": "import os\nos.chdir('/path/to/directory')"
  },
  {
    "type": "text",
    "question": "What will be the result of type(5.0)?",
    "answer": "float",
    "example": "print(type(5.0))  # Output: <class 'float'>"
  }
    ]

    if "question_index" not in st.session_state:
        st.session_state.question_index = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "show_feedback" not in st.session_state:
        st.session_state.show_feedback = False
    if "user_answer" not in st.session_state:
        st.session_state.user_answer = ""

    q_index = st.session_state.question_index

    if "shuffled_questions" not in st.session_state:
        st.session_state.shuffled_questions = random.sample(questions, len(questions))
        st.session_state.question_index = 0

    if st.session_state.question_index < len(st.session_state.shuffled_questions):
        q = st.session_state.shuffled_questions[st.session_state.question_index]
        st.markdown(f"#### Question {st.session_state.question_index + 1} of {len(questions)}")
        st.write(q["question"])
        user_input = ""
        if q["type"] == "mcq":
            user_input = st.radio("Choose your answer:", q["options"], key=f"mcq_{q_index}")
        elif q["type"] == "text":
            user_input = st.text_input("Enter your answer:", key=f"text_{q_index}")

        if not st.session_state.show_feedback:
            if st.button("Submit Answer", key=f"submit_{q_index}"):
                st.session_state.user_answer = user_input
                if user_input.strip().lower() == q["answer"].strip().lower():
                    st.success("✅ Correct!")
                    st.session_state.score += 1
                else:
                    st.error(f"❌ Incorrect! The correct answer is **{q['answer']}**.")
                st.session_state.show_feedback = True

        if st.session_state.show_feedback:
            if st.button("Show Example", key=f"example_{q_index}"):
                st.code(q.get("example", "No example available."), language="python")
            if st.button("Next Question", key=f"next_{q_index}"):
                st.session_state.question_index += 1
                st.session_state.show_feedback = False
                st.session_state.user_answer = ""
                st.rerun()

    else:
        st.markdown("## 🎉 Quiz Complete!")
        st.write(f"Your final score is **{st.session_state.score} / {len(questions)}**")
        if st.button("Restart Quiz", key="restart_btn"):
            st.session_state.question_index = 0
            st.session_state.score = 0
            st.session_state.show_feedback = False
            st.session_state.user_answer = ""
            st.rerun()
        if st.button("Quit Application"):
            st.success("✅ Application terminated. You can now close the browser or stop the script.")
            st.stop()

if __name__ == "__main__":
    st.markdown("#### Quiz Application on Python")
    st.write("This is a quiz application. You can answer the questions and see your score at the end.")
    quiz_fun()
