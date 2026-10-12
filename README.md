# Digital Chaos Score

A simple Python project that calculates a score based on direction changes in a list of numbers.

## How It Works

The program checks whether the numbers switch from increasing to decreasing or from decreasing to increasing.

Score = (Direction Changes / Comparisons) × 100

Equal consecutive numbers are skipped.

## Levels

- **Low Change:** Score below 25
- **Medium Change:** Score from 25 to below 75
- **High Change:** Score of 75 or above

## Features

- Accepts at least three numbers.
- Calculates a score between 0 and 100.
- Displays the change level.
- Saves results to `score_results.txt`.
- Handles invalid input.
- Runs until the user enters `q`.

## How to Run

1. Install Python.
2. Run `python main.py`.
3. Enter numbers separated by spaces.
4. Type `q` to quit.

## Example

Input: `10 20 30 20 10`

Chaos Score: 33.3  
Level: Medium Change

## Skills Used

Functions, loops, lists, conditions, error handling and file operations.