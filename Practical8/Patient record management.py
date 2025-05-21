#create a class called patient
class patients:
    #it contains name age dat history
    def __init__(self, name, age, date, history):
        self.name = name
        self.age = age
        self.date = date
        self.history = history
    
    def describle (self):
        info = self.name + " ages " + str(self.age)+" burn in "+ self.date + " " + self.history
        print(info)
        return info

#example
patient1 = patients("Jay",18, "2025.03.12","no medicine history")
patients.describle(patient1)
        
    