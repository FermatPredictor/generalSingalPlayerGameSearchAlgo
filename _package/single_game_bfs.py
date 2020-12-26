class single_game_BFS():
    
    def __init__(self, state):
        self.state = state
        
    def BFS(self):
        seen_set = set() # 記錄哪些盤面走過了
        queue = [(self.state.hash_value(), [])]
        while queue:
            board, actions = queue.pop()
            if board not in seen_set:
                seen_set.add(board)
                self.state.setBoard(board)
                if self.state.terminal():
                    return actions
                queue += [(v, actions+[k])for k, v in self.state.getValidMoves().items()]
        