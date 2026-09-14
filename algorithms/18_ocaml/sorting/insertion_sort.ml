let insertion_sort arr =
  let a = Array.copy arr in
  for i = 1 to Array.length a - 1 do
    let key = a.(i) in
    let j = ref (i - 1) in
    while !j >= 0 && a.(!j) > key do
      a.(!j + 1) <- a.(!j);
      decr j
    done;
    a.(!j + 1) <- key
  done;
  a

let () =
  let data = [|33; 7; 91; 12; 5; 5; 78; 2; 44; 19|] in
  let expected = Array.copy data in
  Array.sort compare expected;
  assert (insertion_sort data = expected);
  Printf.printf "[OCaml InsertionSort] Insertion sort verified\n"
