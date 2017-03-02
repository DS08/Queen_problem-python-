
chess_board_row= [0,0,0,0,0,0,0,0,0] ## row[] = column
count = 0


def possible_placement(position):
    for index in range(1,position):
        if chess_board_row[index]==chess_board_row[position] or abs(chess_board_row[index]-chess_board_row[position])==abs(index-position):
            return False ## For checking queen's position in same column or diagonals 
    return True        

def print_soln(n):
    global count
    count +=1
    print('\n\nSolution #'+str(count)+':\n')
    for i in range(1, n+1):
        for j in range(1,n+1):
            if(chess_board_row[i]==j):
                print('Q\t'),
            else:
                print('*\t'),
        print('\n')
                    



    
def Queen_index(n):
    k = 1
    global chess_board_row
    chess_board_row[k] = 0
    while(k!=0):
        while True:
          chess_board_row[k] +=1
          if chess_board_row[k]>n or (possible_placement(k)):
            break
        if(chess_board_row[k]<=n):
            if(k==n):
                print_soln(n)
            else:
                k +=1
                chess_board_row[k] = 0
        else:
            k -=1    
        


Queen_index(8)                    

print('\nTotal solutions='+str(count))
