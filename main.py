krestik = 'X'
nolik = 'O'
moves = 0
flag = True
figure = [['.' for j in range(3)] for i in range(3)]
krestik_bool = [[0 for j in range(3)] for i in range(3)]
nolik_bool = [[0 for j in range(3)] for i in range(3)]
Corners = [[0, 0], [2, 0], [2, 2], [0, 2]]
Sides = [[1, 0], [2, 1], [1, 2], [0, 1]]
nextmove = ['Next','']

def printing_tictac():
    print('* 0 1 2')
    for y in range(3):
        print(y,figure[0][y], figure[1][y], figure[2][y])

def printing_tictac_with_bool():
    print('* 0 1 2')
    for y in range(3):
        print(y,figure[0][y], figure[1][y], figure[2][y],
              ' - ',krestik_bool[0][y], krestik_bool[1][y], krestik_bool[2][y],
              ' - ', nolik_bool[0][y], nolik_bool[1][y], nolik_bool[2][y])

def input_coordinates():
    xy_is_real = False
    xy = ''
    while not xy_is_real or xy == '':
        #printing_tictac()
        which_move = moves + 1
        xy = input('Input your %d move to (xy):' % which_move)
        if not xy.isdigit():
            print('---Warning!--- Not digits')
        elif len(xy) != 2:
            print('---Warning!--- Only 2 digits')
        elif len(xy) == 2:
            x = int(xy[0])
            y = int(xy[1])
            if x > 2 or y > 2:
                xy_is_real = False
                print('---Warning!--- Out of range')
            else:
                xy_is_real = True
                #print('xy_is_real',xy)
                x = int(xy[0])
                y = int(xy[1])
                if figure[x][y] != '.':
                    xy_is_real = False
                    print('---Warning!--- Not empty field')
                    print('xy', xy)
                else:
                    xy_is_real = True
                    figure[x][y] = 'X'
                    krestik_bool[x][y] = 1
                    z = 1
    else:
        pass
        #print('Some real XY is got:',xy_is_real,x,y,z)
    return xy

def cell_check(matrix,name):
    #print('Cell cheking for', name)
    global nextmove
    Victory = False
    #print(name)
    fp = False #first priority
    column = [0,0,0]
    row = 0
    for y in range(3):
        row = matrix[0][y] + matrix[1][y] + matrix[2][y]
        #print(y,figure[0][y], figure[1][y], figure[2][y],' - ',krestik_bool[0][y], krestik_bool[1][y], krestik_bool[2][y],' - ', nolik_bool[0][y], nolik_bool[1][y], nolik_bool[2][y],' - Row_sum', y, row)
        column[y] = sum(matrix[y])
        if row == 3 or column[y] == 3:
            Victory = True
        #print('Thinking next move for:', y, name)
        if row == 2:
            #print('Row=2', y)
            fp = True
            if not nolik_bool[0][y] and not krestik_bool[0][y]:
                 nextmove = [0,y]
            elif not nolik_bool[1][y] and not krestik_bool[1][y]:
                 nextmove = [1,y]
            elif not nolik_bool[2][y] and not krestik_bool[2][y]:
                nextmove = [2,y]
            else:
                fp = False
                nextmove = ['Next', 'row']
            #print('nextmove', nextmove, fp)
        if not fp and column[y] == 2:
            #print('Column=2',y)
            fp = True
            if not nolik_bool[y][0] and not krestik_bool[y][0]:
                nextmove = [y,0]
            elif not nolik_bool[y][1] and not krestik_bool[y][1]:
                nextmove = [y,1]
            elif not nolik_bool[y][2] and not krestik_bool[y][2]:
                nextmove = [y,2]
            else:
                fp = False
                nextmove = ['Next', 'col']
            #print('nextmove', nextmove)
    #print('nextmove all else', nextmove)
    #print('C', column)
    diag_0 = matrix[0][0] + matrix[1][1] + matrix[2][2]
    diag_2 = matrix[2][0] + matrix[1][1] + matrix[0][2]
    #print('diag_0', diag_0, 'diag_2', diag_2)
    if diag_0 == 2:
        #print('diag_0=2')
        fp = True
        if not nolik_bool[0][0] and not krestik_bool[0][0]:
            nextmove = [0, 0]
        elif not nolik_bool[1][1] and not krestik_bool[1][1]:
            nextmove = [1, 1]
        elif not nolik_bool[2][2] and not krestik_bool[2][2]:
            nextmove = [2, 2]
        else:
            fp = False
            nextmove = ['Next', 'd1']
        #print('nextmove', nextmove)
    if not fp and diag_2 == 2:
        #print('diag_2=2')
        fp = True
        if not nolik_bool[2][0] and not krestik_bool[2][0]:
            nextmove = [2, 0]
        elif not nolik_bool[1][1] and not krestik_bool[1][1]:
            nextmove = [1, 1]
        elif not nolik_bool[0][2] and not krestik_bool[0][2]:
            nextmove = [0, 2]
        else:
            fp = False
            nextmove = ['Next', 'd2']
        #print('nextmove', nextmove)
    if diag_0 == 3 or diag_2 == 3:
        Victory = True
    if Victory:
        winner = name
        #print(name, 'wins')
        return name
    else:
        return False

def checking_victory():
    if moves >= 3:
        name = cell_check(nolik_bool, 'Noliki')
        #print('Name Noliki', name)
        if not name:
            name = cell_check(krestik_bool, 'Krestiki')
            #print('Name Krestiki', name)
        return name

def noliki_moves():
    fla = True
    global nextmove
    nextmove = ['Next', 'b']
    #print('Next move for Noliki:', nextmove)
    #print('Flag:',fla)
    if not krestik_bool[1][1] and not nolik_bool[1][1]:
        print('Comp moved to center: 1, 1')
        figure[1][1] = 'O'
        nolik_bool[1][1] = 1
        fla = False
    else:
        cell_check(nolik_bool,'Noliki')
        #print('Next move from NM Nol:',nextmove)
        if nextmove[0] == 'Next':
            cell_check(krestik_bool, 'Krestiki')
            #print('Here next from NM Kre:', nextmove)
    if nextmove[0] == 'Next':
        for c in Corners:
            x,y = c[0],c[1]
            #print('Searching corners:', x, y)
            if fla and not krestik_bool[x][y] and not nolik_bool[x][y]:
                print('Comp moved to corner:',x,y)
                figure[x][y] = 'O'
                nolik_bool[x][y] = 1
                fla = False
                #print('Flag:',fla)
                break
        if fla:
            for s in Sides:
                x, y = s[0], s[1]
                #print('Searching Sides:', x, y)
                if fla and not krestik_bool[x][y] and not nolik_bool[x][y]:
                    print('Comp moved to side', x, y)
                    figure[x][y] = 'O'
                    nolik_bool[x][y] = 1
                    fla = False
                    #print('Flag:',fla)
                    break
    else:
        x, y = nextmove[0], nextmove[1]
        print('COMP MOVED TO...', x, y)
        figure[x][y] = 'O'
        nolik_bool[x][y] = 1
        fla = False
    printing_tictac()

print('Begin')
print('You plays X, comp plays O')
Victory = False
printing_tictac()

while moves < 5:
    xy = input_coordinates()
    #print(xy)
    #print('XY',xy[0],xy[1])
    moves += 1
    print('Moves did =', moves)
    Victory = checking_victory()
    noliki_moves()
    #printing_tictac()
    #printing_tictac_with_bool()
    Victory = checking_victory()
    if Victory:
        print(Victory, 'WINS')
        break
    if moves == 5:
        print('GAME OVER')
        break
