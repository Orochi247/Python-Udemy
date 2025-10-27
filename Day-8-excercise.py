#love calculator
true_list = ["t", "r", "u", "e"]
love_list = ["l", "o", "v", "e"]

def calculate_love_score(name1, name2):
    name1_list = list(name1.lower())
    name2_list = list(name2.lower())
    name1_score = 0
    name2_score = 0
    for check in range(len(name1_list)):
        if name1_list[check] in true_list:
            name1_score += 1
        if name1_list[check] in love_list:
            name2_score += 1
    print(name1_score)
    print(name2_score)
    print(name1_list)
    
calculate_love_score("Kanye West", "Kim Kardashian")

#need to work on this again,INCOMPLETE
#need to combine both name and then do the iterations