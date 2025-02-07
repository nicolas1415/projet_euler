
using LinearAlgebra

function next_direc_vec(unit_vect, actual_pos)
    M_R = [-1 0;0 1]
    m = - actual_pos[1]/actual_pos[2]
    Passage_matrix = 1/sqrt(1+m^2) * [m -1; 1 m]

    M_star = inv(Passage_matrix)*M_R*Passage_matrix

    return M_star*unit_vect
end

function compute_next_pos(unit_vect, actual_pos)

    a = unit_vect[2]/unit_vect[1]
    b = actual_pos[2] - a*actual_pos[1]

    delta = 4*a^2*b^2 - 4*(4+a^2)*(b^2-100)

    x_sol1 = -a*b + sqrt(delta)/2
    x_sol2 = -a*b + sqrt(delta)/2

    if abs(x_sol1-actual_pos[1])< abs(x_sol2-actual_pos[1])
        return [x_sol2 ,a*x_sol2+b]
    else
        return [x_sol1 , a*x_sol1+b]
    end
end


function main()
    init_vect = [1.4,-9.6] - [0.0, 10.1]
    init_vect = init_vect / norm(init_vect)

    ini_pos = [0.0, 10.1]
    pos = copy(ini_pos)


    pos = compute_next_pos(init_vect,pos)
    count = 1

    while (pos[1]>0.01 || pos[1]<-0.01) && pos[2]<0
        init_vect = next_direc_vec(init_vect,pos)
        pos = compute_next_pos(init_vect,pos)
        count += 1
    end

    println(count-1)
end


main()


