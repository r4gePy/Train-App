class Route:
    """
    Class for route,
        features:
        1. create route - only one start and end
        2. add_point - usual adding point on position [-2]
        3. delete_point - deleting on value
        4. print_station - printing route_list
    """

    def __init__(self):
        self.route_list = []

    def create_route(self, start, end):
        """
        :param end:
        :param start, end adding in list route
        """
        if self.route_list:
            self.route_list[0] = start
            self.route_list[-1] = end
        else:
            self.route_list.append(start)
            self.route_list.append(end)

    def add_point(self, name_point):
        """
        :param name_point adding in list on position [-2]
        """
        self.route_list.insert(-1, name_point)

    def delete_point(self, name):
        """
        point will delete from list (only be removed one at a time)
        """
        self.route_list.remove(name)

    def print_station(self):
        """
        printing route_list
        """
        return self.route_list
