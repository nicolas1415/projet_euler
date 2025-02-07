
function T(a,b)
    if a > b
        return T(b,a)
    elseif a == 1
        return 1*(b%2 == 0)
    else
        a_prime = div(a,2)
        b_prime = div(b,2)
        return T(a_prime,b)*T(a-a_prime,b) + T(a, b_prime)*T(a,b-b_prime) - T(a_prime,b_prime)*T(a-a_prime,b-b_prime)*T(a-a_prime,b_prime)*T(a_prime,b-b_prime)
    end
end

println(T(2,3))