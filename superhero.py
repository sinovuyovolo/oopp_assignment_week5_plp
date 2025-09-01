# Define the Superhero class
class Superhero:
    # Constructor to set up the superhero's attributes
    def __init__(self, name, superpower, city):
        self.name = name            # Attribute: Name of the superhero
        self.superpower = superpower  # Attribute: Superpower of the superhero
        self.city = city            # Attribute: City where the superhero lives
    
    # Method: What the superhero can do (save the day)
    def save_the_day(self):
        print(f"{self.name} is using {self.superpower} to save the day in {self.city}!")

# Define the FlyingHero class, which inherits from Superhero
class FlyingHero(Superhero):
    # Constructor for FlyingHero (with added flight_speed)
    def __init__(self, name, superpower, city, flight_speed):
        super().__init__(name, superpower, city)  # Inherit attributes from Superhero class
        self.flight_speed = flight_speed         # Unique to FlyingHero: Speed of flight
    
    # Overriding the save_the_day method to include flying
    def save_the_day(self):
        super().save_the_day()  # Call the parent method to keep it
        print(f"{self.name} is flying at {self.flight_speed} mph to stop the villain!")

# Create objects (superheroes)
hero1 = Superhero("Captain Justice", "Super Strength", "Metropolis")
hero2 = Superhero("Sky Avenger", "Flight", "SkyCity")
hero3 = FlyingHero("Air Defender", "Flight", "CloudCity", 600)

# Calling the method to show what they do
hero1.save_the_day()
hero2.save_the_day()
hero3.save_the_day()
