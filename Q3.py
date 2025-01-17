import turtle

def draw_branch(branch_length, depth, left_angle, right_angle, reduction_factor):
    if depth == 0:
        return
    
    # Set color: red for main trunk, green for others
    if depth == max_depth:
        turtle.pencolor("red")
    else:
        turtle.pencolor("green")
    
    # Draw main branch
    turtle.forward(branch_length)
    
    # Left branch
    turtle.left(left_angle)
    draw_branch(branch_length * reduction_factor, depth - 1, left_angle, right_angle, reduction_factor)
    turtle.right(left_angle)  # Return to center
    
    # Right branch
    turtle.right(right_angle)
    draw_branch(branch_length * reduction_factor, depth - 1, left_angle, right_angle, reduction_factor)
    turtle.left(right_angle)  # Return to center
    
    # Move back to previous position
    turtle.backward(branch_length)

# Get user input for tree parameters
left_angle = int(input("Enter left branch angle: "))
right_angle = int(input("Enter right branch angle: "))
start_length = int(input("Enter starting branch length: "))
depth = int(input("Enter recursion depth: "))
reduction_factor = float(input("Enter branch length reduction factor (e.g., 0.7): "))

# Set up the turtle
turtle.speed("fastest")
turtle.left(90)  # Point turtle upwards
turtle.up()
turtle.goto(0, -200)  # Move turtle to starting position
turtle.down()

global max_depth
max_depth = depth  # Store the maximum depth

# Draw the tree
draw_branch(start_length, depth, left_angle, right_angle, reduction_factor)

turtle.hideturtle()
turtle.done()
