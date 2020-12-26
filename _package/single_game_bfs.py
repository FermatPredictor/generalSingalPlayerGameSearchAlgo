# -*- coding: utf-8 -*-

from collections import deque
import time

class single_game_BFS():
    
    """
    單人遊戲的BFS模版，
    用途是只要定義好遊戲規則，
    ai就會透過此演算法尋找最短步數解法
    
    適用: n-puzzle, 青蛙過河這類單人遊戲，
    在有限步可以抵達過關盤面
    
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
        if not res:
            print(f"We can't solve the game within {max_step} step")
        eval_time = time.time() - start_time
        print(f"--- {eval_time} seconds ---, search {self.search_node} nodes")
        return res
        
        
        