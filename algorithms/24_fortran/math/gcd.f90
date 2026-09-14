module math_mod
  implicit none
contains
  recursive function gcd(a, b) result(res)
    integer, intent(in) :: a, b
    integer :: res
    if (b == 0) then
      res = a
    else
      res = gcd(b, mod(a, b))
    end if
  end function gcd

  function lcm(a, b) result(res)
    integer, intent(in) :: a, b
    integer :: res
    res = (a / gcd(a, b)) * b
  end function lcm
end module math_mod
