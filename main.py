import tkinter as tk

# Define dictionaries to store button colors
r_button_color = {}
g_button_color = {}
b_button_color = {}


def get_button_color(row, col, color_dict):
    button_id = f'{color_dict["prefix"]}{row + 1}{col + 1}'
    return color_dict.get(button_id, 'black')  # Default to black if button_id not found


def color_mixing(frame, row, col):
    red_color = get_button_color(row, col, r_button_color)
    green_color = get_button_color(row, col, g_button_color)
    blue_color = get_button_color(row, col, b_button_color)

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

    print(
        f"r{row + 1},{col + 1}: {red_color}, g{row + 1},{col + 1}: {green_color}, b{row + 1},{col + 1}: {blue_color}, solution: {solution_color}")

    # Update solution color on the white grid
    button_id = f'white{row + 1}{col + 1}'
    white_grid_button_color[button_id] = solution_color
    white_grid_button[button_id].configure(bg=solution_color)


def create_color_button(frame, color, row, col, color_dict):
    button_id = f'{color[0]}{row + 1}{col + 1}'
    color_dict[button_id] = color
    button = tk.Button(frame, bg=color, width=1, height=1,
                       command=lambda: toggle_color(frame, button, color, row, col, color_dict))
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
            white_frame = tk.Frame(frame)
            white_frame.grid(row=0, column=0)
            create_white_grid_buttons(white_frame, num_buttons)
        else:
            color_dict = r_button_color if color == 'red' else g_button_color if color == 'green' else b_button_color
            color_dict["prefix"] = color[0]
            for row in range(num_buttons):
                for col in range(num_buttons):
                    create_color_button(frame, color, row, col, color_dict)


def create_white_grid_buttons(frame, num_buttons):
    global white_grid_button_color, white_grid_button
    white_grid_button_color = {}
    white_grid_button = {}

    for row in range(num_buttons):
        for col in range(num_buttons):
            button_id = f'white{row + 1}{col + 1}'
            white_grid_button_color[button_id] = 'white'
            button = tk.Button(frame, bg='white', width=1, height=1)
            button.config(state="disabled")
            button.grid(row=row, column=col, sticky='nsew')
            white_grid_button[button_id] = button


def main():
    root = tk.Tk()
    root.title("Color Boxes Program")

    create_color_boxes(root)

    root.mainloop()


if __name__ == "__main__":
    main()
