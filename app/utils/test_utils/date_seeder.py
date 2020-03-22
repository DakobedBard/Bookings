

import csv
from users.models import Host

def seed_host(host_csv):
    with open(host_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                try:

                    host = Host()

                    username = row[0]
                    host.username=username

                    password = row[1]
                    host.password=password

                    first_name = row[2]
                    host.first_name = first_name

                    last_name = row[3]
                    host.last_name = last_name

                    email = row[5]
                    host.email = email

                    phone_number = row[6]
                    host.phone_number=phone_number

                    state = row[7]
                    host.state=state

                    city = row[8]
                    host.city = city

                    address = row[9]
                    host.address=address

                    zip = int(row[10])
                    host.zip = zip

                    host.save()
                    print("Processed a host")
                    line_count += 1
                except Exception as e:
                    print(e)

        print(f'Processed {line_count} lines.')

seed_host('hosts.csv')
