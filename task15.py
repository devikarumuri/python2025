#creating classes and object by using laptop as object
class laptop():
    def __init__(self,brand,model,year_of_manufacture):
        self.brand=brand
        self.model=model
        self.year_of_manufacture=year_of_manufacture

    def watching(self,movie):
        print(f"siya is watching {movie} on {self.brand}") 
    def gaming(self,game):
        print(f"laxman is playing {game} in {self.brand} of {self.year_of_manufacture}")  
    def coding(self,language):
        print(f"neha is coding using {language} in {self.brand} of {self.model}")

gadget=laptop("lenovo","ideapad_gaming",2023) 
gadget.watching("ramayan")
gadget.coding("python") 
gadget.gaming("gta") 

#-----------------------------------------------------------------------------------------------------------------#

#class,object,inheritance:
class keypadphone():
    def __init__(self,brand,model,network):
        self.brand=brand
        self.model=model
        self.network=network

    def calling(self,number):
        print(f"he is taking on {self.brand} {self.model} to {number}") 
    def messaging(self,number):
        print(f"he is messaging to {number} in {network} condition") 

class smartphone(keypadphone):
    def browsing(self,app):
        print(f"{app} is best browsing app in {self.brand} mobile") 
    def gaming(self,game):
        print(f"adi id playing {game} in {self.model}") 

class foldable(smartphone):
    def tablet(self):
        print(f"{self.brand}'s {self.model} is trnding now")
    def easy_trading(self,trading_app):
        print(f"in {trading_app} trading is easy") 

my_foldable=foldable("samsung","z fold 5","5g")
my_foldable.calling(12345)
my_foldable.easy_trading("grow") 
my_foldable.gaming("firefire")      



        