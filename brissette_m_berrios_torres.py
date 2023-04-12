

def process_matrix(matrix):
    W = len(matrix)
    H = len(matrix[0])

    # Create empty matrix
    result =[]

    for i, column in enumerate(matrix):
        row = []
        for j, value in enumerate(column):
            new_value = process_element(i, j, value, matrix, W, H)
            row.append(new_value)
        result.append(row)

    return result

def process_element(i, j, value, matrix, W, H):
    neighbours = find_neighbours(i, j, matrix, W, H)
    elements = neighbours + [value]
    avg = get_average (elements)

    return avg

def find_neighbours(i, j, matrix, W, H):
    neighbours = []

    # Top
    if (j - 1) >= 0:
        value = matrix[i][j-1]
        neighbours.append(value)

    # Right
    if (i + 1) < W:
        value = matrix[i+1][j]
        neighbours.append(value)

    # Bottom
    if (j + 1) < H:
        value = matrix[i][j+1]
        neighbours.append(value)

    # Left
    if (i - 1) >= 0:
        value = matrix[i-1][j]
        neighbours.append(value)

    return neighbours


def get_average(elements): 
    """
    Calcular el promedio
    """
    return sum(elements) / len(elements)
