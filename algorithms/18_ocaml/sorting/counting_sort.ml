let counting_sort arr =
  if Array.length arr = 0 then [||]
  else begin
    let mx = Array.fold_left max arr.(0) arr in
    let count = Array.make (mx + 1) 0 in
    Array.iter (fun x -> count.(x) <- count.(x) + 1) arr;
    for i = 1 to mx do
      count.(i) <- count.(i) + count.(i - 1)
    done;
    let out = Array.make (Array.length arr) 0 in
    for k = Array.length arr - 1 downto 0 do
      let x = arr.(k) in
      count.(x) <- count.(x) - 1;
      out.(count.(x)) <- x
    done;
    out
  end

let () =
  let data = [|4; 2; 2; 8; 3; 3; 1|] in
  let expected = Array.copy data in
  Array.sort compare expected;
  assert (counting_sort data = expected);
  Printf.printf "[OCaml CountingSort] Counting sort verified\n"
