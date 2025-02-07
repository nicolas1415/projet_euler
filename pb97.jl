

n = 28433
m = 7830457

function gettingPower(adding::Int,power::Int)
    elem::BigInt =  1
    lst = []
    while power != 0
        push!(lst,power%2)
        power = div(power,2)
    end

    p = length(lst)

    for i in 1:p
        if lst[p-i+1] == 0
            elem = (elem*elem)%10000000000
        else
            elem = (2*elem*elem)%10000000000

        end
    end
    return (adding*elem +1)%10000000000
end

println(gettingPower(n,m))