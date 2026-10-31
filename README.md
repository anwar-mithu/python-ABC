PythonABC
My Python learning journey: from everyday syntax to the foundations of AI applications.

PythonABC is my personal practice repository. I use it to work through Python concepts, solve exercises, experiment with small programs, and keep track of what I learn.

My goal is to become comfortable reading, writing, debugging, and explaining Python code independently. Over time, I want to apply these skills to data analysis, automation, and applications that combine language models with databases and tools.

This is an evolving learning project. Exercises may contain simple solutions, experiments, and work in progress.
Contents

- Learning goals
- Topics I am practising
- Practice examples
- Connection to AI and database projects
- Getting started
- Running scripts and notebooks
- My practice workflow
- Git workflow
- Next learning goals
- Useful documentation
- Feedback
- Author
  Learning goals
- Understand how Python programs execute, step by step.
- Choose suitable data structures for a problem.
- Break larger problems into small functions and classes.
- Handle unexpected input and execution errors.
- Read and write structured data.
- Organize code into modules that can be reused.
- Use virtual environments and manage dependencies.
- Practise Git and GitHub as part of everyday development.
- Build enough confidence to develop small projects independently.
  Topics I am practising
  The following describes my learning scope. It is not a claim that every topic already has a complete implementation in this repository.

1. Python fundamentals
   Variables, strings, numbers, Boolean values, type conversion, operators, input, and formatted output.

A recurring lesson: understanding the difference between a value and its type. For example, text entered through input is a string, even when it looks like a number or a Boolean. 2. Conditions and loops

- Conditional logic with if, elif, and else.
- Iteration with for and while.
- Loop control with break and continue.
- Nested loops, counters, and limited retry attempts.
- Combining conditions with and, or, and not.

3. Functions and scope

- Defining and calling functions.
- Parameters, arguments, and return values.
- Understanding the difference between returning a value and printing it.
- Local and global scope.
- Separating input, processing, and output.

4. Data structures and comprehensions

- Lists, tuples, sets, and dictionaries.
- Indexing, slicing, and iteration.
- Filtering and transforming collections.
- List comprehensions and dictionary comprehensions.
- Working with nested data.

5. Exception handling
   Using try, except, else, finally, and raise to handle errors and enforce rules. Practice includes invalid input, failed conversions, and understanding when a conditional check is appropriate versus when an exception needs handling.
6. Modules, files, and JSON

- Imports and reusable modules.
- Reading and writing text files with with open(...).
- Working with JSON and CSV data.
- Understanding json.load(), json.loads(), and json.dump().
- Separating code, input data, and generated output.

7. Object-oriented programming

- Classes, objects, and instances.
- Instance attributes and class attributes.
- **init** and self.
- Instance methods and static methods.
- Inheritance, super(), and method overriding.
- Encapsulation, abstraction, inheritance, and polymorphism.
- Composition: building objects that use other objects.

8. NumPy and data exploration
   Array creation, shapes, dimensions, indexing, slicing, and basic calculations. A particular focus is understanding how rows, columns, and additional axes relate to an array's shape.
9. Small practical programs
   Exploring HTTP requests, JSON responses, simple data processing, and charts. These exercises connect basic Python concepts to tasks involving external data.
10. Development tools
    Virtual environments, package installation, VS Code, Python scripts, notebooks, Git staging, commits, branches, and pushing changes to GitHub.
    Practice examples
    Examples from my learning journey include:
    Exercise Skills involved
    Select integers divisible by 4 but not by 8 Input parsing, conversion, conditions, filtering
    Give a user a limited number of attempts While loops, counters, break conditions
    Process several questions with retries Nested loops, state tracking, summaries
    Find the longest word in a text file File reading, splitting, punctuation handling, comparison
    Filter words using a condition String methods, loops, lists
    Store and inspect query results Classes, attributes, methods, Boolean values
    Read and write structured records Dictionaries, lists, JSON
    Explore multidimensional arrays NumPy, shapes, indexing
    Retrieve and plot weather data HTTP requests, JSON, data transformation, plotting

Individual exercises may be revised as I learn clearer approaches.
Connection to AI and database projects
Some examples use natural-language questions, generated SQL or MDX queries, execution results, and correctness checks. These relate to my interest in systems that turn questions into database queries.

The Python concepts have direct uses in those projects:
Python concept Possible application
Dictionaries Store the current question, query, feedback, and execution status
Lists Keep tool history and previous attempts
Functions Separate schema retrieval, query generation, execution, and validation
Loops Manage a bounded sequence of attempts
Exceptions Handle failed requests, invalid responses, and database errors
JSON Store benchmark questions, configuration, and run results
Classes Organize model clients, tools, and result records
Modules Keep project responsibilities in separate files

