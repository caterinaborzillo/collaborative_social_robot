with OneshotPlanner(name='fast-downward') as planner: #fast-downward pyperplan tamer enhsp
    assert planner.supports(problem_kind)
    result = planner.solve(problem)
    if result.status == up.engines.PlanGenerationResultStatus.SOLVED_SATISFICING:
        print("Pyperplan returned: %s" % result.plan)
        completePlan = (str(result.plan)[1:-1]) 
        movesPlan = completePlan.split(', move_') 
        move = movesPlan[0].split("(")[0][5:] 
        vehicle = movesPlan[0].split("vehicle_")[1].split(",")[0] 
        n_cells = 1 
        for m in movesPlan[1:]:
            v = m.split("vehicle_")[1].split(",")[0]
            if move in m and vehicle==v:
                n_cells+=1
            if move not in m or vehicle!=v:
                break
        if "forward" in move:
            return vehicle, "forward", n_cells
        else:
            return vehicle, "backward", n_cells
    else:
        noPlan = "No plan found"
        return 0,noPlan,0
