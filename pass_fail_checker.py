name = input("Enter your name: ").strip().title()
score = float(input("Enter your score: "))

information = {
    "name": name,
    "score": score
}

if information['score'] <= 33:
    print(f"Sorry, {information['name']}. You have failed.")
else:
    print(f"Congratulations, {information['name']}! You have passed.")