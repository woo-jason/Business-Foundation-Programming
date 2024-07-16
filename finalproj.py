import random

n_tries = 1000
# Lists to store results from stay and switch strategy
stay_results = []
switch_results = []
switchstay_results = []

for i in range(n_tries):
    doors = ['money', 'none', 'none', 'none']
    random.shuffle(doors)
    #print(doors)  
    # prints arrangement of doors

    chosen_index = random.randint(0,3)
    #print(chosen_index) 
    # prints index of chosen door

    stay_door = doors.pop(chosen_index)
    #print(stay_door)
    doors.remove('none')
    #print(doors)

    second_doors = doors
    #print(second_doors)
    second_chosen_index = random.randint(0,1)
    #print(second_chosen_index)
    
    second_stay_door = second_doors.pop(second_chosen_index)
    #print(second_stay_door)

    switch_door = doors[0]
    #print(switch_door)

    stay_results.append(stay_door)
    switch_results.append(switch_door)
    switchstay_results.append(second_stay_door)

    
a = int(switch_results.count('money'))
b = int(switchstay_results.count('money'))
sum = a + b
# print(sum)

print('Probability of winning if user doesnt switch doors is ' + str((stay_results.count('money')/n_tries)*100) + '%')
print('Probability of winning if user does switch doors is ' + str((sum/n_tries)*100) + '%')



