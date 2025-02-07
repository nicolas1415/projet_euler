
struct Frac
    num::Int
    den::Int

    function Frac(num::Int, den::Int)
        new(num, den)
    end
end

function simplify(frac::Frac)
    x, y = frac.num, frac.den
    while y != 0
        x, y = y, x % y
    end
    gcd_val = x
    return Frac(frac.num ÷ gcd_val, frac.den ÷ gcd_val)
end

function verify(frac::Frac)
    return frac.num == 1
end


Base.:+(fr1::Frac,fr2::Frac) = simplify(Frac(fr1.num*fr2.den + fr2.num*fr1.den, fr1.den*fr2.den))
Base.:-(fr1::Frac,fr2::Frac) = simplify(Frac(fr1.num*fr2.den - fr2.num*fr1.den, fr1.den*fr2.den))


function main()
    n = 2
    while true
        count = 0
        base_frac::Frac = Frac(1,n)
        for x in (n+1):(2*n)
            if verify(base_frac-Frac(1,x))
                count+=1
            end
        end
        if count >= 1000
            break
        end
        if n%1000 == 0
            print("processing, value of count : ")
            println(count)
        end
        n+=1
    end
    print("found n value : ")
    print(n)
end

main()
