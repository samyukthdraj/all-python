#unlimited keyworded arguments.
def calc(n, **kwargs):
    print (kwargs)
    n += kwargs["add"]
    n *= kwargs["mult"]
    print(n) #10 + 5 *10

calc(10, add = 5, mult = 10)

# class Car:
#     def __init__(self, **kwargs):
#         self.make = kwargs.get ("make")
#         self.model = kwargs.get ("model")
        
# mycar = Car(make = "Nissan", model = "Sunny")
# print(mycar)  
#       