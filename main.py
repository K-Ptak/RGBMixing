import tkinter as tk

# Define dictionaries to store button colors
r_button_color = {}
g_button_color = {}
b_button_color = {}

def get_button_color(frame, row, col, color_dict):
    button_id = f'{color_dict["prefix"]}{row + 1}{col + 1}'
    return color_dict.get(button_id)  # Use get() to avoid KeyError if button_id not found

def color_mixing(frame, row, col):
    red_color = get_button_color(frame, row, col, r_button_color)
    green_color = get_button_color(frame, row, col, g_button_color)
    blue_color = get_button_color(frame, row, col, b_button_color)

    if red_color == 'black' and green_color == 'black' and blue_color == 'black':
        solution_color = 'black'
    elif red_color == 'red' and green_color == 'black' and blue_color == 'black':
        solution_color = 'red'
    elif red_color == 'black' and green_color == 'green' and blue_color == 'black':
        solution_color = 'green'
    elif red_color == 'black' and green_color == 'black' and blue_color == 'blue':
        solution_color = 'blue'
    elif red_color == 'red' and green_color == 'green' and blue_color == 'black':
        solution_color = 'yellow'
    elif red_color == 'red' and green_color == 'black' and blue_color == 'blue':
        solution_color = 'magenta'
    elif red_color == 'black' and green_color == 'green' and blue_color == 'blue':
        solution_color = 'cyan'
    else:
        solution_color = 'white'


    print(f"r{row,col}: {red_color}, g{row,col}: {green_color}, b{row,col}: {blue_color}")


def create_color_button(frame, color, row, col, color_dict):
    button_id = f'{color[0]}{row + 1}{col + 1}'
    color_dict[button_id] = color
    button = tk.Button(frame, bg=color, width=1, height=1, command=lambda: toggle_color(frame, button, color, row, col, color_dict))
    button.grid(row=row, column=col, sticky='nsew')

def toggle_color(frame, button, original_color, row, col, color_dict):
    current_color = button.cget('bg')
    new_color = 'black' if current_color == original_color else original_color
    button.configure(bg=new_color)

    button_id = f'{color_dict["prefix"]}{row + 1}{col + 1}'
    color_dict[button_id] = new_color  # Update the color in the dictionary

    color_mixing(frame, row, col)

def create_color_boxes(root):
    colors = ['red', 'green', 'blue', 'white']
    num_buttons = 10

    for color in colors:
        frame = tk.Frame(root)
        frame.grid(row=0, column=colors.index(color))
        frame.column, frame.row = 0, 0

        if color == 'white':
            canvas = tk.Canvas(frame, width=num_buttons * 10, height=num_buttons * 10, bg=color)
            canvas.grid(row=0, column=0, sticky='nsew')
            create_color_grid(canvas, color, num_buttons * 10, num_buttons, num_buttons)
        else:
            color_dict = r_button_color if color == 'red' else g_button_color if color == 'green' else b_button_color
            color_dict["prefix"] = color[0]
            for row in range(num_buttons):
                for col in range(num_buttons):
                    create_color_button(frame, color, row, col, color_dict)

def create_color_grid(canvas, color, size, rows, columns):
    square_size = size // columns
    for row in range(rows):
        for col in range(columns):
            x1 = col * square_size
            y1 = row * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size
            square_id = f'{color[0]}{row + 1}{col + 1}'
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='black', tags=square_id)

def main():
    root = tk.Tk()
    root.title("Color Boxes Program")

    create_color_boxes(root)

    root.mainloop()

if __name__ == "__main__":
    main()
