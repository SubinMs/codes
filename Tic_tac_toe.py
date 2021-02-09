#player1 = 0
#player2 = 1
print()
print("***************SOS****************")
size = int(input("Enter size of the bord : "))
final_gameResult = []
print()
print("Enter the final result :")
#outcom = [[1,1,0],[0,1,0],[1,1,0]]
#print(type(outcom))
for i in range(size):
    final_gameResult.append([])
    for j in range(size):
        final_gameResult[i].append(0)

for i in range(0,size) :
    for j in range(0,size) :
        final_gameResult[i][j] = int(input())
        

#print(final_gameResult)
#size = len(outcome)


def row(outcome):
    
    for i in range(0 , size) :
        flag = flag2 = j = 0
        
        for j in range(0 , size) :
            if outcome[i][j] == 0 :
                flag = flag +  1
            else:
                flag2 = flag2 + 1
            
        if flag == size :
            result = "player1 won"
            return result
            break
        elif flag2 == size :
            result = "player2 won"
            return result
            break
        
            
 
def col(outcome):
    
    for i in range(0 , size) :
        flag = flag2 = 0
        
        for j in range(0 , size) :
            if outcome[j][i] == 0 :
                flag = flag +  1
            else:
                flag2 = flag2 + 1
           
        if flag == size :
            result = "player1 won"
            return result
            break
        elif flag2 == size :
            result = "player2 won"
            return result
            break       
 
def diag(outcome) :
    flag = flag2 =0
    for i in range(0,size) :
        
        if outcome[i][i] == 0 :
            flag = flag+1
        else:
            flag2 = flag2+1
            
       
    if flag == size :
        result = "player1 won"
        return result
        
    elif flag2 == size :
        result = "player2 won"
        return result
          
    flag = flag2 =0    
    for j in range(size-1,-1) :
        
        if outcome[j][j] == 0 :
            flag = flag+1
        else:
            flag2 = flag2+1
            
        
    if flag == size :
        result = "player1 won"
        return result
        
    elif flag2 == size :
        result = "player2 won"
        return result

print(" ")
if row(final_gameResult) == "player1 won" or col(final_gameResult) == "player1 won" or diag(final_gameResult) == "player1 won":
    print("Player1 won")
elif row(final_gameResult) == "player2 won" or col(final_gameResult) == "player2 won" or diag(final_gameResult) == "player2 won":
    print("Player2 won")
else:
    print("Draw")
 


            
                
                
