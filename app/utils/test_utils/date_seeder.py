

import csv
from users.models import Host
from rooms.models import Room

class DataSeeder:
    @staticmethod
    def seed_host(host_csv):
        with open(host_csv) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:

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

                        line_count += 1
                    except Exception as e:
                        print(e)

    def seed_rooms(rooms_csv):
        with open(rooms_csv) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:

                    line_count += 1
                else:
                    try:
                        room = Room()
                        hostID = int(row[0])+29
                        host = Host.objects.get(id=hostID)
                        room.host = host

                        name = row[1]
                        room.name = name


                        address = row[2]
                        room.name = address

                        city = row[3]
                        room.city = city

                        state = row[4]
                        room.name = state

                        lat = row[5]
                        room.name = float(lat)

                        lng = row[6]
                        room.long = float(lng)
                        room.save()
                        property_type = row[7]
                        room.property_type = property_type

                        guest_count = row[8]
                        room.guest_count = guest_count

                        bed_count = row[9]
                        room.bed_count = bed_count

                        bath_count = row[10]
                        room.bath_count = bath_count

                        description = row[11]
                        room.description = description

                        available_date = row[12]
                        room.available_date = available_date

                        price = row[13]
                        room.price = int(price)

                        published = row[14]
                        room.published = published

                        room.save()
                        print("save a room")
                        line_count += 1
                    except Exception as e:
                        print(e)


    seed_rooms('rooms.csv')

