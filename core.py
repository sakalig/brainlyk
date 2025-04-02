import sys

def brainlyk_core():
    print(get_titles())
    _menu = ["PLAY", "ABOUT", "QUIT"]
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

    print(get_complete_badge())
    print("\n\nYou've beat the quest\nHere are your stats:\n\n")
    if score == len(questions):
        print("You got a PERFECT score!")
        print(get_perfect_score_badge())
    else:
        print("Correct: " + score)


def get_titles():
    titles = """
    ßɾαιɳɬყƙ
    Welcome to Brainlyk\n
    """
    return titles

def get_complete_badge():
    return """

    //                                                                                                                                                                 
    //                                                                                                                                                                 
    //    ,----..                                                         ___                
    //   /   /   \                                                      ,--.'|_              
    //  |   :     :  ,---.        ,---,              __  ,-.            |  | :,'             
    //  .   |  ;. / '   ,'\   ,-+-. /  |  ,----._,.,' ,'/ /|            :  : ' :  .--.--.    
    //  .   ; /--` /   /   | ,--.'|'   | /   /  ' /'  | |' | ,--.--.  .;__,'  /  /  /    '   
    //  ;   | ;   .   ; ,. :|   |  ,"' ||   :     ||  |   ,'/       \ |  |   |     :  /`./   
    //  |   : |   '   | |: :|   | /  | ||   | .\  .'  :  / .--.  .-. |:__,'| :     :  ;_     
    //  .   | '___'   | .; :|   | |  | |.   ; ';  ||  | '   \__\/: . .  '  : |__ \  \    `.  
    //  '   ; : .'|   :    ||   | |  |/ '   .   . |;  : |   ," .--.; |  |  | '.'| `----.   \ 
    //  '   | '/  :\   \  / |   | |--'   `---`-'| ||  , ;  /  /  ,.  |  ;  :    ;/  /`--'  / 
    //  |   :    /  `----'  |   |/       .'__/\_: | ---'  ;  :   .'   \ |  ,   / --'.     /  
    //   \   \ .'           '---'        |   :    :       |  ,     .-./  ---`-'   `--'---'   
    //    `---`                           \   \  /         `--`---'                          
    //                                     `--`-'                                            

    """

def get_perfect_score_badge():
    return """

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

if __name__ == "__main__":
    brainlyk_core()