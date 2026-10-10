
def chaos_score_calculate(data):
    if len(data) < 2:
        print("Please enter at least two numbers.")
        return None

    changes = []

    for i in range(len(data) - 1):
        difference = abs(data[i + 1] - data[i])
        changes.append(difference)

    average = sum(changes) / len(changes)
    biggest = max(changes)

    if biggest == 0:
        return 0

    score = (average / biggest) * 100

    return round(score, 1)


def interpret_chaos(score):
    if score < 30:
        return "Status: Calm"
    elif score < 70:
        return "Status: Moderate"
    else:
        return "Status: Chaotic"


def save_result(data, score, status):
    with open("chaos_result.txt", "a", encoding="utf-8") as file:
        file.write("Input list: " + str(data) + "\n")
        file.write("Chaos Score: " + str(score) + "\n")
        file.write(status + "\n")
        file.write("--------------------\n")

    print("Result saved successfully.")


while True:
    user_input = input(
        "Enter numbers separated by spaces (or type 'exit' to quit): "
    ).strip()

    if user_input.lower() == "exit":
        print("Goodbye.")
        break

    try:
        data = [float(x) for x in user_input.split()]
        score = chaos_score_calculate(data)

        if score is not None:
            status = interpret_chaos(score)

            print("Chaos Score:", score)
            print(status)

            save_result(data, score, status)

    except ValueError:
        print("Please enter only numbers.")