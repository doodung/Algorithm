def solution(bridge_length, weight, truck_weights):
    time = 0
    ing_truck = [0]*bridge_length
    while ing_truck:
        time += 1
        ing_truck.pop(0)
        if truck_weights:
            if sum(ing_truck)+truck_weights[0] <= weight:
                ing_truck.append(truck_weights.pop(0))
            else:
                ing_truck.append(0)
    return time