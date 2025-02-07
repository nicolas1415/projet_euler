



function get_value(top)
    hist = fill(0,top)
    println("HELOO")
    for a in 3:(top-1)
        n = minimize(top-a,a-1)
        for b in 2:n
            elem = Int((a+b)*(a-b))
            print("hello")
            println(elem)
            if elem <= top
                hist[elem] += 1
            end
        end
    end
    println(hist)
    return hist
end


function main()
    top = 100
    histo = fill(0,100)
    get_value(top)
    #print(histo)
end 

main()