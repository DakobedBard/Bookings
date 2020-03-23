

import csv
from users.models import Host, Guest
from rooms.models import Room

class DataSeeder:

    @staticmethod
    def seed_data(model, csv_file):
        if model == 'host':
            parse_method = DataSeeder.parse_host_csv_row
        elif model == 'guest':
            parse_method = DataSeeder.parse_guest_csv_row
        elif model == 'rooms':
            parse_method = DataSeeder.parse_room_csv_row
        else: return False

        with open(csv_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    try:
                        parse_method(row)
                        line_count += 1
                    except Exception as e:
                        print(e)



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
                        DataSeeder.parse_host_csv_row(row)
                        line_count += 1
                    except Exception as e:
                        print(e)

    @staticmethod
    def seed_rooms(rooms_csv):
        with open(rooms_csv) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:

                    line_count += 1
                else:
                    try:
                        DataSeeder.parse_room_csv_row(row)
                        print("save a room")
                        line_count += 1
                    except Exception as e:
                        print(e)

    @staticmethod
    def parse_host_csv_row(row):
        host = Host()

        host.username = row[0]
        host.password = row[1]
        host.first_name = row[2]
        host.last_name = row[3]
        host.email = row[4]
        host.phone_number = row[5]
        host.state = row[6]
        host.city = row[7]
        print("row 8 " + row[8])
        # host.address = row[8]
        host.zip = int(row[9])
        host.save()

    @staticmethod
    def parse_guest_csv_row(row):
        host = Host()

        host.username = row[0]
        host.password = row[1]
        host.first_name = row[2]
        host.last_name = row[3]
        host.email = row[4]
        host.phone_number = row[5]
        host.state = row[6]
        host.city = row[7]
        print("row 8 " + row[8])
        # host.address = row[8]
        host.zip = int(row[9])
        host.save()


    @staticmethod
    def parse_room_csv_row(row):
        room = Room()
        hostID = int(row[0]) + 44
        host = Host.objects.get(id=hostID)
        room.host = host

        room.name = row[1]
        room.address = row[2]
        room.city = row[3]
        room.state = row[4]
        room.lat = float(row[5])
        room.long = float(row[6])
        room.property_type = row[7]
        room.guest_count = row[8]
        room.bed_count = row[9]
        room.bath_count = row[10]
        room.description = row[11]
        room.available_date = row[12]
        room.price = int(row[13])
        room.published = row[14]
        room.save()
#DataSeeder.seed_host('hosts.csv')
DataSeeder.seed_rooms('rooms.csv')

