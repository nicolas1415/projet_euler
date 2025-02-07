



function getSudoku(PATH::String)
    file = open(PATH, "r")
    lines = readlines(file)
    sudokus = []
    matrix = []

    for line in lines
        if occursin("Grid", line)
            if !isempty(matrix)
                push!(sudokus, copy(matrix))  # Copy to preserve the matrix structure
            end
            matrix = []
        else
            row = parse.(Int, collect(line))  # Simplified conversion
            push!(matrix, row)
        end
    end

    # Check if the last matrix needs to be added
    if !isempty(matrix)
        push!(sudokus, copy(matrix))
    end

    close(file)  # Close the file after reading
    return sudokus
end

function checkRow!(vect, row, nbr_column)
    bool = false
    for (index, elem) in enumerate(row)
        if length(elem)==1 && index!=nbr_column
            u = length(vect)
            filter!(x -> x != elem[1], vect)
            bool =  length(vect) != u
        end
    end
    return bool
end

function checkColumn!(vect, column, nbr_row)
    bool = false
    for (index, elem) in enumerate(column)
        if length(elem)==1 && index!=nbr_row
            u = length(vect)
            filter!(x -> x != elem[1], vect)
            bool = length(vect) != u
        end
    end
    return bool
end



function checkSquare!(vect,bigMatrix,nbr_row,nbr_column)
    bool = false
    start_x = div(nbr_row-1,3)*3+1
    start_y = div(nbr_column-1,3)*3+1
    for i in start_x:start_x+2
        for j in start_y:start_y+2
            if length(bigMatrix[i][j])==1 && (nbr_column != j || nbr_row!=i)
                u = length(vect)
                filter!(x -> x != bigMatrix[i][j][1], vect)
                bool =  length(vect) != u
            end
        end
    end
    return bool
end

function SimpleCheck!(bigMatrix)
    bool = false
    for (i,row) in enumerate(bigMatrix)
        for (j,elem) in enumerate(row)
            bool_row = checkRow!(elem,row,j)
            column = [row[j] for row in bigMatrix]
            #println(column)
            bool_col = checkColumn!(elem,column,i)
            bool_square = checkSquare!(elem,bigMatrix,i,j)
            if bool_col || bool_row || bool_square
                bool = true
            end
        end
    end
    return bigMatrix, bool
end


function getSol(sudokuGrid)
    biggerMatrix = []
    for elem in sudokuGrid
        row = []
        for nbr in elem
            if nbr != 0
                push!(row, [nbr])
            else
                push!(row, [1,2,3,4,5,6,7,8,9])
            end
        end
        push!(biggerMatrix,row)
    end
    bool = true
    while bool
        _,bool = SimpleCheck!(biggerMatrix)
    end
    return computing(biggerMatrix)
end

function impossible(bigMatrix)
    for elem in bigMatrix
        for vect in elem
            if length(vect) == 0
                return true
            end
        end
    end
    return false
end

function finished(bigMatrix)
    count = 0
    for elem in bigMatrix
        for vect in elem
            count += 1*(length(vect)==1)
        end
    end
    return count == 81
end
function computing(bigMatrix)
    if finished(bigMatrix)
        return bigMatrix
    elseif impossible(bigMatrix)
        return nothing
    else
        min_len = 10
        x = 1
        y = 1
        for (i,row) in enumerate(bigMatrix)
            for (j,elem) in enumerate(row)
                if length(elem) < min_len && length(elem) >= 2
                    min_len = length(elem)
                    x = i
                    y = j
                end
            end
        end

        for nbr in bigMatrix[x][y]
            m = deepcopy(bigMatrix)
            m[x][y] = [nbr]
            bool = true
            count = 0
            while bool
                _,bool = SimpleCheck!(m)
                count += 1
            end
            if computing(m) !== nothing
                return computing(m)
            end
        end
        return nothing
    end
end

function fund(bigMatrix)
    elem = string(string(bigMatrix[1][1][1]),string(bigMatrix[1][2][1]), string(bigMatrix[1][3][1]))
    println(elem)
    return parse(Int, elem)
end

function main()
    sudokus = getSudoku("sudoku.txt")
    S = 0
    println("======================================================================")
    for sudo in sudokus
        big = getSol(sudo)
        S += fund(big)
        println(S)
    end
    println(S)

end

main()