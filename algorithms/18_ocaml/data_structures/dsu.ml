type dsu = {
  mutable parent : int array;
  rank : int array;
}

let make n = { parent = Array.init n (fun i -> i); rank = Array.make n 0 }

let rec find dsu x =
  if dsu.parent.(x) <> x then dsu.parent.(x) <- find dsu dsu.parent.(x);
  dsu.parent.(x)

let union dsu x y =
  let rx = find dsu x in
  let ry = find dsu y in
  if rx <> ry then begin
    if dsu.rank.(rx) < dsu.rank.(ry) then dsu.parent.(rx) <- ry
    else if dsu.rank.(rx) > dsu.rank.(ry) then dsu.parent.(ry) <- rx
    else begin
      dsu.parent.(ry) <- rx;
      dsu.rank.(rx) <- dsu.rank.(rx) + 1
    end
  end

let connected dsu x y = find dsu x = find dsu y

let () =
  let dsu = make 5 in
  union dsu 0 1;
  union dsu 1 2;
  union dsu 3 4;
  assert (connected dsu 0 2);
  assert (not (connected dsu 0 3));
  Printf.printf "[OCaml DSU] Disjoint set union verified\n"
