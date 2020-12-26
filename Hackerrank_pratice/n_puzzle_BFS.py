# -*- coding: utf-8 -*-
from collections import deque
import time

class single_game_BFS():
    
    def __init__(self, state):
        self.state = state
        self.search_node = 0
        
    def __BFS(self, max_step):
        """ max_step: 最多搜索幾步 """
        seen_set = set() # 記錄哪些盤面走過了
        queue = deque([(self.state.get_board(), [], 0)])
        while queue:
            board, actions, step = queue.popleft()
            self.search_node += 1
            if board not in seen_set:
                seen_set.add(board)
                self.state.set_board(board)
                if self.state.terminal():
                    return (actions, step)
                if step<max_step:
                    queue += [(v, actions+[k], step+1) for k, v in self.state.getValidMoves().items()]
                
    def BFS(self, max_step=10):
        start_time = time.time()
        self.search_node = 0
        res = self.__BFS(max_step)
        #if not res:
        #    print(f"We can't solve the game within {max_step} step")
        #eval_time = time.time() - start_time
        #print(f"--- {eval_time} seconds ---, search {self.search_node} nodes")
        return res

class n_puzzle():
    
    def __init__(self, height, width, board):
        self.height = height
        self.width = width
        self.board = tuple(sum(board,[]))
        self.final_board = tuple(range(height*width))
        
    def __swap_tuple(self, Tuple, a, b):
        if a > b:
            a, b = b, a
        return Tuple[:a]+(Tuple[b],)+Tuple[a+1:b]+(Tuple[a],)+Tuple[b+1:]
    
    def getValidMoves(self):
        H, W = self.height, self.width
        board = self.board
        empty_idx = board.index(0)
        move = {'LEFT':-1, 'RIGHT': 1, 'UP': -W, 'DOWN': W}
        q, r = divmod(empty_idx,W)
        if r==W-1:
            del move['RIGHT']
        if r==0:
            del move['LEFT']
        if q==H-1:
            del move['DOWN']
        if q==0:
            del move['UP']
        return {k:self.__swap_tuple(board, empty_idx, empty_idx+v) for k, v in move.items()}
            
    
    def get_board(self):
        return self.board
    
    def set_board(self, board):
        self.board = board
    
    def terminal(self):
        return self.board == self.final_board 

def main():
    n = int(input())
    board = [[None]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            board[i][j]=int(input())
    state = n_puzzle(n,n, board)
    solver = single_game_BFS(state)
    res = solver.BFS(200)
    if res:
        action, step = res
        print(step)
        for a in action:
            print(a)
            
if __name__=='__main__':
    """
    ref: https://www.hackerrank.com/challenges/n-puzzle
    用普通的BFS解hackerrank的n-puzzle，過關了，
    本來以為是不是要用「A-star」之類的
    """
    main()