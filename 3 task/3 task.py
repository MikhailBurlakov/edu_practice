n, k = map(int, input().split())
snow_amounts = [0] * n
for _ in range(k):
    line = list(map(int, input().split()))
    event_type = line[0]
    if event_type == 1:
        street_index = line[1]
        snow_amount = line[2]
        snow_amounts[street_index - 1] += snow_amount
    elif event_type == 2:
        start_index = line[1]
        end_index = line[2]
        total_snow_in_range = 0
        for i in range(start_index - 1, end_index):
            total_snow_in_range += snow_amounts[i]
        print(total_snow_in_range)