def solution(id_list, report, k):
    answer = []
    user_id = {idStr : [] for idStr in id_list}
    report_id = {idStr : 0 for idStr in id_list}
    
    for r in report:
        user, report_user = r.split()
        if report_user in user_id[user]:
            continue
        elif report_user not in user_id[user]:
            user_id[user].append(report_user)
            report_id[report_user] += 1
    
    reported = []
    for user, count in report_id.items():
        if count >= k:
            reported.append(user)
    
    send_id = {idStr : 0 for idStr in id_list}
    for user, report_user_list in user_id.items():
        for report_user in report_user_list:
            if report_user in reported:
                send_id[user] += 1
    
    for send in send_id.values():
        answer.append(send)
    
    return answer