These are motivations for learning. PythonABC itself is a practice repository; it does not claim to contain a complete agent framework or a production database system.
Getting started
Prerequisites

- Python 3. My current learning environment uses Python 3.12.
- Git, if cloning the repository.
- An editor such as VS Code.
- A notebook environment if running .ipynb files.

1. Download or clone
   On the repository page, select Code and copy its HTTPS or SSH clone URL. Replace the placeholder below with that URL:
   git clone YOUR_REPOSITORY_URL
   cd PythonABC
   If you already have the repository locally, open its folder instead of cloning it again.
2. Create a virtual environment
   On Windows:
   py -m venv .venv
   On macOS or Linux:
   python3 -m venv .venv
3. Activate it
   Windows PowerShell:
   .\.venv\Scripts\Activate.ps1
   Windows Command Prompt:
   .venv\Scripts\activate.bat
   macOS or Linux:
   source .venv/bin/activate
   In VS Code, select the interpreter from this environment using Python: Select Interpreter.
4. Install dependencies when needed
   Many basic exercises use only Python's standard library and need no additional packages.

If an exercise has a requirements.txt, install from its actual location:
python -m pip install -r path/to/requirements.txt
Otherwise, install the packages imported by the exercise you want to run. Examples of packages used for numerical and plotting practice are:
python -m pip install numpy pandas matplotlib requests
These commands are setup guidance, not a verified dependency list for every file. Replace example paths with the paths in your checkout.
Running scripts and notebooks
Python scripts
From the appropriate directory, run:
python path/to/exercise.py
Replace path/to/exercise.py with an actual filename. Some programs ask for terminal input; read the prompt before entering a value.
Jupyter notebooks
Open a .ipynb file in VS Code with notebook support and choose the intended Python environment as its kernel. If that environment needs a kernel package:
python -m pip install ipykernel
Run cells from top to bottom. When checking whether a notebook works independently, restart its kernel and run all cells in order.
Files and external services
Relative paths such as data.txt are resolved from the program's current working directory. Check where the terminal is running if a file cannot be found.

Read scripts before running them: some exercises write output files. API examples may require internet access, while database-related examples may depend on services that are not included in this repository.

There is no assumed single command that runs every exercise. Choose one script or notebook at a time.
My practice workflow

1. Read the problem and identify its input and expected output.
2. Write the steps in plain language.
3. Implement a small working solution.
4. Check normal cases and relevant edge cases.
5. Read error messages and fix the underlying issue.
6. Explain why the solution works.
7. Improve names, structure, and comments where needed.
8. Commit the completed change with a descriptive message.
   The goal is to understand the logic well enough to adapt it to a new problem. Documentation is part of the process; I do not expect to memorize every function or method.
   Git workflow
   For a small practice update:
   git status
   git diff
   git add path/to/exercise.py
   git diff --cached
   git commit -m "Add a limited-attempt question exercise"
   git push
   For several selected files:
   git add path/to/first.py path/to/second.py README.md
   Use git add . only after checking that all changes under the current directory belong in the next commit. Virtual environments, credentials, and unrelated generated output should stay out of commits.

For a larger change, practise a separate branch:
git switch -c practice/query-result-class
After making and committing the changes, publish the branch:
git push -u origin practice/query-result-class
A pull request can then be used to review the changes before merging them.
Next learning goals

- [ ] Refactor larger exercises into small reusable functions.
- [ ] Practise passing structured data between modules.
- [ ] Add useful tests for functions with several possible outcomes.
- [ ] Improve logging and error messages.
- [ ] Build a small database-backed Python application.
- [ ] Connect a local language model to clearly defined tools.
- [ ] Build and inspect a bounded agent loop.
- [ ] Document setup and execution steps as projects grow.
      This list records intended next steps rather than completed features.
      Useful documentation
- Python documentation
- Python tutorial
- Python standard library
- NumPy documentation
- pandas documentation
- Matplotlib documentation
- Requests documentation
- Git documentation
- GitHub documentation
  Feedback
  Suggestions and corrections are welcome. When discussing an exercise, include the filename, the input used, the expected behavior, and the actual output or error. An explanation of why a change helps is especially useful for this learning repository.
  Author
  Md Anwarul Islam Mithu

Learning Python through regular practice, with a longer-term interest in AI, automation, and database applications.
