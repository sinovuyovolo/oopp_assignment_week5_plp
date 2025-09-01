# Define the Superhero class
class Superhero:
    def __init__(self, name, superpower, city):
        self.name = name            # Attribute: Name of the superhero
        self.superpower = superpower  # Attribute: Superpower of the superhero
        self.city = city            # Attribute: City where the superhero lives

    # The superhero saves the day
    def save_the_day(self):
        print(f"{self.name} is using {self.superpower} to save the day in {self.city}!")

#FlyingHero class, from Superhero.
class FlyingHero(Superhero):
    def __init__(self, name, superpower, city, flight_speed):
        super().__init__(name, superpower, city)  
        self.flight_speed = flight_speed         
    
    def save_the_day(self):
        super().save_the_day()  
        print(f"{self.name} is flying at {self.flight_speed} mph to stop the villain!")

# Create superheroes
hero1 = Superhero("Captain Justice", "Super Strength", "Metropolis")
hero2 = Superhero("Sky Avenger", "Flight", "SkyCity")
hero3 = FlyingHero("Air Defender", "Flight", "CloudCity", 600)

# Calling the method to show what they do
hero1.save_the_day()
hero2.save_the_day()
hero3.save_the_day()
