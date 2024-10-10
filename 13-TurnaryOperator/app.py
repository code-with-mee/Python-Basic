score = 12

if score == 12:
    message = "the best"
elif score >= 10:
    message = "good"
print(message)

message2 = "the best" if score == 12 else "good"
print(message2)
