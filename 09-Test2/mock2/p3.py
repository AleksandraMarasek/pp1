def f(array2d):
    for i in range(0, len(array2d)-1):
        sum_row=0
        sum_col=0
        for j in range(0,len(array2d[i])):
            sum_row+=array2d[i][j]
            sum_col+=array2d[j][i]
        if sum_col==sum_row:
            return True
        else:
            return False

print(f([[3,7,2],[4,2,5],[5,2,1]]))

    