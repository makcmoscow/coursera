import csv
import os




class CarBase:
    """Базовый класс машин"""

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying




    # def get_photo_file_ext(self):
    #     return (os.path.splitext(self.photo_file_name))


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count




class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra



def get_car_list(csv_filename):
    car_list = []
    return car_list


def read_csv_file(file_obj):
    reader = csv.DictReader(file_obj, delimiter=';')
    for line in reader:
        print(str(line["car_type"]) + " " + str(line["body_whl"]))


filename = "coursera_week3_cars.csv"
with open(filename, "r") as f_obj:
    read_csv_file(f_obj)



