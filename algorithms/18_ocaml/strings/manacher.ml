let manacher s =
  let t = ref "#" in
  String.iter (fun c -> t := !t ^ String.make 1 c ^ "#") s;
  let t = !t in
  let n = String.length t in
  let p = Array.make n 0 in
  let c = ref 0 in
  let r = ref 0 in
  for i = 0 to n - 1 do
    (if i < !r then
       p.(i) <- min (!r - i) p.(2 * !c - i));
    let rec extend pi =
      if i + pi + 1 < n && i - pi - 1 >= 0 && t.[i + pi + 1] = t.[i - pi - 1]
      then extend (pi + 1)
      else pi
    in
    p.(i) <- extend p.(i);
    if i + p.(i) > !r then begin
      c := i;
      r := i + p.(i)
    end
  done;
  Array.fold_left max 0 p

let () =
  assert (manacher "abba" = 4);
  assert (manacher "racecar" = 7);
  Printf.printf "[OCaml Manacher] Longest palindromic substring verified\n"
