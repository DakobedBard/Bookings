import csv
from users.models import Host, Guest
from rooms.models import Room
from django.db.models import Avg, Max, Min, Sum

class DataSeeder:
    '''
    Data seeding class with methods for seeding specific tables

    '''

    @staticmethod
    def seed_data(model, csv_file):
        if model == 'host':
            parse_method = DataSeeder.parse_host_csv_row
        elif model == 'guest':
            parse_method = DataSeeder.parse_guest_csv_row
        elif model == 'room':
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
                        print("I processed a row of " + model)
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
        host.address = row[8]
        host.zip = int(row[9])
        host.save()

    @staticmethod
    def parse_guest_csv_row(row):
        guest = Guest()
        guest.username = row[0]
        guest.password = row[1]
        guest.first_name = row[2]
        guest.last_name = row[3]
        guest.email = row[4]
        guest.phone_number = row[5]
        guest.state = row[6]
        guest.city = row[7]
        guest.address = row[8]
        guest.zip = int(row[9])
        guest.save()

    @staticmethod
    def parse_room_csv_row(row):

        minID =  Host.objects.all().aggregate(Min('id'))['id__min'] #
        hostID = int(row[0]) + minID - 1  # Account for the offset

        room = Room()
        room.host = Host.objects.get(id=hostID)

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

    @staticmethod
    def default_seed():
        DataSeeder.seed_data('host', 'hosts.csv')
        DataSeeder.seed_data('guest', 'guests.csv')
        DataSeeder.seed_data('room', 'rooms.csv')


# DataSeeder.seed_data('host', 'hosts.csv')
# DataSeeder.seed_data('guest', 'guests.csv')
# DataSeeder.seed_data('room', 'rooms.csv')

