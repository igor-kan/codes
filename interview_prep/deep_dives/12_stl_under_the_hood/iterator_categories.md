# Iterator Categories

| Category | Supports | Examples |
|:---|:---|:---|
| Input | single-pass read | `istream_iterator` |
| Output | single-pass write | `ostream_iterator` |
| Forward | multi-pass, `++` | `forward_list` |
| Bidirectional | `++` and `--` | `list`, `map` |
| Random access | `+`, `-`, `[]`, ordering | `vector`, `deque`, `array` |
| Contiguous (C++20) | adjacent in memory | `vector`, `array`, `string` |

## Why it matters

Algorithms dispatch on the strongest category to pick the best implementation
(e.g. `std::advance` and `std::sort` need random access). Contiguous iterators
enable pointer-like optimizations and safe `span` conversions.

## Tags

`iterator_traits<It>::iterator_category` communicates the category; custom
iterators must supply it (or model the C++20 `std::input_iterator` concepts).
