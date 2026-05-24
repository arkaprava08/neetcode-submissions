class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        row,col=len(board),len(board[0])

        def find(i,j):
            toadd=[[0,1],[0,-1],[1,0],[-1,0]]
            out=[]
            for add in toadd:
                x,y=i+add[0],j+add[1]
                if (0 <= x < row) and (0 <= y < col):
                    out.append([x,y])
            
            return out

        def dfs(i, j, word, visited):
            if not word:
                return True
            if word[0] == board[i][j]:
                visited[i][j]=1
                if len(word) == 1:
                    return True
            else:
                return False


            out=False
            for x,y in find(i,j):
                if visited[x][y] == 0:
                    out = out or dfs(x,y,word[1:len(word)],visited)

            visited[i][j]=0
            return out

        for i in range(row):
            for j in range(col):
                visited=[[0 for _ in range(col)] for _ in range(row)]
                if dfs(i, j, word, visited):
                    return True
        

        return False

