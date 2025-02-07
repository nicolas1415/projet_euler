

struct Point
    x::Int
    y::Int

    function Point(x::Int, y::Int)
        new(x, y)
    end
end

Base.:+(p1::Point,p2::Point) = Point(p1.x+p2.x,p1.y+p2.y)
Base.:-(p1::Point,p2::Point) = Point(p1.x-p2.x,p1.y-p2.y)
Base.:*(p1::Point,p2::Point) = BigInt(p1.x)*BigInt(p2.x) + BigInt(p1.y)*BigInt(p2.y)

struct Triangle
    A::Point
    B::Point
    C::Point

    function Triangle(A::Point,B::Point, C::Point)
        new(A,B,C)
    end
end

function getData(PATH::String)
    file = open(PATH,"r")
    lst_triangle = Triangle[]
    lines = readlines(file)
    for line in lines
        numbers = parse.(Int, split(line, ','))
        A::Point=Point(numbers[1],numbers[2])
        B::Point=Point(numbers[3],numbers[4])
        C::Point=Point(numbers[5],numbers[6])
        Tri::Triangle=Triangle(A,B,C)
        push!(lst_triangle,Tri)
    end
    return lst_triangle
end

function goodSide(A::Point,B::Point,C::Point)::Bool
    u = B - A
    v = Point(u.y,-u.x)


    last_point = C - A
    origin = Point(0,0)-A


    return (last_point*v)*(origin*v)>=0
end


function checkTriangle(Tri::Triangle)::Bool
    if goodSide(Tri.A,Tri.B,Tri.C) && goodSide(Tri.B,Tri.C,Tri.A) && goodSide(Tri.C,Tri.A,Tri.B)
        return true
    end
    return false
end

function main()
    triangles = getData("triangles.txt")
    count = 0
    for triangle in triangles
        if checkTriangle(triangle)
            count += 1
        end
    end
    print("Number of triangles that contain the origin : ")
    println(count)
    Tri = triangles[2]
    println(checkTriangle(Tri))
end

main()