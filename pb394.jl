

function model_bite(frac::BigFloat)
    size::BigFloat = 1.0
    count::Int = 0
    while size >= frac
        X1 = rand()
        X2 = rand()
        Z = min(X1,X2)
        Z = BigFloat(Z)
        size *= Z
        count += 1
    end
    return count
end

function monte_carlo(frac::BigFloat, aprox::Int)
    Y = 0
    for i in 1:aprox
        X = model_bite(frac)
        Y+=X
    end
    return Y/aprox   
end

println(monte_carlo(BigFloat(0.5),10000000))
