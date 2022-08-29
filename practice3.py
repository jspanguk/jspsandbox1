class Stats():
    
    def __init__(self, num):
        
        self.num = num
    
    def list_gen(self):
        
        inputed=list()
        for x in range(self.num):
            input_list = list()
            while True:
                a = int(  input(str(x+1)+"반 학생 점수를 정수로 입력하세요(0을 입력시 바로 0을 무시하고 총합과 평균 계산함): ")  )
                if a == 0:
                    break
                input_list.append(a)
            inputed.append(input_list)
            
        return inputed

    
    def list_sum(self, input):
        sum_list=list()
        for x in input:
            sum = 0
            count=0
            for y in x:
                count = count + 1   
                sum = sum + y
            sum_list.append((sum, count))
        return sum_list

    
def main():
    i = int(input("몇 번 실행하길 원하는지 정수로 입력해주세요: "))
    stat = Stats(i)
    x = stat.list_gen()
    y = stat.list_sum(x)
    count=0
    for z in y:
        
        print(str(count+1)+"반")
        print("점수 총합 :"+str(z[0]))
        print("평균 점수 :"+str(z[0]/z[1]))
        
        count=count+1
    
if __name__ == '__main__':
    main()