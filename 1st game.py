print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("How old are you? "))
print("Hello", name, "you are", age, "years old")

health = 10

if age >= 18:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play!").lower()
    if wants_to_play == "yes":
        print("Let's  play!")
        print("You are stating with", health, "health")

        left_or_right = input("First choice.... Left or Right (left/right)?")
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake...Do you swim across or go around (across/around)? ")
            if ans == "around":
                print("You went around and reached the other side of the lake")




            elif ans == "around":
                print("You managed to get across, but were bit by a fish and lost 5 health.")
                health -= 5
            ans = input("You notice a house and a river. Where would you like to go(river/house)? ")
            if ans == "house":
                print("You go tothe house and are greeted by the owner... He doesn't like you and you lose 5 health")
                health -= 5

            else:
                print("You fell in the river and lost...")



        else:
            print("You fell down and lost... :(")




    else:
        print("Cya...")







elif age >= 14:
    print("You can play with supervision")
else:
    print("You are not old enough to play...!")






"""
    wants_to_play = input("Do you want to play!").lower()
    if wants_to_play == "yes":
        print("You are stating with", health,"health")
        print("Let's  play!")

        left_or_right = input("First choice.... Left or Right (left/right)?")
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake...Do you swim across or go around")

"""