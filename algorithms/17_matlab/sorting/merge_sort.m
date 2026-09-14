function arr = merge_sort(arr)
% MERGE_SORT Sorts array using divide and conquer
    if length(arr) <= 1
        return;
    end
    mid = floor(length(arr) / 2);
    left = merge_sort(arr(1:mid));
    right = merge_sort(arr(mid+1:end));
    
    arr = [];
    i = 1; j = 1;
    while i <= length(left) && j <= length(right)
        if left(i) <= right(j)
            arr = [arr, left(i)]; i = i + 1;
        else
            arr = [arr, right(j)]; j = j + 1;
        end
    end
    if i <= length(left), arr = [arr, left(i:end)]; end
    if j <= length(right), arr = [arr, right(j:end)]; end
end
