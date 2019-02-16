import json
import os


def handle_location(location, location_list):
    """
    (dict, list) -> int
    Print items contained in given part of file
    :param location: current location
    :param location_list: current_location in list representation
    :return: 0 if there was 1 item and location moved 2 levels down
    else 1
    """
    if type(location) == dict:
        for i in location:
            if type(location[i]) != dict and type(location[i]) != list:
                print("{:20} : {}".format(i, location[i]))
            else:
                print("{:20} : ...".format(i))

    elif type(location) == list:
        if len(location) == 1:
            location_list.append("0")
            return 0
        for i in range(len(location)):
            if type(location[i]) == dict:
                if "screen_name" in location[i]:
                    print("{:20} : ...".format(location[i]["screen_name"]))
            elif type(location[i]) == list:
                if len(location[i]) > 0:
                    print(location[i][0])
            else:
                print(location[i])
    return 1


def move(location, location_list, root):
    """
    (dict, list, dict) -> dict
    Change location_list and return new_location by users input
    :param location: current location
    :param location_list: current location in list representation
    :param root: dict formed of .json file
    :return: updated location
    """
    a = input("Where to go now: ")
    if a.strip() == "..":
        # move one level higher
        location_list.pop()
        if not location_list:
            return
        new_location = location_list[0]
        for i in location_list[1:]:
            new_location += "[" + str(i) + "]"
        location = eval(new_location)

        # prevent from going back down
        if len(location) == 1:
            location_list.pop()
            if not location_list:
                return
            new_location = location_list[0]
            for i in location_list[1:]:
                new_location += "[" + str(i) + "]"
                location = eval(new_location)
        return location

    else:
        if type(location) == dict and a in location:
            location_list.append('"' + a.strip() + '"')
            return location[a]
        elif type(location) == list:
            # find out what item to choose
            for i in range(len(location)):
                if type(location[i]) == dict:
                    if "screen_name" in location[i] and location[i]['screen_name'] == a:
                        location_list.append(str(i))
                        return location[i]


def get_file():
    """
    (None) -> dict
    :return: dict made if .json file entered by user
    """
    try:
        file_name = input("Enter the file name (.json format) or path to it: ")
        while not file_name.endswith(".json"):
            file_name = input("Enter a .json file: ")
        file = open(file_name, "r")
        js = json.load(file)
        return js
    except FileNotFoundError:
        os.system("clear")
        print("Nos such file in directory")
        return get_file()


def print_intro():
    """
    (None) -> None
    Print the information for user
    """
    print("""This program helps to navigate on .json file got via Twitter API
You can navigate to items marked as "..." by writing
their names or use ".." to move a level higher""")


def main():
    """
    Main function of the program
    """
    print_intro()
    root = get_file()
    # create current location
    location = root
    location_list = ["root"]
    while location_list:
        os.system("clear")
        print("You are here:", ".".join(location_list))
        # handle location and miss move if location
        # automatically moved 2 levels deeper
        if handle_location(location, location_list) == 0:
            location = location[0]
            continue
        location = move(location, location_list, root)


if __name__ == "__main__":
    main()
