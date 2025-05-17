

# 123
import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.resizable(False, False)
        
        # Constants
        self.WIDTH = 600
        self.HEIGHT = 400
        self.GRID_SIZE = 20
        self.GAME_SPEED = 150  # milliseconds
        
        # Game state variables
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"
        self.next_direction = "Right"
        self.food_position = self.place_food()
        self.score = 0
        self.game_over = False
        
        # Create canvas
        self.canvas = tk.Canvas(root, width=self.WIDTH, height=self.HEIGHT, bg="black")
        self.canvas.pack(padx=10, pady=10)
        
        # Create score display
        self.score_display = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 14))
        self.score_display.pack(pady=5)
        
        # Create buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)
        
        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start_game)
        self.start_button.grid(row=0, column=0, padx=5)
        
        self.pause_button = tk.Button(self.button_frame, text="Pause", command=self.toggle_pause)
        self.pause_button.grid(row=0, column=1, padx=5)
        
        self.reset_button = tk.Button(self.button_frame, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=0, column=2, padx=5)
        
        # Set up key bindings
        self.root.bind("<Left>", lambda event: self.change_direction("Left"))
        self.root.bind("<Right>", lambda event: self.change_direction("Right"))
        self.root.bind("<Up>", lambda event: self.change_direction("Up"))
        self.root.bind("<Down>", lambda event: self.change_direction("Down"))
        
        # Draw initial game state
        self.draw_game()
        
        # Game is initially paused
        self.is_paused = True
    
    def start_game(self):
        self.is_paused = False
        self.game_loop()
    
    def toggle_pause(self):
        self.is_paused = not self.is_paused
        if not self.is_paused and not self.game_over:
            self.game_loop()
    
    def reset_game(self):
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"
        self.next_direction = "Right"
        self.food_position = self.place_food()
        self.score = 0
        self.game_over = False
        self.is_paused = True
        self.score_display.config(text=f"Score: {self.score}")
        self.draw_game()
    
    def change_direction(self, new_direction):
        # Prevent 180-degree turns
        opposite_directions = {"Left": "Right", "Right": "Left", "Up": "Down", "Down": "Up"}
        if new_direction != opposite_directions.get(self.direction):
            self.next_direction = new_direction
    
    def place_food(self):
        while True:
            x = random.randint(1, (self.WIDTH - self.GRID_SIZE) // self.GRID_SIZE) * self.GRID_SIZE
            y = random.randint(1, (self.HEIGHT - self.GRID_SIZE) // self.GRID_SIZE) * self.GRID_SIZE
            position = (x, y)
            
            # Make sure food doesn't appear on snake
            if position not in self.snake:
                return position
    
    def draw_game(self):
        self.canvas.delete("all")
        
        # Draw snake
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(
                x, y, x + self.GRID_SIZE, y + self.GRID_SIZE,
                fill="green", outline="black"
            )
        
        # Draw snake head in a different color
        head_x, head_y = self.snake[0]
        self.canvas.create_rectangle(
            head_x, head_y, head_x + self.GRID_SIZE, head_y + self.GRID_SIZE,
            fill="dark green", outline="black"
        )
        
        # Draw food
        food_x, food_y = self.food_position
        self.canvas.create_oval(
            food_x, food_y, food_x + self.GRID_SIZE, food_y + self.GRID_SIZE,
            fill="red", outline="black"
        )
        
        # Draw game over message
        if self.game_over:
            self.canvas.create_text(
                self.WIDTH // 2, self.HEIGHT // 2,
                text="Game Over!", fill="white", font=("Arial", 24)
            )
    
    def move_snake(self):
        # Update direction
        self.direction = self.next_direction
        
        # Get current head position
        head_x, head_y = self.snake[0]
        
        # Calculate new head position
        if self.direction == "Right":
            new_head = (head_x + self.GRID_SIZE, head_y)
        elif self.direction == "Left":
            new_head = (head_x - self.GRID_SIZE, head_y)
        elif self.direction == "Up":
            new_head = (head_x, head_y - self.GRID_SIZE)
        elif self.direction == "Down":
            new_head = (head_x, head_y + self.GRID_SIZE)
        
        # Check for collisions
        if (
            new_head[0] < 0 or new_head[0] >= self.WIDTH or
            new_head[1] < 0 or new_head[1] >= self.HEIGHT or
            new_head in self.snake
        ):
            self.game_over = True
            return
        
        # Add new head
        self.snake.insert(0, new_head)
        
        # Check if food is eaten
        if new_head == self.food_position:
            # Don't remove tail (snake grows)
            self.score += 10
            self.score_display.config(text=f"Score: {self.score}")
            self.food_position = self.place_food()
            
            # Increase game speed every 50 points
            if self.score % 50 == 0 and self.GAME_SPEED > 50:
                self.GAME_SPEED -= 10
        else:
            # Remove tail (snake moves)
            self.snake.pop()
    
    def game_loop(self):
        if not self.is_paused and not self.game_over:
            self.move_snake()
            self.draw_game()
            self.root.after(self.GAME_SPEED, self.game_loop)

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()