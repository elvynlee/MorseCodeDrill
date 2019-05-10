"""Morse code practices

"""
from random import shuffle

#--------------------------------------------------------------------------------
dic1 = {'e':'.', 'i':'..', 'a':'.-', 's':'...', 'u':'..-', 'r':'.-.', 'w':'.--', 
        't':'-', 'm':'--', 'n':'-.', 'o':'---', 'g':'--.', 'k':'-.-', 'd':'-..', 
        'j':'.---', 'p':'.--.', 'l':'.-..', 'f':'..-.', 
        'b':'-...', 'x':'-..-', 'y':'-.--', 'q':'--.-', 
        'v':'...-', 'c':'-.-.', 'z':'--..', 'h':'....', 
        '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-', 
        '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', 
        ',':'--..--', '.':'.-.-.-', '\'':'.----.', '!':'-.-.--', '-':'-....-', 
        '"':'.-..-.', '?':'..--..', 
        }

dic2 = {v:k for k, v in dic1.items()}

def en_to_morse(sen):
    result = []
    word_list = sen.rstrip().split(' ')
    for word in word_list:
        morse_word = []
        for chr in word:
            if chr == '’': chr = "'"
            morse_word.append(dic1[chr.lower()]+' ')
        result.append(''.join(morse_word))
    return '/ '.join(result)



def morse_to_en(sen):
    result = []
    word_list = sen.rstrip().split(' / ')
    for word in word_list:
        chr_list = word.split(' ')
        en_word = []
        for chr in chr_list:            
            en_word.append(dic2[chr])
        result.append(''.join(en_word))
    return ' '.join(result)

def check_trans(sys_trans, pla_trans):
    correct = 1
    if sys_trans[0] in '.-':
        sys_word_list = sys_trans.split(' / ')
        pla_word_list = pla_trans.split(' / ')
    else:
        sys_word_list = sys_trans.split(' ')
        pla_word_list = pla_trans.split(' ')
    i = 0
    while i < len(sys_word_list) and i < len(pla_word_list):
        if sys_word_list[i] != pla_word_list[i]:
            pla_word_list[i] = '[' + pla_word_list[i] + ']'
            correct = 0
        i += 1
    if correct:
        return "correct, well done."
    return ' / '.join(pla_word_list) if sys_trans[0] in '.-' else ' '.join(pla_word_list)


def main():
    with open('sentences.txt', 'r', encoding='UTF-8') as f:
        stns = f.readlines()
    rnd_line_num = [i*2 for i in range(len(stns)//2)]
    shuffle(rnd_line_num)
    
    
    while rnd_line_num:
        print("translate the sentence to Morse code: ")
        print(stns[rnd_line_num[0]])
        pla_trans_1 = input("your translation(or input 's' to skip): \n")
        if pla_trans_1 == 's':
            print("ok, let's skip this one!-----\n")
        else:
            sys_trans_1 = en_to_morse(stns[rnd_line_num[0]])
            print(sys_trans_1)

            print(check_trans(sys_trans_1, pla_trans_1))


        
        mc_stns = en_to_morse(stns[rnd_line_num[1]])
        print(stns[rnd_line_num[1]])
        print("translate the sentence to English: ")
        print( mc_stns)
        pla_trans_2 = input("your translation(or input 's' to skip): \n")
        if pla_trans_2 == 's':
            print("skipped!")
        else:
            sys_trans_2 = morse_to_en(mc_stns)
            print(sys_trans_2)

            print(check_trans(sys_trans_2, pla_trans_2))
        
        del rnd_line_num[0]
        del rnd_line_num[1]
        tr_ag = input("try again?(y=yes, other=quit): ")
        if tr_ag != 'y':
            break
    else:
        print("oops, run out of sentences...pls add more.")
       

if __name__ == '__main__':
    main()

