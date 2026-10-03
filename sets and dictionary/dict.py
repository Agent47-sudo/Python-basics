marks = {
    "Agent": 90,
    "Agent2": 80,
    "Agent3": 70,
}
print(f"Agent's marks: {marks['Agent']}\nAgent2's marks: {marks['Agent2']}\nAgent3's marks: {marks['Agent3']}")


info = {
    "name": "Agent",
    "age": 20,
    "city": "Punjab",
    "mark": [85, 56, 76]
}

print(f"\n-------------\nName: {info['name']}\nAge: {info['age']}\nCity: {info['city']}\nMarks: {info['mark']}")
marks.update({"Agent": 95, "Agent2": 85, "Agent3": 75})
print(marks)

print(marks.get("Agent4", "Not found")) # it will return "Not found" if the key is not present in the dictionary.
empty_dict = {} # this is an empty dictionary