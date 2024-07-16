import random

n_tries = 1000
# Lists to store results from stay and switch strategy
stay_results = []
switch_results = []

for i in range(n_tries):
    doors = ['money', 'none', 'none']
    random.shuffle(doors)
    # print(doors)  
    # prints arrangement of doors

    chosen_index = random.randint(0,2)
    #print(chosen_index) 
    # prints index of chosen door

    stay_door = doors.pop(chosen_index)
    #print(stay_door)
    doors.remove('none')

    switch_door = doors[0]
    #print(switch_door)

    stay_results.append(stay_door)
    switch_results.append(switch_door)

print('Probability of winning if user doesnt switch doors is ' + str(stay_results.count('money')/n_tries))
print('Probability of winning if user does switch doors is ' + str(switch_results.count('money')/n_tries))

