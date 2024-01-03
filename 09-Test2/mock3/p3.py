def f(array2D):
    for row in range(0, len(array2D)-1):
        sum_row=0
        sum_column=0
        for column in range(0,len(array2D[row])):
            sum_row+=array2D[row][column]
            sum_column+=array2D[column][row]

        if sum_row==sum_column:
            return True
        else:
            return False

print(f([[3,7,2],[4,2,5],[5,2,1]]))
    