memo = {}
def minPathSum(grid):
  def loof(x,y,gird):
    point = '{},{}'.format(x, y)
    if point == '0,0':
      memo[point] = grid[0][0]
      return grid[0][0]
    elif point in memo.keys():
      return memo[point]
    else:
      if x == 0:
        point_sum = memo['{},{}'.format(x, y-1)]+grid[x][y]
        memo[point] = point_sum
        return memo[point]
      elif y == 0:
        point_sum = memo['{},{}'.format(x-1, y)]+grid[x][y]
        memo[point] = point_sum
        return memo[point]
      else:
        point_sum = min(memo['{},{}'.format(x, y-1)]+grid[x][y], memo['{},{}'.format(x-1, y)]+grid[x][y])
        memo[point] = point_sum
        return memo[point]
  
  for x in range(len(grid)):
    for y in range(len(grid[0])):
      result = loof(x,y,grid)
  return result

'''
모범 답안
def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    
    for i in range(1, n):
        grid[0][i] += grid[0][i-1]
        
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
        
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
            
    return grid[-1][-1]
    '''