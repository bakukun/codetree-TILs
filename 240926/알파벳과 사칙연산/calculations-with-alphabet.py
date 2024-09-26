string = list(input())

alphabet = []
for i in range(0,len(string),2):
    alphabet.append(string[i])

unique_string = list(set(alphabet))
unique_string.sort()
length = len(unique_string)

string_list = []
maximum = 0

def backtracking(num):
    global maximum
    
    if(num == length):
        maximum = max(maximum,compute(string,string_list))
        return

    for i in range(1,5):
        #여기서 i를 써서 각 변수에 추가하기
        string_list.append(i)
        backtracking(num+1)
        string_list.pop()
    return

def compute(string,string_list):
    tmp_sum = string_list[unique_string.index(string[0])]

    for i in range(0,len(string)-2,2):
        
        end = string[i+2]
        math = string[i+1]

        idx_end = unique_string.index(end)

        if (math == '+'):
            tmp_sum += string_list[idx_end]
        if (math == '-'):
            tmp_sum -= string_list[idx_end]
        if (math == '*'):
            tmp_sum *= string_list[idx_end]      

        #print(tmp_sum)
        #print(tmp_sum,math,end," ",string_list[idx_end],i)

    return tmp_sum

    #string 과 stringlist를 가지고 계산을 해야함

backtracking(0)
print(maximum)