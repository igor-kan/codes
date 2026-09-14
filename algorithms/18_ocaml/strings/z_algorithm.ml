let z_algorithm s =
  let n = String.length s in
  let z = Array.make n 0 in
  if n > 0 then z.(0) <- n;
  let l = ref 0 in
  let r = ref 0 in
  for i = 1 to n - 1 do
    (if i <= !r then z.(i) <- min (!r - i + 1) z.(i - !l));
    let rec extend zi =
      if i + zi < n && s.[zi] = s.[i + zi] then extend (zi + 1) else zi
    in
    z.(i) <- extend z.(i);
    if i + z.(i) - 1 > !r then begin
      l := i;
      r := i + z.(i) - 1
    end
  done;
  z

let () =
  assert (z_algorithm "abacaba" = [|7; 0; 1; 0; 3; 0; 1|]);
  Printf.printf "[OCaml ZAlgorithm] Z-algorithm verified\n"
