# -*- coding: utf-8 -*-

import sys
sys.path.append('..') # 添加相對路徑上兩層到sys.path，讓程式找到的模組_package
from _package.single_game_dfs import single_game_DFS

import cProfile

class frog():
    
    def __init__(self, n):
        self.board = (1,)*n+(0,)+(2,)*n
        self.final_board = (2,)*n+(0,)+(1,)*n
        
    def __swap_tuple(self, Tuple, a, b):
        if a > b:
            a, b = b, a
        return Tuple[:a]+(Tuple[b],)+Tuple[a+1:b]+(Tuple[a],)+Tuple[b+1:]
    
    def getValidMoves(self):
        board = self.board
        empty_idx = board.index(0)
        Len = len(board)
        move = {'蛙1右跳':-2, '蛙1右走': -1, '蛙2左跳': 2, '蛙2左走': 1}
        if empty_idx<2 or board[empty_idx-2]!=1:
            del move['蛙1右跳']
        if empty_idx<1 or board[empty_idx-1]!=1:
            del move['蛙1右走']
        if empty_idx>Len-3 or board[empty_idx+2]!=2:
            del move['蛙2左跳']
        if empty_idx>Len-2 or board[empty_idx+1]!=2:
            del move['蛙2左走']
        return {k:self.__swap_tuple(board, empty_idx, empty_idx+v) for k, v in move.items()}
            
    
    def get_board(self):
        return self.board
    
    def set_board(self, board):
        self.board = board
    
    def terminal(self):
        return self.board == self.final_board 

def main():
    state = frog(7)
    solver = single_game_DFS(state)
    res = solver.DFS(100)
    print(len(res), res)
    
if __name__=='__main__':
    """
    求解青蛙過河, 問題: https://www.i-gamer.net/play/1231.html
    因為行動很少，幾乎都是單行道，搜索深度可以很深
    """
    #cProfile.run('main()')
    main()