

function test(k,n)
    return 2*k*(k-1) == n*(n-1)
end

function find(n)
    dep = round(convert(Int, 0.7*n))
    println(dep)
    fin = round(convert(Int, 0.8*n))
    for k in dep:fin
        if test(k,n)
            return k
        end
    end
    return false
end

println(find(21))