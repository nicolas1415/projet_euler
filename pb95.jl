

function amicable(number::Int)
    Sum = 0
    n = div(number,2)
    for i in 1:n
        if number%i == 0
            Sum+=i
        end
    end
    return Sum
end

#println(amicable(220))

function main(limit::Int)
    amicable_dict = Dict()
    amicable_dict["1"] = 1
    max_len = 1
    ini_nbr = 1
    for elem_dep in 1:limit
        nbr_string = string(elem_dep)
        has_nbr = haskey(amicable_dict,nbr_string)
        if has_nbr
            value = amicable_dict[nbr_string]
        else
            empty_set = Set()
            first_nbr = elem_dep
            nbr_last = amicable(first_nbr)
            push!(empty_set,first_nbr)
            while !(nbr_last in empty_set)
                push!(empty_set,nbr_last)
                if nbr_last > limit || haskey(amicable_dict,string(nbr_last))
                    amicable_dict[nbr_string] = 0
                    break
                end
                nbr_last = amicable(nbr_last)
            end
            if first_nbr == nbr_last
                amicable_dict[nbr_string] = length(empty_set)
            else
                amicable_dict[nbr_string] = 0
            end
            value = amicable_dict[nbr_string]
        end

        if value > max_len
            max_len = value
            ini_nbr = elem_dep
        end

    end
    println(max_len)
    println(ini_nbr)
end

main(1000000)