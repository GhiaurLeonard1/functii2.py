# Ex . 1
# PI = 3.14
# class cerc:#Clasa cerc
#     raza = 20
#     culoare = None
# #
#     def __init__(self, raza, culoare):#Constructor pentru ambele atribute
#         self.raza = raza
#         self.culoare = culoare
#         print("Culoarea este:",culoare)
#         print("Raza este:",raza)
#
#     PI = float(3.14)
#     aria = PI * raza * raza
#     diametru = 2 * raza
#     circumferinta = 2 * raza * PI
#
# cerc1 = cerc("20","alb")
# print("Aria va fi:",cerc1.aria)
# print("Diametrul este de:",cerc1.diametru)
# print("Circumferinta este de:",cerc1.circumferinta)
# cerc2 = cerc("50","aldastru")
# print("Aria va fi:",cerc2.aria)
# print("Diametrul este de:",cerc2.diametru)
# print("Circumferinta este de:",cerc2.circumferinta)
#

#
# # Ex. 2

class rectangle:# atribute lungime,latime, inaltime
    length = None
    width = None
    color = None

    def __init__(self, length, width, color):#constructor pentru toate atributele
        self.length = length
        self.width = width
        self.color = color

    def describe(self):
        print(self.length)
        print(self.width)
        print(self.color)

aria= ("length") * ("width")
perimetru= 2 * ("length") + ("width")
culoare = culoare.replace("Galben","Violet")
#schimb culoarea cu noua culoare, metoda nu returneaza nimic,
rect1 = rectangle(100,60,"Violet")
print(rect1.aria)
print(rect1.perimetru)
print(rect1.culoare)

rect1 = rectangle(140,80,"verde")
print(rect1.aria)
print(rect1.perimetru)
print(rect1.culoare)




