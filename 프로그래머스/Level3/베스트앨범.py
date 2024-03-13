from collections import defaultdict

def solution(genres, plays):
    playlist_per_genres = defaultdict(list)
    play_number_per_genres = defaultdict(int)
    
    answer = []

    for idx, (genre, play) in enumerate(zip(genres, plays)): # 최대 10,000
        playlist_per_genres[genre].append([play, idx])
        play_number_per_genres[genre]+=play
    
    playlist = []
    for key, value in play_number_per_genres.items(): #최대 100
        playlist.append([value, key])
    playlist.sort(reverse=True)
    playlist = [genre for number, genre in playlist]
    
    answer = []
    for genre in playlist:
        value = playlist_per_genres[genre]
        value.sort(key=lambda x:[-x[0], x[1]])
        for number, idx in value[:2]:
            answer.append(idx)
        
        
    
    return answer