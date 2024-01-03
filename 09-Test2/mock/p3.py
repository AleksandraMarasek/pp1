def f(array2D):
    size=len(array2D)
    
    for i in range(size):
        row_sum=sum(array2D[i])
        column_sum=sum(array2D[j][i] for j in range(size))

        if row_sum!=column_sum:
            return False
    return True

print(f([[3,7,2],[4,2,5],[9,2,1]]))