def open_and_print_file(file):
    try:
        with open(file, "r") as opened_file:
            file_line_list = opened_file.readlines()
            for line in file_line_list:
                print(line. replace("\n", ""))

    except FileNotFoundError as e:
        print("Couldn't find that file, soz:\n", e)
    finally:
        print("\nDone reading the file.")


def write_to_file(file, order_item):
    try:
        with open(file, "a") as file_to_write:
            file_to_write.write(order_item + "\n")
    except FileNotFoundError:
        print("That file doesn't exist. ")

open_and_print_file("order.txt")
write_to_file("order.txt", "Mozzarella Sticks")
open_and_print_file("order.txt")
