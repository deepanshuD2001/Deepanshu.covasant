def Converts(input):
    final=[]
    for i in input:
        temp1=[]
        for j in i:
            temp2=[]
            for k in j:
                if k.isdigit():
                    temp2.append(int(k))
            temp1.append(temp2)
        final.append(temp1)
    return [final]
    

if __name__=='__main__':
    input=[[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
    
    print(input)
    result=Converts(input[0])
    print(result)
