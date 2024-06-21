class Apartment:
    # конструктор
    def __init__(self, address, square, number_of_rooms, rent_price, description):
        # статус
        self.status = "свободна"
        # - адрес;
        self.adress = address
        # - площадь;
        self.square = square
        # - количество комнат;
        self.number_of_rooms = number_of_rooms
        # - стоимость аренды за сутки;
        self.rent_price = rent_price
        # - текстовое описание;
        self.description = description
    def to_rent(self):
        self.status = "сдана"
    def cancel_rental(self):
        self.status = "свободна"

    def __str__(self):
        return self.status + "-- адрес: " + self.adress + ", площадь = " + str(self.square) + ", комнат " + str(self.number_of_rooms) + ", стоимость аренды за сутки " + str(self.rent_price) + "-- " + self.description
