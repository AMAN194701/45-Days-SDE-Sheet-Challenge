from collections import deque
class Solution():
    def rotten_org(self, grid):
        row = len(grid)
        col = len(grid[0])

        queue = deque()
        fresh = 0 

        # count all the fresh and rotten oranges
        for r in range(row):
            for c in range(col):
                if grid[r][c]==2 :
                    queue.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1

        # if no fresh exist the return 0 
        if fresh ==0 :
            return 0
        
        # up, down , left and right  
        drxn = [(-1,0), (1,0),(0,-1), (0,1)]
        mints=0 

        while queue and fresh >0:
            for _ in range(len(queue)):
                r , c = queue.popleft()

                # move and check for new row and col
                for dr , dc in drxn:
                    nr = dr+ r 
                    nc = dc + c 

                    # check 3 condition 
                    # 1. Inside row boundary
                    # 2. Inside column boundary
                    # 3. Neighbor is a fresh orange
                    if (
                        0 <= nr < len(grid) and 
                        0 <= nc < len(grid[0]) and 
                        grid[nr][nc] ==1
                    ):
                        grid[nr][nc]=2
                        fresh -=1
                        queue.append((nr,nc))


            mints+=1
        return mints if fresh ==0 else -1

