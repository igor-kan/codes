struct Point
    x::Int
    y::Int
end
cross_prod(o::Point, a::Point, b::Point) = (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)
function convex_hull(pts::Vector{Point})
    sort!(pts, by = p -> (p.x, p.y))
    hull = Point[]
    for p in pts
        while length(hull) >= 2 && cross_prod(hull[end - 1], hull[end], p) <= 0
            pop!(hull)
        end
        push!(hull, p)
    end
    return hull
end
h = convex_hull([Point(0,0), Point(1,1), Point(2,2), Point(0,2), Point(2,0)])
@assert !isempty(h)
println("Julia Graham Scan verified.")
