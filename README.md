# Digital Chaos Score

A simple Python tool that calculates a chaos score based on changes
between increasing and decreasing numbers.

## How It Works

The program compares consecutive numbers and counts how often
their direction changes.

Chaos Score = (Direction Changes / Direction Comparisons) × 100

Equal numbers are skipped when checking direction.

This score is a simple rule defined for this project,
not a scientific measure of chaos.

## Levels

- Calm: score below 25
- Moderate: score from 25 to below 75
- Chaotic: score from 75 to 100

## Features

- Accepts numbers entered by the user
- Calculates a score from 0 to 100
- Displays the level
- Automatically saves valid results to chaos_result.txt
- Keeps previous results
- Handles invalid input

## Requirements

- Python 3
- No additional libraries are required

## How to Run

1. Download the project.
2. Open a terminal in the project folder.
3. Run:

   python main.py

4. Enter at least three numbers separated by spaces.
5. Type q to quit.

## Examples

| Input | Score | Level |
|-------|-------|-------|
| 10 20 30 | 0.0 | Calm |
| 10 20 30 20 | 50.0 | Moderate |
| 10 20 10 | 100.0 | Chaotic |
| 5 5 5 | 0 | Calm |

## Project Files

- main.py: program code
- chaos_result.txt: saved results
- README.md: project description

## Skills Used

Functions, loops, lists, user input, error handling, and file operations.