# #     def area_rectangle(self):
# #         area = rectangle.length * rectangle.width
# #         return area
# #
# #     def perimeter(self):
# #         perimeter = 2 * (rectangle.length + rectangle.width)
# #         return perimeter
# #
# #     def change_color(self):
# #         rectangle.color = 'green'
# #
# #
# # rectangle = rectangle(20, 10, 'yellow')
# # rectangle.describe()
# # print(f'Area of rectangle is : {rectangle.area_rectangle()}')
# # print(f'Perimeter of rectangle is : {rectangle.perimeter()}')
# # rectangle.change_color()
# # rectangle.describe()
#
#
# # Ex. 3
#
# # class employee:
# #     first_name = None
# #     last_name = None
# #     salary = None
# #
# #     def __init__(self, first_name, last_name, salary):
# #         self.first_name = first_name
# #         self.last_name = last_name
# #         self.salary = salary
# #
# #     def describe(self):
# #         print(f'The first name of employee is : {employee.first_name}.')
# #         print(f'The last name of employee is : {employee.last_name}.')
# #         print(f'The salary of employee is : {employee.salary} ron.')
# #
# #     def complet_name(self):
# #         print(f'The complete name of employee it is : {employee.first_name +" " + employee.last_name}.')
# #
# #     def monthly_salary(self):
# #         print(f'The monthly salary is : {employee.salary} ron.')
# #
# #     def annual_salary(self):
# #         annual_salary = 12 * employee.salary
# #         print(f'The annual salary is : {annual_salary} ron.')
# #
# #     def salary_raise(self):
# #         salary_raise = employee.salary / 6000 / 10
# #         # salary_raise = salary_raise * 100
# #         salary_raise = "{:.1%}".format(salary_raise)
# #         print(f'The salary_raise is {salary_raise}')
# #
# #
# # employee = employee('Mihail', 'Ilut', 6900)
# # employee.describe()
# # employee.complet_name()
# # employee.monthly_salary()
# # employee.annual_salary()
# # employee.salary_raise()
#
#
# # Ex. 4
#
# # class account:
# #     iban = None
# #     account_holder = None
# #     balance = None
# #
# #     def __init__(self, iban, account_holder, balance):
# #         self.iban = iban
# #         self.account_holder = account_holder
# #         self.balance = balance
# #
# #     def balance_display(self):
# #         print(f'Account holder, {account.account_holder} has in the account,'
# #               f' {account.iban} amount of {account.balance} ron.')
# #
# #     def account_debit(self):
# #         debit = 200
# #         print(f'The bank account was debited with the amount of {debit} ron.')
# #
# #     def account_credit(self):
# #         credit = 20000
# #         print(f'The bank account was credited with amount of {credit} ron.')
# #
# #
# # account = account('RO123456789ZZ133A2', 'Mihail Ilut', 99999)
# # account.balance_display()
# # account.account_debit()
# # account.account_credit()
#
#
# # Ex. 5
#
# # from datetime import date
# # from tabulate import tabulate
# #
# #
# # class invoice:
# #     SERIAL = 'ROCJ'
# #     number = None
# #     product_name = None
# #     quantity = None
# #     price_buc = None
# #
# #     def __init__(self, number, product_name, quantity, price_buc):
# #         self.number = number
# #         self.product_name = product_name
# #         self.quantity = quantity
# #         self.price_buc = price_buc
# #
# #     def change_quantity(self):
# #         invoice.quantity = 700
# #         print(invoice.quantity)
# #
# #     def change_price(self):
# #         invoice.price_buc = 7
# #
# #     def change_product(self):
# #         invoice.product_name = "Phone"
# #
# #     def invoice_generate(self):
# #         today = date.today()
# #         total = invoice.quantity * invoice.price_buc
# #         print(f'Inovice SN: {invoice.SERIAL}, Nr: {invoice.number}')
# #         print("In data :", today)
# #         print(tabulate([["Product", "Quantity", "Price/Buc.", "Total"],
# #                         [invoice.product_name, invoice.quantity, invoice.price_buc, total]], headers="firstrow"))
# #
# #
# # invoice = invoice(12345, 'Case', 5, 39)
# # invoice.change_product()
# # invoice.change_quantity()
# # invoice.change_price()
# # invoice.invoice_generate()
#
#
# # Ex. 6
#
#
# # class car:
# #     brand = 'Volvo'
# #     model = None
# #     max_speed = None
# #     current_speed = 0
# #     color = 'grey'
# #     colors_available = {'red', 'fuchsia', 'blue', 'green', 'black'}
# #     registered = False
# #
# #     def __init__(self, model, max_speed):
# #         self.model = model
# #         self.max_speed = max_speed
# #
# #     def describe(self):
# #         print(f'The brand of car is : {car.brand}')
# #         print(f'The model of car is : {car.model}')
# #         print(f'The speed now is : {car.current_speed}')
# #         print(f'The maximum speed of car is : {car.max_speed}')
# #         print(f'The color of car is : {car.color}')
# #         print(f'The car is registered with : {car.registered}')
# #
# #     def registered_now(self):
# #         car.registered = True
# #         print(f'The car is registered now.')
# #
# #     def paint_car(self):
# #         new_color = 'blue'
# #         if new_color in car.colors_available:
# #             print(f'The new color of car is {new_color}.')
# #         else:
# #             print(f'This color is not available for moments.')
# #
# #     def accelerate(self):
# #         car.current_speed = 80
# #         if car.current_speed < 0:
# #             print(f'This speed is invalid for car.')
# #         elif car.current_speed < car.max_speed:
# #             print(f'The current speed of car is : {car.current_speed}.')
# #         elif car.current_speed > car.max_speed:
# #             car.current_speed = 200
# #             print(f'The maximum speed of this car has been exceeded ,'
# #                   f'and I returned to the maximum possible speed which is : {car.max_speed},')
# #
# #     def brakes_car(self):
# #         car.now_speed = 0
# #         print(f'The speed of car is {car.now_speed}, and the car is stopped.')
# #
# #
# # car = car('XC60', 200)
# # car.describe()
# # car.registered_now()
# # car.paint_car()
# # car.accelerate()
# # car.brakes_car()
#
#
# # Ex. 7
#
#
# class to_do_list:
#     to_do = {None: None}
#
#     def add_task(self):
#         to_do_list.to_do = {"make_clean": "you have to vacuum, wipe the dust, air the room"}
#         to_do_list.to_do.update({"make_shower": "Go to bathroom and wash your body"})
#
#     def end_task(self):
#         to_do_list.to_do.pop("make_shower")
#
#     def print_to_do(self):
#         for x in to_do_list.to_do:
#             print(f'You have to do : {x}.')
#
#     def details_to_do(self):
#         if "make_dinner" not in to_do_list.to_do:
#             x = input('Do you want to add a new task ? \n')
#             if x == 'yes':
#                 details1 = input('Please insert the task name :\n')
#                 details2 = input('Please insert the task description :\n')
#                 to_do_list.to_do.update({details1: details2})
#                 print(f'You have to do : {to_do_list.to_do.items()}')
#             else:
#                 print('Goodbye')
#         else:
#             print(f'This task already exists.')
#
#
# to_do_list = to_do_list()
# to_do_list.add_task()
# to_do_list.end_task()
# to_do_list.print_to_do()
# to_do_list.details_to_do()