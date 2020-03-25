function createArray(L, p) result (array)
    integer, intent(in) :: L
    real, intent(in) :: p
    real, dimension(L, L) :: array
    real :: r = 0
    do i = 0,L
        do j = 0,L
            call random_number(r)
            print *,(r)
            if (r < p) then
                array(i,j) = 1
                print *,(r)
            else
                array(i,j) = 0
                print *,(array(i,j))
            end if
        end do
    end do
end function createArray

program percolation
    print *,(createArray(10, 0.5))
end program percolation
