def master():
    print("The bathinator is booting up...")
    print("Bathinator is fully loaded")
    how_long = float(input("How many seconds has it been since you started the bath?"))
    best_adv = float(300) #seconds
    if how_long > best_adv:
        print("ALERT!!! STOP THE BATH!")
    else:
        print("Stop the bath in ", best_adv - how_long, "seconds")

    restart = input("Do you want to restart? y/n")
    if restart.lower() == "y":
        master()
    else:
        exit()

master()