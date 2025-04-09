#Yeh project ek weight conversion program hai jisme aap user ka Earth par weight lete hain aur phir
# calculate karte hain ke uska wazan kisi aur planet par kitna hoga — jaise Mars, Jupiter, Venus waghera.

# Dictionary to hold gravity constants
planet_gravity = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

# Get input from user
earth_weight = float(input("Enter a weight on Earth: "))
planet = input("Enter a planet: ")

# Get gravity factor for that planet
gravity_factor = planet_gravity[planet]

# Calculate weight on that planet
planet_weight = round(earth_weight * gravity_factor, 2)

# Print result
print(f"The equivalent weight on {planet}: {planet_weight}")
