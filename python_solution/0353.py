class SnakeGame:
    
    # Solution by myself: Deque + Hash Table (296ms: 76.27%)

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.score = 0
        self.food = food[::-1]
        self.height = height
        self.width = width
        self.ocup = {(0,0):True}
        self.snake = deque([(0,0)])

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        directions = {'U':(-1,0), 'L':(0,-1), 'R':(0,1), 'D':(1,0)}
        curi, curj = self.snake[-1]
        di, dj = directions[direction]
        newi, newj = curi+di, curj+dj
        if newi<0 or newi>=self.height or newj<0 or newj>=self.width:
            return -1
        if self.food and newi==self.food[-1][0] and newj==self.food[-1][1]:
            self.food.pop()
            self.snake.append((newi, newj))
            self.ocup[(newi, newj)] = True
            self.score += 1
            return self.score
        else:
            oldi, oldj = self.snake.popleft()
            self.ocup[(oldi, oldj)] = False
            if (newi, newj) in self.snake and self.ocup[(newi, newj)]==True:
                return -1
            self.ocup[(newi, newj)] = True
            self.snake.append((newi, newj))
            return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)