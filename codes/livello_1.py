cars = [[1,1,2,1,1],[2,1,4,2,4],[3,3,1,4,1],[4,5,6,5,5],[5,4,3,4,2],[6,5,1,6,1],[7,5,2,6,2]]  
trucks = [[8,3,4,4,4,5,4]] 
vehicle, move_type, nCells = problemDefinition(cars,trucks)
if vehicle==0:
    print("No plan found")
else:
    print(f"The vehicle_{vehicle} is moving {move_type} of {nCells} number of cells")
