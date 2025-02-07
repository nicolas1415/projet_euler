using LinearAlgebra

function getData(PATH::String)
    file = open(PATH,"r")
    lines = readlines(file)
    Matrix = []
    for line in lines
        line = replace(line, r"-" => "10000")
        numbers = parse.(Int, split(line, ','))
        line_matrix = []
        for number in numbers
            push!(line_matrix, number)
        end
        push!(Matrix, line_matrix)
    end
    return Matrix
end

function gettingIndice(matrix)
    elem = 1000
    x = 1
    y = 1
    for i in 1:40
        for j in 1:40
            if matrix[i][j]<elem
                x = i 
                y = j
                elem = matrix[i][j]
            end
        end
    end
    return [x,y]
end

function count(matrix)
    count = 0
    for i in 1:39
        for j in i+1:40
            if matrix[i][j] < 1000
                count += matrix[i][j]
            end
        end
    end
    return count
end

function main()
    matrix = getData("graph.txt")
    flat_mat = hcat(matrix)
    lst_graphs = []
    vertices = Set()
    S = 0
    c = count(flat_mat)
    stop_feature = 0
    while (stop_feature < 39)
        println(stop_feature)
        index = gettingIndice(flat_mat)
        vertice_first, vertice_last = index[1],index[2]
        elem = flat_mat[vertice_first][vertice_last]
        flat_mat[vertice_first][vertice_last] = 1000
        flat_mat[vertice_last][vertice_first] = 1000
        elem_first = 0
        elem_last = 0
        for (index,vertices) in enumerate(lst_graphs)
            if vertice_first in vertices
                elem_first = index
            end
            if vertice_last in vertices
                elem_last = index
            end
        end
        if elem_first == 0 && elem_last == 0
            new_vertices = Set()
            push!(new_vertices,vertice_first)
            push!(new_vertices,vertice_last)
            push!(lst_graphs,new_vertices)
            stop_feature += 1
            S += elem
        elseif elem_first == 0
            push!(lst_graphs[elem_last], vertice_first)
            stop_feature += 1
            S += elem
        elseif elem_last == 0
            push!(lst_graphs[elem_first], vertice_last)
            stop_feature += 1
            S += elem
        elseif elem_first != elem_last
            if elem_first < elem_last
                union!(lst_graphs[elem_first], lst_graphs[elem_last])
                splice!(lst_graphs, elem_last)
                stop_feature += 1
                S += elem
            else
                union!(lst_graphs[elem_last], lst_graphs[elem_first])
                splice!(lst_graphs, elem_first)
                stop_feature += 1
                S += elem
            end
        end
    end
    print("the optimum sum is : ")
    println(c-S)
end

main()

