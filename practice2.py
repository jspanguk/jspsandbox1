def list_gen(): # input: empty / output: list of int
    score_list = list()
    while True:
        inputed = int(input("정수를 입력하세요. 반복문을 빠져나가시려면 '0'을 입력하세요. 그리고 엔터키를 누르세요: "))
        
        if inputed != 0:
            score_list.append(inputed)
        else:
            break
    return score_list

def avg_gen(score_list): # input: list of int / output: tuple of int
    sum = 0
    for x in score_list:
        sum = sum + x
    return (sum, len(score_list))

print(avg_gen(list_gen()))