function arr = bubble_sort(arr)
% BUBBLE_SORT Sorts an array using standard bubble sort algorithm
    n = length(arr);
    for i = 1:(n - 1)
        for j = 1:(n - i)
            if arr(j) > arr(j + 1)
                temp = arr(j);
                arr(j) = arr(j + 1);
                arr(j + 1) = temp;
            end
        end
    end
end
