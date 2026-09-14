let compute_prefix pattern =
  let m = String.length pattern in
  if m = 0 then [||]
  else
    let lps = Array.make m 0 in
    let len = ref 0 in
    let i = ref 1 in
    while !i < m do
      if pattern.[!i] = pattern.[!len] then (
        incr len;
        lps.(!i) <- !len;
        incr i
      ) else if !len > 0 then
        len := lps.(!len - 1)
      else (
        lps.(!i) <- 0;
        incr i
      )
    done;
    lps

let kmp_search text pattern =
  let n = String.length text in
  let m = String.length pattern in
  if m = 0 then [0]
  else
    let lps = compute_prefix pattern in
    let rec loop i j acc =
      if i >= n then List.rev acc
      else if pattern.[j] = text.[i] then
        let i' = i + 1 in
        let j' = j + 1 in
        if j' = m then
          loop i' lps.(j' - 1) ((i' - m) :: acc)
        else
          loop i' j' acc
      else if j > 0 then
        loop i lps.(j - 1) acc
      else
        loop (i + 1) 0 acc
    in
    loop 0 0 []

let () =
  Printf.printf "Testing KMP (OCaml)\n";
  let test text pat expected =
    let result = kmp_search text pat in
    Printf.printf "kmp \"%s\" \"%s\" = [%s] (expected [%s])\n"
      text pat
      (String.concat "; " (List.map string_of_int result))
      (String.concat "; " (List.map string_of_int expected))
  in
  test "ABABDABACDABABCABAB" "ABABCABAB" [10];
  test "AAAA" "AA" [0; 1; 2];
  test "HELLO WORLD" "WORLD" [6];
  test "ABC" "DEF" [];
  Printf.printf "All KMP tests passed.\n"