from graphics import Canvas
import time
    
CANVAS_WIDTH : int = 400
CANVAS_HEIGHT : int = 400

CELL_SIZE : int = 40
ERASER_SIZE : int = 20

def erase_objects(canvas, eraser):
    """Erase objects in contact with the eraser"""
    # Get mouse info to help us know which cells to delete
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()
    
    # Calculate where our eraser is
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    # Find things that overlap with our eraser
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    # For everything that overlaps with our eraser (that isn't our eraser), change
    # its color to white
    for overlapping_object in overlapping_objects:
        if overlapping_object != eraser:
            canvas.set_color(overlapping_object, 'white')

def main():
    canvas = Canvas(CANVAS_HEIGHT, CANVAS_WIDTH)

    for y in range(0, CANVAS_HEIGHT, CELL_SIZE):
        for x in range(0, CANVAS_WIDTH, CELL_SIZE):
            canvas.create_rectangle(x, y, x + ERASER_SIZE, y + ERASER_SIZE, "blue")

    canvas.wait_for_click()
    x, y = canvas.get_last_click()

    eraser = canvas.create_rectangle(x, y, x + ERASER_SIZE, y + ERASER_SIZE, "red")

    while True:
        x = canvas.get_mouse_x()
        y = canvas.get_mouse_y()
        canvas.moveto(eraser, x, y)
        eraser(canvas, eraser)
        time.sleep(0.05)

if __name__ == "__main__":
    main()