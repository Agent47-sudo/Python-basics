task1 = input("task1: ").strip().title()
task2 = input("task2: ").strip().title()
task3 = input("task3: ").strip().title()
task4 = input("task4: ").strip().title()

tasks = [task1, task2, task3, task4]

print("\n-------TASK LIST-------")
print(f"1. {tasks[0]}\n2. {tasks[1]}\n3. {tasks[2]}\n4. {tasks[3]}")
print(f"\nTotal tasks: {len(tasks)}\n---------------------")