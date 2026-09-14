function lps = compute_lps(pattern)
% COMPUTE_LPS Computes the LPS (longest proper prefix-suffix) array
    m = length(pattern);
    lps = zeros(1, m);
    len = 0;
    i = 2;
    while i <= m
        if pattern(i) == pattern(len + 1)
            len = len + 1;
            lps(i) = len;
            i = i + 1;
        else
            if len > 0
                len = lps(len);
            else
                lps(i) = 0;
                i = i + 1;
            end
        end
    end
end

function indices = kmp_search(text, pattern)
% KMP_SEARCH Knuth-Morris-Pratt string matching
    n = length(text);
    m = length(pattern);
    lps = compute_lps(pattern);
    i = 1;
    j = 1;
    indices = [];
    while i <= n
        if pattern(j) == text(i)
            i = i + 1;
            j = j + 1;
        end
        if j == m + 1
            indices = [indices, i - j + 1];
            j = lps(j - 1) + 1;
        elseif i <= n && pattern(j) ~= text(i)
            if j > 1
                j = lps(j - 1) + 1;
            else
                i = i + 1;
            end
        end
    end
end

function test_kmp()
    fprintf('[Matlab KMP] Testing KMP string matching\n');
    r = kmp_search('ABABDABACDABABCABAB', 'ABABCABAB');
    fprintf('Pattern found at: ');
    fprintf('%d ', r);
    fprintf('(expected 11)\n');
    r = kmp_search('AAAA', 'AA');
    fprintf('Pattern found at: ');
    fprintf('%d ', r);
    fprintf('(expected 1 2 3)\n');
    r = kmp_search('HELLO WORLD', 'WORLD');
    fprintf('Pattern found at: ');
    fprintf('%d ', r);
    fprintf('(expected 7)\n');
    fprintf('[Matlab KMP] Test completed.\n');
end