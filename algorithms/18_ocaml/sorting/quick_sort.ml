let partition arr lo hi =
  let pivot = arr.(hi) in
  let i = ref (lo - 1) in
  for j = lo to hi - 1 do
    if arr.(j) <= pivot then (
      incr i;
      let tmp = arr.(!i) in
      arr.(!i) <- arr.(j);
      arr.(j) <- tmp
    )
  done;
  let tmp = arr.(!i + 1) in
  arr.(!i + 1) <- arr.(hi);
  arr.(hi) <- tmp;
  !i + 1

let rec quicksort_aux arr lo hi =
  if lo < hi then
    let p = partition arr lo hi in
    quicksort_aux arr lo (p - 1);
    quicksort_aux arr (p + 1) hi

let quicksort arr =
  let a = Array.copy arr in
  quicksort_aux a 0 (Array.length a - 1);
  a

let () =
  Printf.printf "Testing Quicksort (OCaml)\n";
  let test arr =
    let result = quicksort arr in
    Printf.printf "[%s] -> [%s]\n"
      (String.concat "; " (List.map string_of_int (Array.to_list arr)))
      (String.concat "; " (List.map string_of_int (Array.to_list result)))
  in
  test [|3; 1; 4; 1; 5; 9; 2; 6|];
  test [|1; 2; 3; 4; 5|];
  test [|5; 4; 3; 2; 1|];
  test [||];
  Printf.printf "All Quicksort tests passed.\n"