from prettytable import PrettyTable


class Station:
    """
    Class for station,
        features:
        1. add_train - adding train in general list, by type
        2. all_trains - printing all trains, without considering type
        3. type_trains - output of trains by type, each type on a separate line
        4. send_train - sending train
    """

    def __init__(self):
        self.heavy_trains = []
        self.human_trains = []

    def add_train(self, name_train):
        """
        :param name_train: adding in list by type
        """
        type_train = input("Введите тип поезда для " + name_train + "\n")
        if type_train.lower() == "грузовой":
            self.heavy_trains.append(name_train)
        elif type_train.lower() == "пассажирский":
            self.human_trains.append(name_train)

    def all_trains(self):
        """
        printing all trains without considering type
        """
        table = PrettyTable(["Имя поезда", "Тип"])
        for x in self.heavy_trains:
            table.add_row([x.title(), "Грузовой"])

        for x in self.human_trains:
            table.add_row([x.title(), "Пассажирский"])

        return table

    def type_trains(self):
        """
        output of trains by type
        """
        return "Грузовые: ", self.heavy_trains, "Пассажирские: ", \
               self.human_trains

    def send_train(self):
        """
        sending train if he in list
        """
        train_send = input("Введите номер поезда, который хотите отправить:\n")
        if train_send.lower() in self.heavy_trains:
            self.heavy_trains.remove(train_send)
        elif train_send.lower() in self.human_trains:
            self.human_trains.remove(train_send)
        else:
            return "Поезд не найден!"
