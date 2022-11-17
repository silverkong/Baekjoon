import math

def solution(fees, records):
    answer = []
    carRecords = {}
    
    for record in records:
        time, carNum, IO = record.split()
        if carNum in carRecords:
            carRecords[carNum] += [[time, IO]]
        else:
            carRecords[carNum] = [[time, IO]]
    
    result = {}
    for key, value in carRecords.items():
        inTime = -1
        outTime = 0
        for timeCheck in value:
            if timeCheck[1] == 'IN':
                HH, MM = timeCheck[0].split(':')
                inTime = (int(HH) * 60) + int(MM)
            else:
                HH, MM = timeCheck[0].split(':')
                outTime = (int(HH) * 60) + int(MM)
                if key in result:
                    result[key] += outTime - inTime
                    inTime, outTime = -1, 0
                else:
                    result[key] = outTime - inTime
                    inTime, outTime = -1, 0
        if inTime >= 0 and outTime == 0:
            outTime = (23 * 60) + 59
            if key in result:
                result[key] += outTime - inTime
            else:
                result[key] = outTime - inTime
    
    result = dict(sorted(result.items()))
    
    for value in result.values():
        if value > fees[0]:
            fee = fees[1] + (math.ceil((value - fees[0]) / fees[2])) * fees[3]
            answer.append(fee)
        else:
            answer.append(fees[1])
    
    return answer