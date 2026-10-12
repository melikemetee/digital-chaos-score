def calculate_score(numbers):
    changes = 0
    comparisons = 0
    previous = 0

    for i in range(len(numbers) - 1):
        difference = numbers[i + 1] - numbers[i]

        if difference != 0:
            if previous != 0:
                comparisons += 1

                if difference * previous < 0:
                    changes += 1

            previous = difference

    if comparisons == 0:
        return 0

    score = (changes / comparisons) * 100
    return round(score, 1)


def find_level(score):
    if score < 25:
        return "Calm"
    elif score < 75:
        return "Moderate"
    else:
        return "Chaotic"


def save_result(numbers, score, level):
    with open("chaos_results.txt", "a") as file:
        file.write("Numbers: " + str(numbers) + "\n")
        file.write("Chaos Score: " + str(score) + "\n")
        file.write("Level: " + level + "\n\n")


while True:
    text = input("Enter numbers or type q to quit: ")

    if text.strip().lower() == "q":
        break

    try:
        numbers = []

        for value in text.split():
            numbers.append(float(value))

        if len(numbers) < 3:
            print("Please enter at least three numbers.")
            continue

        score = calculate_score(numbers)
        level = find_level(score)

        print("Chaos Score:", score)
        print("Level:", level)

        save_result(numbers, score, level)
        print("Result saved.")

    except ValueError:
        print("Please enter only numbers.")