aliens = 2
peopleOnEarth = 7400000000
password = "ALIENS"
print("Quickly! Aliens are invading the planet.")
print("You need to activate the global defence platforms.")
print("Hope you know the password, for Earth's sake...")
print()
print("---------------------------------------------------")
print("       WELCOME TO THE GLOBAL DEFENSE NETWORK       ")
print("---------------------------------------------------")
print()
guess = input("Please enter the password: ").upper()
while guess != password:
    print()
    print("INCORRECT PASSWORD.")
    print()
    aliens = aliens ** 2
    print("There are", aliens, "aliens now on Earth.")
    if aliens > peopleOnEarth:
        break
    print()
    print("Try again! Password hint: the things that are attacking us.")
    print()
    guess = input("Quick! Please enter the password: ").upper()
if aliens > peopleOnEarth:
    print("Noooooo! The aliens have outnumbered us. All is lost.")
else:
    print("Hooray! We won the fight and the world is saved!")