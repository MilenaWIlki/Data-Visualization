import matplotlib.pyplot as plt

def data_visualization(x, y):
    plt.scatter(x, y)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Data Visualization")
    plt.show()

# Example usage:
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
data_visualization(x, y)
