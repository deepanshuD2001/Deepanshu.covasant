#input data = [1,2,3, [1,2,3,[3,4],2]]
#output data=[1, 2, 3, 1, 2, 3, 3, 4, 2]

def flattens(input):
    temp=[]
    temp=[*input[:3],*input[-1][:3],*input[-1][3],input[-1][-1]]
    return temp
    
if __name__=='__main__':
    input = [1,2,3, [1,2,3,[3,4],2]]
    result=flattens(input)
    print(result)