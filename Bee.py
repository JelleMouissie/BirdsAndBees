class Bee:
    def __init__(self, hive_location):
        self.employed = False
        self.hive_location = hive_location
        self.pos_x = hive_location[0]
        self.pos_y = hive_location[1]
        self.load_pollen = 0
        self.load_nectar = 0

        self.food_location = []
        self.food_priority = 0

    def gather_food():
        pass

    def go_home():
        pass

    def go_to_food():
        pass

    def dance():
        pass


class Scout(Bee):
    def __init__(self, hive_location):
        super().__init__(hive_location)
        self.hive_distance = 0

    def search():
        pass

    def check_block():
        pass


class Employee(Bee):
    def __init__(self, hive_location):
        super().__init__(hive_location)
