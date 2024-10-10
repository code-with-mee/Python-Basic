# and
# or
# not
is_working = True

if is_working:
    print("is working ")
else:
    print("not working anymore")

course = ""
if not course:
    print("course name empty")

age = 24
if age > 18 and age < 45:
    print("qualify")

if 18 < age < 45:
    print("qualify")

if age == 24 or age == 34:
    print("special condition")
