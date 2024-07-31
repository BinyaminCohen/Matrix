from collections import deque

def updateMatrix(mat):
    if not mat or not mat[0]:
        return mat

    rows, cols = len(mat), len(mat[0])
    dist = [[float('inf')] * cols for _ in range(rows)]
    queue = deque()

    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                dist[r][c] = 0
                queue.append((r,c))

    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        r, c = queue.popleft()

        for dr, dc in direction:
            rr, cc = r + dr , c + dc

            if 0 <= rr < rows and 0 <= cc < cols:
                if dist[rr][cc] > dist[r][c] + 1:
                    dist[rr][cc] = dist[r][c] + 1
                    queue.append((rr, cc))

    return dist





if __name__ == '__main__':

    mat1 = [[0,0,0],[0,1,0],[0,0,0]]
    mat2 = [[0,0,0],[0,1,0],[1,1,1]]
    print(updateMatrix(mat1))
    print(updateMatrix(mat2))




