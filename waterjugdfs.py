def dfs(capacities,target,current_state =(0,0),path =[]):
    if current_state==target:
        return path+[current_state]
    visited.add(current_state)

    #empty jug1
    if (0,current_state[1]) not in visited:
        result=dfs(capacities,target,(0,current_state[1]),path+[current_state])
        return result

    #empty jug2
    if (current_state[0],0) not in visited:
        result=dfs(capacities,target,(current_state[0],0),path+[current_state])
        return result
    
    #fill jug1
    if (capacities[0],current_state[1]) not in visited:
        result=dfs(capacities,target,(capacities[0],current_state[1]),path+[current_state])
        return result

    #fill jug2
    if (current_state[0],capacities[1]) not in visited:
        result=dfs(capacities,target,(current_state[0],capacities[1]),path+[current_state])
        return result
    #pour from jud1 to jug2
    pour_amount=min(current_state[0],capacities[1] - current_state[1])
    if (current_state[0]-pour_amount,current_state[1]+pour_amount) not in visited:
        result=dfs(capacities,target,(current_state[0]-pour_amount,current_state[1]+pour_amount),path+[current_state])
        return result
    #pour from jug2 to jug1
    pour_amount=min(current_state[1],capacities[0]-current_state[0])
    if (current_state[0]+pour_amount,current_state[1]-pour_amount) not in visited:
        result=dfs(capacities,target,(current_state[0]+pour_amount,current_state[1]-pour_amount),path+[current_state])
        return result
    
def user_input():
    jug_1=int(input("Enter capacity of jug 1:"))
    jug_2=int(input("Enter capacity of jug 2:"))
    target_jug1=int(input("Enter target capacity of jug1:"))
    target_jug2=int(input("Enter target capacity of jug2:"))
    return (jug_1,jug_2),(target_jug1,target_jug2)

capacities,target =user_input()
visited=set()
solution=dfs(capacities,target)
if solution:
    print("solution fould:")
    for state in solution:
        print(state)
else:
    print("no solution exists!")