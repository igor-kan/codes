let lis arr =
  let n = Array.length arr in
  if n = 0 then 0
  else begin
    let dp = Array.make n 1 in
    for i = 1 to n - 1 do
      for j = 0 to i - 1 do
        if arr.(j) < arr.(i) then
          dp.(i) <- max dp.(i) (dp.(j) + 1)
      done
    done;
    Array.fold_left max 0 dp
  end

let () =
  assert (lis [|10; 9; 2; 5; 3; 7; 101; 18|] = 4);
  assert (lis [||] = 0);
  Printf.printf "[OCaml LIS] Longest increasing subsequence verified\n"
