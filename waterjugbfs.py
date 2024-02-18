from collections import deque
def bfs(capacities,target):
    visited=set()
    queue=deque([((0,0),[])])
    while queue:
        (x,y),path=queue.popleft()
        if (x,y)==target:
            return path+[(x,y)]
        visited.add((x,y))

        #empty jug_1
        if (0,y) not in visited:
            queue.append(((0,y),path+[(x,y)]))

        #empty jug_2
        if (x,0) not in visited:
            queue.append(((x,0),path+[(x,y)]))
        
        #fill jug_1
        if (capacities[0],y) not in visited:
            queue.append(((capacities[0],y),path+[(x,y)]))
        
        #fill jug_2
        if (x,capacities[1]) not in visited:
            queue.append(((x,capacities[1]),path+[(x,y)]))
        
        #pour from jug1 to jug2
        pour_amout=min(x,capacities[1]-y)
        if (x-pour_amout,y+pour_amout) not in visited:
            queue.append(((x-pour_amout,y+pour_amout),path+[(x,y)]))

        #pour from jug2 to jug1
        pour_amount=min(capacities[0]-x,y)
        if (x+pour_amount,y-pour_amount) not in visited:
            queue.append(((x+pour_amount,y-pour_amount),path+[(x,y)])) 
    return None
def user_input():
    jug_1=int(input("Enter capacity of jug 1:"))
    jug_2=int(input("Enter capacity of jug 2:"))
    target_jug1=int(input("Enter target capacity of jug 1:"))
    target_jug2=int(input("Enter target capacity of jug 2:"))
    return (jug_1,jug_2),(target_jug1,target_jug2)
capacities,target=user_input()
solution=bfs(capacities,target)
if solution:
    print("solution found")
    for state in solution:
        print(state)
else:
    print("no solution exists!")
