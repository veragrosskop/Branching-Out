import json

def read_users():
    """
    Reads the users.json file and returns a list of users.
    :return:
    """
    try:
        with open("users.json", "r", encoding="utf-8") as file:
            users = json.load(file)
    except FileNotFoundError:
        print("File not found. Please create a users.json file.")
        return []
    return users


def filter_users_by_name(name):
    """
    Filters users by name
    """
    users = read_users()

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)

def filter_by_age(age):
    """
    Filters users by age.
    """
    users = read_users()

    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)


def filter_by_email(email):
    """
    Filters users by email.
    """
    users = read_users()

    filtered_users = [user for user in users if user["email"] == email]

    for user in filtered_users:
        print(user)

if __name__ == "__main__":
    """
    Main function to run the program.
    """
    filter_option = input("What would you like to filter by? "
                          "(Currently, only 'name', 'email' and 'age' are supported): "
                          ).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = int(input("Enter an age to filter users: "))
        filter_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")
