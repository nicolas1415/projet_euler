
import Base: isless

struct ExpNum
    num::Float64
    exp::Float64
end

function ExpNum(num, exp)
    return ExpNum(num, exp)
end

Base.isless(a::ExpNum, b::ExpNum) = log(a.num) * a.exp < log(b.num) * b.exp




PATH = "base_data.txt"

content = open(PATH, "r") do file
    read(file,String)
end


lines = eachline(IOBuffer(content))

max_exp = ExpNum(2.0,11.0)
line_number = 1
indexing = 1

for line in lines
    # Assuming the format is "num exp", split the line
    parts = split(line)
    index = 1
    num = ""
    while parts[index] != ","
        num *= parts[index]
    end
    index += 1
    exp = parts[index:end]
    num = Float(num)
    exp = Float(exp)
    elem = ExpNum(num,exp)

    if max_exp < elem
        max_exp = elem
        line_number = indexing
    end
    indexing +=1
    
end

println(list_of_exp[1])
