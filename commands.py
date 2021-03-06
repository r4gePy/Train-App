from prettytable import PrettyTable

##########################################################
list_commands_train = PrettyTable(["Название команды", "Что делает"])
list_commands_train.add_row(
    ["Создать поезд", "Создаёт поезд с последующим запросом "
                      "его характеристик"])
list_commands_train.add_row(
    ["Набрать скорость", "Поднимает скорсть на указанное "
                         "значение"])
list_commands_train.add_row(["Скорость", "Выводит текущую скорость"])
list_commands_train.add_row(["Остановить поезд", "Скорость поезд равняется 0"])
list_commands_train.add_row(["Вагоны", "Выводит текущее количество вагонов"])
list_commands_train.add_row(["Вагон", "Присоединяет или отсоединяет один вагон"
                                      "(на выбор)"])
list_commands_train.add_row(
    ["Принят маршрут", "Передаёт список маршрута поезду"])
list_commands_train.add_row(
    ["На следующую", "Поезд проезжает на следующую станцию"])
list_commands_train.add_row(
    ["На предыдущую", "Поезд проезжает на предыдущую станцию"])
list_commands_train.add_row(
    ["Текущую", "Выводит текущую станцию, на которой находится поезд"])
list_commands_train.add_row(
    ["Предыдущую", "Выводит станцию предыдущую станцию"]
)
list_commands_train.add_row(
    ["Следующую", "Выводит следующую станцию"]
)
#
##########################################################

list_commands_route = PrettyTable(["Название команды", "Что делает"])
list_commands_route.add_row(
    ["Создать маршрут",
     "Создаёт маршрут с указанными начальной и конечной точками"])
list_commands_route.add_row(["Добавить точку", "Добавляет промежуточную точку "
                                               "в маршрут"])
list_commands_route.add_row(["Удалить точку", "Удаляет указанную точку из "
                                              "маршрута"])
list_commands_route.add_row(["Маршрут", "Выводит список маршрута"])

##########################################################

list_commands_station = PrettyTable(["Название команды", "Что делает"])
list_commands_station.add_row(["Добавить поезд", "Добавляет поезд на станцию "
                                                 "по типу(один за раз)"])
list_commands_station.add_row(["Все поезда", "Выводит список всех поездов"])
list_commands_station.add_row(["Типы поездов", "Вывод всех отсортированных "
                                               "по типу поездов"])
list_commands_station.add_row(["Отправить поезд",
                               "Отправляет поезд(один за раз)"])

##########################################################
