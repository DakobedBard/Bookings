

import csv
from users.models import Host
with open('host_directory.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            try:
                print("There are rows: " + str(len(row)))
                username = row[0]
                password = row[1]
                first_name = row[2]
                last_name = row[3]
                email = row[4]
                phone_number = row[5]
                state = row[6]
                # city = row[8]
                # address = row[9]
                # zip = row[10]
                # host.username = username
                # host.password = password
                # host.address = address
                # host.city = city
                # host.state  =state
                # host.zip = zip
                # host.phone_number = phone_number
                host = Host()
                host.first_name = first_name
                host.last_name = last_name
                host.email = email
                host.save()
                print("Processed a host")
                line_count += 1
            except Exception as e:
                print(e)

    print(f'Processed {line_count} lines.')


