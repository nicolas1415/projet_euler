using Combinatorics

function S(space)
    return sum(space)
end


function get_subindices(n, k)
    return collect(combinations(1:n, k))
end

function get_elements_by_subindices(arr, subindices)
    return [arr[idx] for idx in subindices]
end

function test(space)
    n = length(space)
    p = div(n,2)
    for k in 1:(n-1)
        indexes = get_subindices(n,k)
        for index_list in indexes
            B = []
            C = []
            left_index = []
            for j in 1:n
                if j in index_list
                    push!(B,space[j])
                else
                    push!(C,space[j])
                    push!(left_index,j)
                end
            end
            
            for i in 1:(n-k)
                new_indexes = collect(combinations(left_index,i))
                for new_indexe in new_indexes
                    D = [space[l] for l in new_indexe]

                    if S(B) == S(D)
                        return false
                    elseif 1*(S(B)>= S(D) && k<i) + 1*(S(B)<= S(D) && k>i) > 0
                        return false
                    end
                end
            end
            
        end
    end
    return true
end

function voisin(A)
    n = length(A)
    vois = []
    for a in -1:1
        for b in -1:1
            for c in -1:1
                for d in -1:1
                    for e in -1:1
                        for f in -1:1
                            for g in -1:1
                                if a!=0 || b!=0 || c!=0 || d!=0 || e!=0 || f!=0 || g!=0
                                    B = deepcopy(A)
                                    B[1] += a
                                    B[2] += b
                                    B[3] += c
                                    B[4] += d
                                    B[5] += e
                                    B[6] += f
                                    B[7] += g
                                    if test(B)
                                        push!(vois,B)
                                    end
                                end
                            end
                        end
                    end
                end
            end
        end
    end
    return vois
end

println(test([20,31,38,39,40,42,45]))

A = [20,31,38,39,40,42,45]

indice = 0
tabou = Set()
push!(tabou, [A,S(A)])
while indice < 20
    global indice += 1
    B = voisin(A)
    println(B)
    min = 1000
    elem = deepcopy(B[1])
    for C in B
        if S(C)<min
            min = S(C)
            elem = deepcopy(C)
        end
    end
    global A = deepcopy(elem)
    push!(tabou,[elem,S(elem)])
end

println(tabou)