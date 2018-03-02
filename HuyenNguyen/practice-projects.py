##Practice Projects
##Chaper 4: Comma Code
spam= ['apples', 'bananas', 'tofu', 'cats']
def list(list):
    new_string = ''
    for i in list:
        new_string += str(i)
        if list.index(i) == (len(list)-2):
            new_string = new_string + ', and '
        elif list.index(i) == (len(list)-1):
            new_string = new_string
        else:
            new_string += ', '
    return new_string

print (list(spam))

##Result:
##apples, bananas, tofu, and cats
##----------------------------------------
##Chaper 4: Character Picture Grid

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def reformat(grid):
    for i in range(0,len(grid[0])):  #length = 6 
        myStr = ''                    
        for j in range(0,(len(grid))): #length = 8 
            myStr += grid[j][i]           
        print(myStr)                  

reformat(grid)
##Result:
##..OO.OO..
##.OOOOOOO.
##.OOOOOOO.
##..OOOOO..
##...OOO...
##....O....
##--------------------------------------
