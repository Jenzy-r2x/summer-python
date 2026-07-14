fighter = "warrior"
key = True
energy = 35

if fighter == "warrior" and key == True:
    print("congrats you are allowed to open the door.")
elif energy > 30:
    print("you can open the door,energy is sufficient")
elif energy < 30:
    print("you now have rested for enough time to open the door")
elif energy == 0 :
    print("you should go back to your cave to rest")