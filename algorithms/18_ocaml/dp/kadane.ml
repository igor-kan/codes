let kadane arr =
  let n = Array.length arr in
  let best = ref arr.(0) in
  let cur = ref arr.(0) in
  for i = 1 to n - 1 do
    cur := max arr.(i) (!cur + arr.(i));
    best := max !best !cur
  done;
  !best

let () =
  assert (kadane [|-2; 1; -3; 4; -1; 2; 1; -5; 4|] = 6);
  assert (kadane [|-5; -2; -3|] = -2);
  Printf.printf "[OCaml Kadane] Maximum subarray sum verified\n"
