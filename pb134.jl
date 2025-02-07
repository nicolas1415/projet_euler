
struct SpecialNumber
    n::BigInt
    rad::BigInt

    function SpecialNumber(n::Int, primes)
        rad_val = rad(n, primes)
        new(BigInt(n), BigInt(rad_val))
    end
end

function rad(n, primes)
    values = []
    for prime in primes
        if n % prime == 0
            push!(values, prime)
        elseif prime > n
            break
        end
    end
    prod = 1
    for value in values
        prod *= value
    end
    return prod
end

import Base: <
# Define the < operator without specifying Base
function <(a::SpecialNumber, b::SpecialNumber)
    if a.rad == b.rad
        return a.n < b.n
    else
        return a.rad < b.rad
    end
end

function ComputePrimes(n)
    elem = fill(true, n)
    elem[1] = false
    for i in 2:n
        if elem[i]
            value = 2 * i
            while value <= n
                elem[value] = false
                value += i
            end
        end
    end
    primes = []
    for (prime, bool) in enumerate(elem)
        if bool
            push!(primes, prime)
        end
    end
    return primes
end

function binarySearch!(vect,number::SpecialNumber,first,last)
    if first==last
        insert!(vect,first,number)
    else
        n = last-first+1
        p = div(n,2)
        if vect[first+p-1] > number
            binarySearch!(vect,number,first,first + p-1)
        else
            binarySearch!(vect,number,first + p,last)
        end
    end
end


function main(limit, index)
    primes = ComputePrimes(limit)
    println("hello world")
    SortedVect = []
    for i in 1:limit
        nbr = SpecialNumber(i, primes)
        if !(length(SortedVect)>index && nbr > SortedVect[end])
            binarySearch!(SortedVect,nbr,1,length(SortedVect)+1)
        end
    end
    println(SortedVect[index])
end

main(Int(1e5), Int(1e4))
