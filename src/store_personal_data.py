# Write your solution here


def store_personal_data(person: tuple):
    with open("people.csv", "a") as my_file:
        line = ""
        for per in person:
            line = line + f"{per};"
        my_file.write(line[:-1] + "\n")
