# Python interview question
# Python program to multiply two matrix
# using nested loop

# let's go

# 3x3 matrix multiplication

x = [[12,7,3],
    [4,5,6],
    [7,8,9]]

y = [[5,8,1,2],
    [6,7,3,8],
    [4,5,9,1]]

# result matrix will be 3x4

result = [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]

for i in result:
    print(i)