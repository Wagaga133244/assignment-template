#  H

import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("贪吃蛇游戏")
        
        self.canvas = tk.Canvas(root, width=400, height=400, bg="lightblue")
        self.canvas.pack()

        self.snake = [(200, 200), (210, 200), (220, 200)]
        self.snake_direction = "Left"
        self.food_position = self.set_new_food_position()
        self.score = 0

        self.root.bind("<KeyPress>", self.change_direction)
        self.run_game()

    def set_new_food_position(self):
        while True:
            x = random.randint(0, 39) * 10
            y = random.randint(0, 39) * 10
            if (x, y) not in self.snake:
                return (x, y)

    def change_direction(self, event):
        new_direction = event.keysym
        all_directions = {"Up", "Down", "Left", "Right"}
        opposites = {("Up", "Down"), ("Left", "Right")}

        if new_direction in all_directions and (self.snake_direction, new_direction) not in opposites:
            self.snake_direction = new_direction

    def run_game(self):
        self.update_snake_position()
        self.check_collisions()
        self.update_canvas()
        self.root.after(100, self.run_game)

    def update_snake_position(self):
        head_x, head_y = self.snake[0]

        if self.snake_direction == "Up":
            new_head = (head_x, (head_y - 10) % 400)
        elif self.snake_direction == "Down":
            new_head = (head_x, (head_y + 10) % 400)
        elif self.snake_direction == "Left":
            new_head = ((head_x - 10) % 400, head_y)
        elif self.snake_direction == "Right":
            new_head = ((head_x + 10) % 400, head_y)

        self.snake = [new_head] + self.snake

        if self.snake[0] == self.food_position:
            self.food_position = self.set_new_food_position()
            self.score += 1
        else:
            self.snake.pop()

    def check_collisions(self):
        if len(self.snake) != len(set(self.snake)):
            self.game_over()

    def update_canvas(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_oval(self.food_position[0], self.food_position[1], 
                                self.food_position[0] + 10, self.food_position[1] + 10, fill="red")
        for i, (x, y) in enumerate(self.snake):
            color = "darkgreen" if i == 0 else "green"
            self.canvas.create_rectangle(x, y, x + 10, y + 10, fill=color)
        self.canvas.create_text(50, 10, text=f"得分: {self.score}", fill="white", font=("Arial", 12))

    def game_over(self):
        self.canvas.create_text(200, 200, text=f"游戏结束！得分: {self.score}", fill="white", font=("Arial", 20))
        self.root.update()
        self.root.after(2000, self.root.destroy)

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()