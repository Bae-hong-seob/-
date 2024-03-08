from collections import defaultdict

def solution(records):
    result = []
    id2name = defaultdict(str)
    
    for record in records:
        if record.split()[0] == 'Leave':
            action, user_id = record.split()
        else:
            action, user_id, user_name = record.split()
            id2name[user_id] = user_name
            
        if action == 'Change': #이름 변경
            id2name[user_id] = user_name
            
        else: #입장 혹은 퇴장
            result.append([user_id, action])

    return [f'{id2name[user_id]}님이 들어왔습니다.' if action=='Enter' else f'{id2name[user_id]}님이 나갔습니다.' for user_id, action in result]