
function memo_counting(n,m,memo)
    if memo[n] != -1
        return memo[n]
    else
        S = 2+memo_counting(n-1,m,memo)
        for i in (n-m-1):-1:1
            S+= memo_counting(i,m,memo)
        end
        memo[n] = S
        return memo[n]
    end
end

function counting(n,m)
    memo = fill(-1,n)
    for i in 1:m
        memo[i]=1
    end
    memo[m]=2
    return memo_counting(n,m,memo)
end


function main()
    n = 50
    while counting(n,50)< 1000000
        n+=1
    end
    println(n)
end

main()
println(counting(57,10))