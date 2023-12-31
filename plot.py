import matplotlib.pyplot as plt


def generate_clockwise_spiral(number_of_rings):
    """
    Generate a n x n clockwise spiral matrix.
    """
    width = (2 * number_of_rings) - 1
    spiral = [[0 for _ in range(width)] for _ in range(width)]

    x, y = width // 2, width // 2  # Start from the center
    num = 0
    dx, dy = 1, 0  # Initial direction: right
    steps = 1

    while num < width * width:
        for _ in range(
            2
        ):  # Change direction twice after completing each layer of the spiral
            for _ in range(steps):
                if 0 <= x < width and 0 <= y < width:
                    spiral[x][y] = num
                    num += 1
                x += dx
                y += dy
            dx, dy = -dy, dx  # Change direction: right -> up -> left -> down
        steps += 1

    return spiral


def plot_spiral(spiral):
    n = len(spiral)
    center_offset = (n - 1) // 2

    plt.figure(figsize=(8, 8))
    plt.title("Clockwise Spiral Grid Indexing with 5 Rings")
    plt.grid(True)

    # Plot each point
    for i in range(n):
        for j in range(n):
            adjusted_x = i - center_offset
            adjusted_y = center_offset - j
            plt.plot(adjusted_x, adjusted_y, "bo", markersize=4)
            plt.text(
                adjusted_x, adjusted_y, str(spiral[i][j]), color="red", fontsize=12
            )

    plt.gca().set_aspect("equal", adjustable="box")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()


corrected_spiral_5x5 = generate_clockwise_spiral(5)
plot_spiral(corrected_spiral_5x5)
