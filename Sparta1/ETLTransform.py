import csv


def transform_user_details(csv_file_name):
    new_user_data = []

    with open(csv_file_name, newline="") as csv_file:
        user_details_csv = csv.reader(csv_file, delimiter=",")

        for user in user_details_csv:
            transformation = []
            transformation.append(user[1].replace("\n", ""))
            transformation.append(user[2].replace("\n", ""))
            transformation.append(user[-1].replace("\n", ""))
            new_user_data.append(transformation)

    return new_user_data


def create_user_data(old_user_file, new_file_name):
    new_user_data = transform_user_details(old_user_file)
    with open(new_file_name, "w", newline="") as new_file:
        csv_writer = csv.writer(new_file)
        for user in new_user_data:
            csv_writer.writerow(user)


print(transform_user_details("user_details.csv"))
create_user_data("user_details.csv", "new_user_data")
