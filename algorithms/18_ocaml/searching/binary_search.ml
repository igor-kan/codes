let binary_search arr target =
  let lo = ref 0 in
  let hi = ref (Array.length arr - 1) in
  let result = ref (-1) in
  while !lo <= !hi && !result = -1 do
    let mid = (!lo + !hi) / 2 in
    if arr.(mid) = target then result := mid
    else if arr.(mid) < target then lo := mid + 1
    else hi := mid - 1
  done;
  !result

let () =
  let arr = [|1; 3; 5; 7; 9; 11; 13|] in
  assert (binary_search arr 7 = 3);
  assert (binary_search arr 8 = -1);
  assert (binary_search arr 1 = 0);
  Printf.printf "[OCaml BinarySearch] Binary search verified\n"
