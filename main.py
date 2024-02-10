import random

job_list = {"Java developer": {"salary": 50, "gladness_less": 10},
            "Python developer": {"salary": 40, "gladness_less": 3},
            "C++ developer": {"salary": 45, "gladness_less": 25},
            "Rust developer": {"salary": 70, "gladness_less": 1}, }

brand_of_car = {"BMW": {"fuel": 100, "strength": 100, "cons": 12},
                "Lada": {"fuel": 100, "strength": 30, "cons": 10},
                "Volvo": {"fuel": 80, "strength": 120, "cons": 8},
                "Ferrari": {"fuel": 60, "strength": 80, "cons": 14}, }


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 500
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brand_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            else:
                self.satiety += 5
                self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 15:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 5

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 15:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel!")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food!")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("I'm happy!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 5

    # Дописати ці 3 методи
    def chill(self):
        if self.gladness <= 20:
            print("I'm chilling")
            self.gladness += 15
            self.home.mess += 10
            self.satiety += 5
            self.money -= 45
        elif self.gladness >= 100:
            self.gladness = 100

    def clean_home(self):
        if self.home.mess == 30:
            print("Time to clean up my house!")
            self.home.mess = 0
            self.gladness -= 5
            self.satiety -= 10
            self.money -= 5
        elif self.home.mess < 0:
            self.home.mess = 0

    def to_repair(self):
        if self.car.strenght <= 10:
            print("Gotta fix the car!")
            if self.car.brand == "BMW":
                if self.car.strenght > 100:
                    self.car.strenght = 100
                else:
                    self.car.strenght += 15
                    self.money -= 75
            elif self.car.brand == "Lada":
                if self.car.strenght > 30:
                    self.car.strenght = 30
                else:
                    self.car.strenght += 5
                    self.money -= 30
            elif self.car.brand == "Volvo":
                if self.car.strenght > 120:
                    self.car.strenght = 120
                else:
                    self.car.strenght += 15
                    self.money -= 75
            elif self.car.brand == "Ferrari":
                if self.car.strenght > 80:
                    self.car.strenght = 80
                else:
                    self.car.strenght += 10
                    self.money -= 100

    def days_indexes(self, day):
        d = f"Today the {day} of {self.name} life"
        # ===="Today the 1 of Ivan life"====
        print(f"{d:=^50}\n")
        h_i = f"{self.name}'s indexes"
        print(f"{h_i:=^50}\n")
        print(f"Total money: {self.money}")
        print(f"Mood: {self.gladness}")
        print(f"Satiety: {self.satiety}")
        home_i = "Home indexes"
        print(f"{home_i:=^50}\n")
        print(f"Food at home: {self.home.food}")
        print(f"Mess at home: {self.home.mess}")
        car_ind = f"{self.car.brand} car indexes"
        print(f"{car_ind:=^50}\n")
        print(f"Car fuel: {self.car.fuel}")
        print(f"Car strength: {self.car.strenght}")

    def is_alive(self):
        pass

    def live(self):
        pass


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.cons = brand_list[self.brand]['cons']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.cons:
            self.fuel -= self.cons
            self.strength -= 1
            return True
        else:
            print("The car cannot move!")
            return False


class House:
    def __init__(self):
        self.food = 0
        self.mess = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']



# h = Human()
# h.get_home()
# print(h.home.food)
