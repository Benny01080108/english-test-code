import random

words_bank = {}

with open('/Users/benny/Downloads/words.txt', 'r', encoding='utf-8') as file:
    for i in file:
        eng, ch = i.strip().split(',')
        words_bank[ch] = eng


def start_test():
    global score
    global wrong
    for i in range(5):
        n = random.randint(1, 2)
        if n == 1:#中翻英
            answer = input('the meaning of %s is: ' % questions_c[i])

            if answer == words_bank[questions_c[i]]:
                print('correct')
                score += 1
            else:
                print('incorrect')
                wrong.append((questions_c[i], words_bank[questions_c[i]]))

            print('-----------------')

        if n == 2:#英翻中
            answer = input('the meaning of %s is: ' % questions_e[i])
            
            for ch, eng in words_bank.items():
                if eng == questions_e[i]:
                    key = ch

            if answer == key:
                print('correct')
                score += 1
            else:
                print('incorrect')
                wrong.append((key, questions_e[i]))
                
            print('-----------------')

    return 
def do_wrong_questions():
    global wrong
    for ch, eng in wrong:
        n = random.randint(1, 2)

        if n == 1:#中翻英
            answer = input('the meaning of %s is: ' % ch)
            correct = eng

            if answer == correct:
                print('correct')
            else:
                print('incorrect')

            print('-----------------')

        else:# 英翻中
            answer = input('the meaning of %s is: ' % eng)
            correct = ch

            if answer == correct:
                print('correct')
            else:
                print('incorrect')

            print('-----------------')
    return

#main
s=[]
while(1):
    print('\n===English word test===')
    print('1.Start the test')
    print('2.View words')
    print('3.View your score')
    print('4.Quit\n')
    choi = input('please choose:')
    if choi == '1':###考試
        c = list(words_bank.keys())
        questions_c = random.sample(c, 5)
        
        e = list(words_bank.values())
        questions_e = random.sample(e, 5)
        score = 0
        wrong = []
        
        start_test()
 
        
        final_score = score * 20
        s.append(final_score)
        print('test over')
        print('your score is %d' % final_score)

        #錯題考試
        num = len(wrong)
        if num != 0:
            while(1):
                print('\n1.Review wrong questions')
                print('2.View wrong words')
                print('3.Back to menu\n')
                choi2 = input('please choose:')
                if choi2 == '1':
                    do_wrong_questions()

                elif choi2 == '2':
                    print('\nwrong words:')

                    for i in range(num):
                        print('%s,%s' % (wrong[i][0], wrong[i][1]))

                elif choi2 == '3':
                    break

                else:
                    print('enter wrong, please enter again')
    
    elif choi == '2':###看單字
        print('\nview words')
        for ch, eng in words_bank.items():
            print('%s,%s' % (ch, eng))

    elif choi=='3':###看成績
        count = len(s)
        total = 0
        if count == 0:
            print('you need to do the test first')
        else:
            for i in range(count):
                print('%d. your score:%d' % (i+1, s[i]))
                total += s[i]

            aver = total / count
            Max=max(s)
            Min=min(s)
            print('Highest score:%d'%Max)
            print('Lowest score:%d'%Min)
            print('your average score:%.2f'%aver)
        
    elif choi=='4':###離開
        print('\nQuit')
        break              
  
    else:
        print('enter wrong, please enter again')



        
    


        

        
