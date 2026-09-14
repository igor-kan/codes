let selection_sort arr =
  let a = Array.copy arr in
  let n = Array.length a in
  for i = 0 to n - 2 do
    let min_idx = ref i in
    for j = i + 1 to n - 1 do
      if a.(j) < a.(!min_idx) then min_idx := j
    done;
    let tmp = a.(i) in
    a.(i) <- a.(!min_idx);
    a.(!min_idx) <- tmp
  done;
  a

let () =
  let data = [|33; 7; 91; 12; 5; 5; 78; 2; 44; 19|] in
  let expected = Array.copy data in
  Array.sort compare expected;
  assert (selection_sort data = expected);
  Printf.printf "[OCaml SelectionSort] Selection sort verified\n"
