
true_list = ["t", "r", "u", "e"]
love_list = ["l", "o", "v", "e"]

def calculate_love_score(name1, name2):
    name1_list = list(name1.lower()) + list(name2.lower())
    true_score = 0
    love_score = 0
    for check in range(len(name1_list)):
        if name1_list[check] in true_list:
            true_score += 1
        if name1_list[check] in love_list:
            love_score += 1
    print(f"{true_score}{love_score}")
    
calculate_love_score("Kanye West", "Kim Kardashian")

#done solved the problem