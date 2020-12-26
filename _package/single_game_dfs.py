# -*- coding: utf-8 -*-
import time

class single_game_DFS():
    
    """
    單人遊戲的DFS模版，
    用途是只要定義好遊戲規則，
    ai就會透過此演算法尋找一組解
    
    適用: 馬踏棋盤，不會造成循環盤面的單人遊戲
    
    必要定義的物件:
    * state: 遊戲規則定義
       (通常board是一個tuple，方便記錄是否到過此盤面)
       - def get_board(): 回傳盤面
       - def set_board(board): 將state的盤面設為board
       - def getValidMoves(): 回傳字典{行動(通常以字串表示): 盤面(通常以tuple表示)}
       - def terminal(): 判斷一場遊戲是否已經解開
    """
    
    def __init__(self, state):
        self.state = state
        self.search_node = 0
        
    def __DFS(self, max_depth, action_list, board=None):
        """ max_depth: 最多搜索幾層 """
        if board:
            self.state.set_board(board)
        self.search_node += 1
        if self.state.terminal():
            return action_list
        if max_depth==0:
            return
        for k, v in self.state.getValidMoves().items():
            res = self.__DFS(max_depth-1, action_list+[k], v)
            if res:
                return res
            
                
    def DFS(self, max_depth=10):
        start_time = time.time()
        self.search_node = 0
        res = self.__DFS(max_depth,[])
        if not res:
            print(f"We can't solve the game within {max_depth} step")
        eval_time = time.time() - start_time
        print(f"--- {eval_time} seconds ---, search {self.search_node} nodes")
        return res