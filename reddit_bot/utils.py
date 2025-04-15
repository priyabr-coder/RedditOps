import csv

def save_usernames_to_csv(usernames, filename="data/usernames.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Username"])
        for user in usernames:
            writer.writerow([user])
