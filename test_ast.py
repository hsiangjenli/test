class Car:
    # 初始化方法，設定屬性
    def __init__(self, color, brand, model):
        """_summary_

        Parameters
        ----------
        color : _type_
            _description_
        brand : _type_
            _description_
        model : _type_
            _description_
        """
        self.color = color
        self.brand = brand
        self.model = model

    # 定義方法，印出車子資訊
    def show_info(self):
        print(f"This car is {self.color}, {self.brand}, {self.model}.")

    # 定義方法，改變車子顏色
    def change_color(self, new_color):
        self.color = new_color
        print(f"The car color has been changed to {self.color}.")


class Bike:
    # 初始化方法，設定屬性
    def __init__(self, color, brand, model):
        self.color = color
        self.brand = brand
        self.model = model

    def show_info(self):
        print(f"This car is {self.color}, {self.brand}, {self.model}.")

    def change_color(self, new_color):
        self.color = new_color
        print(f"The car color has been changed to {self.color}.")


def main():
    car = Car(color='red', brand="BMW", model="none")
    car.show_info()