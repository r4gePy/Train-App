class Train:
    """
    Class for train,
        features:
        1. up_speed - raising the speed of the train to the specified number
        2. speed - returns the speed of the train
        3. stop_train - train speed will  be equal 0
        4. wagons - returns the number of wagons
        5. connect_wagons - connecting or disconnecting specified
                                                                number of wagons
        6. get_route - train will get route
        7. move_to - change the position of the train to the specified
        8. return_station - Displays the previous, current, and next route point
    """

    def __init__(self, number, type_train, wagons):
        self.number = number
        self.type = type_train
        self.wagons = wagons
        self.t_speed = 0
        self.position = ""
        self.current_position_number = 0

    def up_speed(self, speed):
        """
        upping speed on specified number
        """
        self.t_speed = speed

    def speed(self):
        """
        returns the speed
        """
        return self.t_speed

    def stop_train(self):
        """
        stops the train
        """
        self.t_speed = 0
        return "Train speed equal 0"

    def return_wagons(self):
        """
        returns the speed
        """
        return self.wagons

    def connect_wagon(self):
        """
        :return:
        """
        ask = input("connect/disconnect ?")
        if self.t_speed == 0 and ask == "connect":
            self.wagons += 1
        elif self.t_speed == 0 and ask == "disconnect" and self.wagons != 0:
            self.wagons -= 1
        else:
            return "Train speed not equal 0!"
        return self.wagons

    def get_route(self, list_stations):
        self.route = list_stations
        self.position = list_stations[0]
        self.current_position_number = 0
        return self.position

    def move_forward(self, index):
        self.position = self.route[index]
        self.current_position_number = index
        return self.position

    def move_back(self, index):
        if self.current_position_number > 0:
            self.position = self.route[index]
            self.current_position_number = index
        else:
            return "Position your train = 0"
        return self.position

    def return_previous(self):
        if self.current_position_number != 0:
            return self.route[self.current_position_number - 1]

    def return_position(self):
        return self.route[self.current_position_number]

    def return_next_position(self):
        if self.position != self.route[-1]:
            return self.route[self.current_position_number + 1]
