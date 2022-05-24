print("Welcome to squid game!")
name = input("What is your name? ")
age = int(input("Please enter your age "))
print("Hello", name, "you are", age, "years old.")
health = 10

if age >= 18:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("You are starting with", health, "health")
        print("May the games begin!")

        left_or_right = input("First choice...left or right (left/right)? ")
        if left_or_right == "left":

            ans = input("Nice you follow the path and reach a lake... Do you swim across or go around (across/around)? ")
            if ans == "around":
                print("You went around and reached the other side of the lake kudos.")
            elif ans == "across":
                print("You managed to get across but were bit by a pirana and lost 5 health.")
                health -= 5            

            ans = input("You notice a house and a river. Which do you go to (river/house)? ")
            if ans == "house":
                print("The house contains a bomb that blasts and you lose 5 health.")
                health -= 5

                if health <= 0:
                    print("You now have 0 health and you lost the game...")
                else:
                    print("You have survived you win....!")
            else:
                print("Oops you fell in the river and lost...")
        else:
            print("You fell in a ditch and lost the game...")
    else:
        print("Godspeed then Cya...")
else:
    print("You are not old enough to play...")



