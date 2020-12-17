def get_start_time(schedules, duration):
    # Sort into time in mins, iterate through, test if all free
    for i in range(len(schedules)):
        for j in range(len(schedules[i])):
            for k in range(len(schedules[i][j])):
                schedules[i][j][k] = int(schedules[i][j][k][:2]) * 60 + int(schedules[i][j][k][3:])
    potentialAns = []
    endTime = 0
    for i in range(len(schedules)):
        for j in range(len(schedules[i])):
            startTime = schedules[i][j][0]
            if startTime - endTime >= duration:
                potentialAns.append(endTime)
            endTime = schedules[i][j][1]

    endTime2 = 0
    for i in range(len(potentialAns)):
        success = 0
        for j in range(len(schedules)):
            endTime2 = 0
            for k in range(len(schedules[j])):
                startTime2 = schedules[j][k][0]
                if potentialAns[i] > endTime2 and potentialAns[i] + duration < startTime2:
                    print(potentialAns[i], endTime2, startTime2)  # TODO: REMOVE
                    success += 1
                endTime2 = schedules[j][k][1]

        if success >= 3:
            print(potentialAns[i])


print(get_start_time([
    [['09:00', '11:30'], ['13:30', '16:00'], ['16:00', '17:30'], ['17:45', '19:00']],
    [['09:15', '12:00'], ['14:00', '16:30'], ['17:00', '17:30']],
    [['11:30', '12:15'], ['15:00', '16:30'], ['17:45', '19:00']]
], 60))
