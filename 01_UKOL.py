
import math

class Locality:
    def __init__(self, name, coefficient):
        self.name = name
        self.coefficient = coefficient

class Property(Locality):
    def __init__(self, name, coefficient, locality):
        super().__init__(name, coefficient)
        self.locality = locality
        
# Daň vypočítej pomocí vzorce: plocha pozemku * koeficient dle typu pozemku (atribut estyte_type) * koeficient obce. 
# U atributu estate_type následující hodnoty a koeficienty:
# -land (zemědělský pozemek) má koeficient 0.85.
# -building site (stavební pozemek) má koeficient 9.
# -forrest (les) má koeficient 0.35.

class Estate(Property):
    def __init__(self, name, coefficient, locality, estate_type, area):
        super().__init__(name, coefficient, locality)
        self.estate_type = estate_type
        self.area = area #area must be in meters
        
    def calculate_tax(self):
        if self.estate_type =="forrest":
            return math.ceil(self.area * 0.35 * self.coefficient)
        if self.estate_type =="building_site":
            return math.ceil(self.area * 9 * self.coefficient)
        if self.estate_type =="land":
            return math.ceil(self.area * 0.85 * self.coefficient)


les = Estate("nazev_katastru_obce", 1000,"locality","forrest", 2)
stavební = Estate("pozemek_name", 100,"locality","building_site", 2)

print(les.calculate_tax())
print(stavební.calculate_tax())

class Residence(Property):
    def __init__(self, name, coefficient, locality, area, commercial):
        super().__init__(name, coefficient, locality)
        self.area = area
        self.commercial = commercial

    def calculate_tax(self):
        if self.commercial == True:
            return math.ceil(self.area * self.coefficient * 15 * 2)
        else:
            return math.ceil(self.area * self.coefficient * 15)


# Zemědělský pozemek o ploše 900 metrů čtverečních v lokalitě Manětín s koeficientem 0.8. Daň z této nemovitosti je 900 * 0.85 * 0.8 = 612.
nemovitost1 = Estate("Manětín", 0.8, "locality", "land", 900)
print(nemovitost1.calculate_tax())

# Dům s podlahovou plochou 120 metrů čtverečních v lokalitě Manětín s koeficientem 0.8. Daň z této nemovitosti je 120 * 0.8 * 15 = 1440.
nemovitost2 = Residence("Manětín", 0.8 ,"locality", 120, False)
print(nemovitost2.calculate_tax())

# Kancelář (tj. komerční nemovitost) s podlahovou plochou 90 metrů čtverečních v lokalitě Brno s koeficientem 3. Daň z této nemovitosti je 90 * 3 * 15 * 2 = 8100.
nemovitost3 = Residence("Brno", 3 ,"locality", 90, True)
print(nemovitost3.calculate_tax())



