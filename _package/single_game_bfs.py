class single_game_BFS():
    
    def __init__(self, state):
        self.state = state
        
    def BFS(self, max_step):
        """ max_step: 最多搜索幾步 """
        seen_set = set() # 記錄哪些盤面走過了
        queue = [(self.state.hash_value(), [], 0)]
        while queue:
            board, actions, step = queue.pop()
            if board not in seen_set:
                seen_set.add(board)
                self.state.setBoard(board)
                if self.state.terminal():
                    return (actions, step)
                queue += [(v, actions+[k], step)for k, v in self.state.getValidMoves().items()]
        