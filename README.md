# Digital Chaos Score

## About the Project

Digital Chaos Score is a simple Python project that calculates a score based on the changes between numbers entered by the user.

The program calculates the score, displays a status, and saves the result in a text file.

## Features

* Calculate a chaos score from a list of numbers
* Classify the result as Calm, Moderate, or Chaotic
* Save the result to a text file
* Handle invalid user input
* Allow multiple calculations in one session
* Exit the program by typing `exit`

## Technologies

* Python
* Functions and Loops
* File Handling
* Exception Handling

## How It Works

1. The user enters numbers separated by spaces.
2. The program calculates the differences between consecutive numbers.
3. The program calculates the chaos score.
4. The score is interpreted as Calm, Moderate, or Chaotic.
5. The result is displayed in the terminal.
6. The result is saved to `chaos_result.txt`.

## How to Run

1. Install Python.

2. Download or clone this repository.

3. Open the project folder in a terminal.

4. Run the following command:

   ```bash
   python main.py
   ```

5. Enter at least two numbers separated by spaces.

6. Type `exit` to close the program.

## Example

**Input:**

```text
10 20 30 40
```

**Output:**

```text
Chaos Score: 100.0
Status: Chaotic
Result saved successfully.
```

## Project Structure

```text
digital-chaos-score/
├── main.py
├── chaos_result.txt
└── README.md
```

Note: `chaos_result.txt` is created automatically when a result is saved.

## Team

This project is developed as a team project to practice basic Python programming, functions, loops, and file handling.
