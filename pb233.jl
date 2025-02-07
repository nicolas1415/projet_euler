
function ComputePrimes(n)
    elem = fill(true,n)
    elem[1] = false
    for i in 2:n
        if elem[i]
            value = 2*i
            while value <= n
                elem[value] = false
                value += i
            end
        end
    end
    primes = []
    for (prime,bool) in enumerate(elem)
        if bool
            push!(primes,prime)
        end
    end
    return primes
end

function f(N)
    count = 0
    if N%4 == 0
        return f(div(N,2))
    else
        elem = div(N,2)
        dep = Int(ceil(elem*(1-sqrt(2))))
        fin = elem-1
        for x in dep:fin
            delta = 2*elem^2 - (x-elem)^2
            if sqrt(delta) == floor(sqrt(delta))
                count += 1
            end
        end
        return count
    end
end

function other_F(N)
    if N == 1
        return -1
    elseif N== 2
        return 1
    elseif N%2 == 0
        return other_F(div(N,2))
    else
        return other_F(div(N,2)) + 2
    end
end

function find(N)
    count = 0
    max = Int(floor((sqrt(2)-1)*N))
    for j in 1:max
        k = j+1
        while k <= div(N,2)
            if N*(k-j) == k^2 + j^2
                count += 1
            end
            k+=1
        end
    end
    return 1+2*count
end



function selectDepnbr(limit)
    m = div(limit,5^3*13^2)
    primes = ComputePrimes(m)
    true_primes = []
    false_primes = []
    for prime in primes
        if find(prime)> 1
            push!(true_primes,prime)
        else
            push!(false_primes, prime)
        end
    end
    println("got important primes")
    #println(true_primes)
    numbers = []
    elem = 0
    elem2 = 0
    for (index1,prime1) in enumerate(true_primes)
        for (index2, prime2) in enumerate(true_primes)
            elem = index2
            if index1!=index2
                nbr = BigInt(prime1^7*prime2^3)
                if nbr <= limit
                    push!(numbers,nbr)
                else
                    break
                end
            end
        end
        if elem == 1
            break
        end
    end
    for (index1,prime1) in enumerate(true_primes)
        for (index2, prime2) in enumerate(true_primes)
            elem = index2
            if index1!=index2
                nbr = BigInt(prime1^10*prime2^2)
                if nbr <= limit
                    push!(numbers,nbr)
                else
                    break
                end
            end
        end
        if elem == 1
            break
        end
    end
    for (index1,prime1) in enumerate(true_primes)
        if prime1^3 >= div(limit,13*5^2)
            break
        end
        for (index2, prime2) in enumerate(true_primes)
            if prime2^2 >= div(limit,5^3*13)
                break
            end
            for (index3,prime3) in enumerate(true_primes)
                if index1!=index2 && index1!=index3 && index2!=index3
                    elem2 = index3
                    nbr = BigInt(prime1^3*prime2^2*prime3)
                    if nbr <= limit
                        push!(numbers,nbr)
                    else
                        break
                    end
                end
            end
        end
    end
    println(true_primes)
    return numbers,true_primes, false_primes
end

function main(limit::BigInt)
    dep, primes, bad_primes = selectDepnbr(limit)
    S = BigInt(0)
    max_index = div(limit,5^3*13^2*17)
    p = length(primes)
    println(length(dep))
    println(p)
    indexes = [1]
    println(max_index)
    for i in 2:max_index
        k = 1
        while k <= p
            if i%primes[k] == 0
                push!(indexes, 0)
                break
            elseif i < primes[k]
                push!(indexes, i)
                break
            end
            k+=1
        end
        if k == p+1
            push!(indexes,i)
        end
        println(indexes)
    end
    for d in dep
        m = div(limit,d)
        S+= d*sum(indexes[1:m])
    end
    println(S)
end

main(BigInt(10^7))