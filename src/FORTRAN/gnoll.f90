program main
    interface
        function roll_and_write(s, f) bind(c, name="roll_and_write")
            import :: C_CHAR
            character(kind=C_CHAR), dimension(*), intent(in) :: s, f
            integer :: roll_and_write
        end function roll_and_write
    end interface
    
    character(len=100) :: s, f
    integer :: result
    
    s = "d20"
    f = "output.die"
    
    result = roll_and_write(s, f)
    print *, "Result:", result
end program main
