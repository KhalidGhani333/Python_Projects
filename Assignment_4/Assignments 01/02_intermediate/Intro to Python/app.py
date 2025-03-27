

# every planet has different gravity
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14
EARTH_GRAVITY = 1.0

#  function for mars
def mars_weight_calculator():
    
    earth_weight = float(input("Enter a weight on Earth: "))

        # calculate weight on mars
    mars_weight = round(earth_weight * MARS_GRAVITY , 2)
    print(f"The equivalent weight on Mars is: {mars_weight}")

 # other planet funtion 
def planetary_weight_calculator():
    
    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet (Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune): ")
 
    # assign gravity to variable based on user input for calculate weight on planet
    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    elif planet == "Neptune":
        gravity_constant = NEPTUNE_GRAVITY
    else:
        print("Invalid planet! Please enter a valid planet name.")
        return

    planetary_weight = round(earth_weight * gravity_constant , 2)
        
    print(f"The equivalent weight on {planet} is: {planetary_weight}")


def main():
    print("=== Planetary Weight Calculator ===")
    print("1. Calculate Mars Weight Only")
    print("2. Calculate Weight on any Planet")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        mars_weight_calculator()
    elif choice == "2":
        planetary_weight_calculator()
    else:
        print("Invalid choice! Please restart the program.")

main()




