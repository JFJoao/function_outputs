def formated_name (first_name, last_name):
    if first_name == "" or last_name == "":
        return(f"You didn't provide correct data.")
    fixed_first_name = first_name.title()
    fixed_last_name = last_name.title()
    return (f"{fixed_first_name} {fixed_last_name}")
first_name = ""
last_name = ""
while first_name == "" or last_name == "":
    print (formated_name(input("What's your first name ?\n"), input("What's your last name?\n")))
