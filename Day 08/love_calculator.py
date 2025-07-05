def calculate_love_score(name1, name2):
    name = (name1 + name2).lower()
    score1 = 0
    score2 = 0
    for i in name:
        if i in "true":
            score1 += 1
    for i in name:
        if i in "love":
            score2 += 1
    print(int(str(score1) + str(score2)))

calculate_love_score("Romeo", "Juliet")

