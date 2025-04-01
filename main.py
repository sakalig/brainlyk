import sys

titles = """
ßɾαιɳɬყƙ
"""
_menu = ["PLAY", "ABOUT", "QUIT"]
print(titles)
print("Welcome to Brainlyk\n")

score = 0
questions = [
    {"1": "What is the capital of Italy?", "answer": "rome"},
    {"2": "From what language are the words 'a la carte' being referenced from?", "answer": "french"},
    {"3": "From which continent is Bosnia from?", "answer": "europe"},
    {"4": "Name the country north of England", "answer": "scotland"},
    {"5": "Which prominent sea is south of Spain? (one word)", "answer": "mediterranean"},
    {"6": "What was the first name of France's first emperor?", "answer": "napoleon"},
    {"7": "What is the country between the border of France and Spain?", "answer": "andorra"},
    {"8": "Is germany landlocked? (one word)", "answer": "no"},
    {"9": "How many countries does the Rhine flow through? (one word, no digits)", "answer": "six"},
    {"10": "Which year did the Berlin wall get demolished? (digits only)", "answer": "1989"},
]

failed = []

for a in range(len(questions)):
    print(questions[a][str(a+1)])
    _input = str(sys.stdin.readline().lower()).strip()

    if _input == questions[a]["answer"]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
        failed.append(questions[a])


def get_titles():
    return titles

completed_badge = """

//                                                                                                                                                                 
//                                                                                                                                                                 
//    ,----..                                                         ___                    ,--,                  ___                                             
//   /   /   \                                                      ,--.'|_                ,--.'|                ,--.'|_    ,--,                                   
//  |   :     :  ,---.        ,---,              __  ,-.            |  | :,'          ,--, |  | :                |  | :,' ,--.'|    ,---.        ,---,             
//  .   |  ;. / '   ,'\   ,-+-. /  |  ,----._,.,' ,'/ /|            :  : ' :        ,'_ /| :  : '                :  : ' : |  |,    '   ,'\   ,-+-. /  | .--.--.    
//  .   ; /--` /   /   | ,--.'|'   | /   /  ' /'  | |' | ,--.--.  .;__,'  /    .--. |  | : |  ' |     ,--.--.  .;__,'  /  `--'_   /   /   | ,--.'|'   |/  /    '   
//  ;   | ;   .   ; ,. :|   |  ,"' ||   :     ||  |   ,'/       \ |  |   |   ,'_ /| :  . | '  | |    /       \ |  |   |   ,' ,'| .   ; ,. :|   |  ,"' |  :  /`./   
//  |   : |   '   | |: :|   | /  | ||   | .\  .'  :  / .--.  .-. |:__,'| :   |  ' | |  . . |  | :   .--.  .-. |:__,'| :   '  | | '   | |: :|   | /  | |  :  ;_     
//  .   | '___'   | .; :|   | |  | |.   ; ';  ||  | '   \__\/: . .  '  : |__ |  | ' |  | | '  : |__  \__\/: . .  '  : |__ |  | : '   | .; :|   | |  | |\  \    `.  
//  '   ; : .'|   :    ||   | |  |/ '   .   . |;  : |   ," .--.; |  |  | '.'|:  | : ;  ; | |  | '.'| ," .--.; |  |  | '.'|'  : |_|   :    ||   | |  |/  `----.   \ 
//  '   | '/  :\   \  / |   | |--'   `---`-'| ||  , ;  /  /  ,.  |  ;  :    ;'  :  `--'   \;  :    ;/  /  ,.  |  ;  :    ;|  | '.'\   \  / |   | |--'  /  /`--'  / 
//  |   :    /  `----'  |   |/       .'__/\_: | ---'  ;  :   .'   \ |  ,   / :  ,      .-./|  ,   /;  :   .'   \ |  ,   / ;  :    ;`----'  |   |/     '--'.     /  
//   \   \ .'           '---'        |   :    :       |  ,     .-./  ---`-'   `--`----'     ---`-' |  ,     .-./  ---`-'  |  ,   /         '---'        `--'---'   
//    `---`                           \   \  /         `--`---'                                     `--`---'               ---`-'                                  
//                                     `--`-'                                                                                                                      

"""

perfect_score_badge = """

//                           
//                           
//       ,---,    ,----..    
//    ,`--.' |   /   /   \   
//   /    /  :  /   .     :  
//  :    |.' ' .   /   ;.  \ 
//  `----':  |.   ;   /  ` ; 
//     '   ' ;;   |  ; \ ; | 
//     |   | ||   :  | ; | ' 
//     '   : ;.   |  ' ' ' : 
//     |   | ''   ;  \; /  | 
//     '   : | \   \  ',  /  
//     ;   |.'  ;   :    /   
//     '---'     \   \ .'    
//                `---`      
//                           

"""
print(completed_badge)
print("\n\nYou've beat the quest\nHere are your stats:\n\n")
if score == len(questions):
    print("You got a PERFECT score!")
    print(perfect_score_badge)
else:
    print("Correct: " + score)