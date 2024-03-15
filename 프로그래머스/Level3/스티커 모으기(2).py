def solution(stickers):
    if len(stickers) <= 3: #dp는 길이가 3이상에서만 가능. 
        return max(stickers)
    
    answer = 0
    for start in [0,1]:
        dp = [0]*(len(stickers)-1)
        if start == 0:
            dp[0], dp[1] = stickers[0], max(stickers[0],stickers[1])
            for i in range(2, len(stickers)-1): # 길이는 1이상 100,000이하.
                dp[i] = max(dp[i-2]+stickers[i], dp[i-1])

        elif start == 1:
            stickers = stickers[1:] + [stickers[0]]
            dp[0], dp[1] = stickers[0], max(stickers[0],stickers[1])
            for i in range(2, len(stickers)-1):
                dp[i] = max(dp[i-2]+stickers[i], dp[i-1])
        
        answer = max(answer, dp[-1])

    return answer