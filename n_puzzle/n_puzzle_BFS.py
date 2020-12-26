# -*- coding: utf-8 -*-

import sys
sys.path.append('..') # 添加相對路徑上兩層到sys.path，讓程式找到的模組_package
from _package.single_game_bfs import single_game_BFS

import cProfile

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
        move = {'LEFT':1, 'RIGHT': -1, 'UP': W, 'DOWN': -W}
        q, r = divmod(empty_idx,W)
        if r==0:
            del move['RIGHT']
        if r==W-1:
            del move['LEFT']
        if q==0:
            del move['DOWN']
        if q==H-1:
            del move['UP']
        return {k:self.__swap_tuple(board, empty_idx, empty_idx+v) for k, v in move.items()}
            
    
    def get_board(self):
        return self.board
    
    def set_board(self, board):
        self.board = board
    
    def terminal(self):
        return self.board == self.final_board 

def main():
    board = [[0,3,8],
             [4,1,7],
             [2,6,5]]
    state = n_puzzle(3,3, board)
    solver = single_game_BFS(state)
    res = solver.BFS(20)
    print(res)
    
if __name__=='__main__':
    """
    用BFS解8-puzzle，解空間只有9!，
    應該是可以完解
    """
    #cProfile.run('main()')
    main()