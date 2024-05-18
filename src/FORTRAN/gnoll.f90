program main
    use, intrinsic :: iso_c_binding, only: c_char, c_int
    implicit none

    interface
        function roll_and_write(s, f) bind(c, name="roll_and_write")
            import :: c_char, c_int
            character(kind=c_char), dimension(*), intent(in) :: s, f
            integer(c_int) :: roll_and_write
        end function roll_and_write
    end interface

    character(len=4, kind=c_char), target :: s
    character(len=11, kind=c_char), target :: f
    integer(c_int) :: result

    s = 'd20'C
    f = 'output.die'C

    result = roll_and_write(s, f)
    print *, "Result:", result
end program main
