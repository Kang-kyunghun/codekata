#다리를 지나는 트럭
def solution(bridge_length, weight, truck_weights):
    len_truck_weights = len(truck_weights)
    on_bridge = []
    final = []
    remained_weight = weight
    total_time = 0
    time_list = []
    
    while True:
        if truck_weights:
            start_truck_weight = truck_weights[0]
            if start_truck_weight <= remained_weight:
                remained_weight -= truck_weights[0]
                on_bridge.append(truck_weights.pop(0))
                time_list.append(1)
        if time_list:
            if time_list[0] > bridge_length:
                remained_weight += on_bridge[0]
                final.append(on_bridge.pop(0))
                time_list.pop(0)
                if truck_weights:
                    start_truck_weight = truck_weights[0]
                    if start_truck_weight <= remained_weight:
                        remained_weight -= truck_weights[0]
                        on_bridge.append(truck_weights.pop(0))
                        time_list.append(1)
        
        if len(final) == len_truck_weights:
            break
        for index in range(len(time_list)):
            time_list[index] += 1
        total_time += 1
        print(final, on_bridge, truck_weights, total_time)

    answer = total_time + 1
    return answer

bridge_length = 2	
weight	= 10
truck_weights = [7, 4, 5, 6]
# return 8

print(solution(bridge_length, weight, truck_weights))
