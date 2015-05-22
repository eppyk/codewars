def fire(x,y):
    if x==0 or y==0:
        return grid[x+y]
    elif x==2 and y==2:
        return grid[x+y]
    return grid[x+y+2]


grid = ['top left',    'top middle',    'top right',
        'middle left', 'center',        'middle right',
        'bottom left', 'bottom middle', 'bottom right']
fire(0,0, grid)
