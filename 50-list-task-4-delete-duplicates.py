lst = [3,4,5,3,4,6,7]
bez_duplicatov = []
for number in lst:
    if number not in bez_duplicatov:
        bez_duplicatov.append(number)
print(bez_duplicatov)