names = ["roth", "jenni", "rina"]
for name in names:
    if name.startswith("j"):
        print("found")
        break
else:
    print("not found")

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
for number in numbers:
    if number == 50:
        print(f"found number : {number}")
        break
else:
    print("not found number 50")
