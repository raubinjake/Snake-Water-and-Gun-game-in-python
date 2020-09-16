import random
counter=1
system_point=0
human_point=0
while(counter<=10):
    #here s for snake ,w for water and g for gun stored in list
    game_list=["s","w","g"]
    comp_choice=random.choice(game_list)
    human_choice=input("Enter Snake for s, Water for w, Gun for g = ")
    if comp_choice==human_choice:
        print("Game tie ! ")
        print("Computer_point= ",system_point)
        print("Your point= ",human_point)
        counter=counter+1
    #if human input snake then 
    elif human_choice=='s' and comp_choice=='g':
        print("computer is winner !")
        counter=counter+1
        system_point=system_point+1
        print("Your point= ",human_point)
        print("Computer point= ",system_point)
    elif human_choice == 's' and comp_choice == 'w':
        print("You are  winner !")
        human_point = human_point + 1
        counter = counter + 1
        print("Your point= ", human_point)
        print("Computer point= ", system_point)
    #if human input g that means Gun
    elif human_choice=='g' and comp_choice=='s':
        print("You are winner !")
        human_point = human_point + 1
        counter=counter+1
        print("Your point= ",human_point)
        print("Computer point= ",system_point)
    elif human_choice=='g' and comp_choice=='w':
        print("computer is winner !")
        counter=counter+1
        system_point=system_point+1
        print("Your point= ",human_point)
        print("Computer point= ",system_point)
    #if human input w that means water then
    elif human_choice=='w' and comp_choice=='s':
        print("computer is winner !")
        counter=counter+1
        system_point=system_point+1
        print("Your point= ",human_point)
        print("Computer point= ",system_point)
    elif human_choice=='w' and comp_choice=='g':
        print("You are winner !")
        human_point = human_point + 1
        counter=counter+1
        print("Your point= ",human_point)
        print("Computer point= ",system_point)
    else:
        print("Wrong input !")
print("Game over !")