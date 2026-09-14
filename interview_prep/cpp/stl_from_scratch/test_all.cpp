// Exercises every from-scratch STL component.
#include <cassert>
#include <iostream>
#include <string>

#include "my_allocator.hpp"
#include "my_function.hpp"
#include "my_optional.hpp"
#include "my_shared_ptr.hpp"
#include "my_span.hpp"
#include "my_string.hpp"
#include "my_tuple.hpp"
#include "my_unique_ptr.hpp"
#include "my_unordered_map.hpp"
#include "my_vector.hpp"

int main() {
    mystl::vector<int> v{1, 2, 3};
    v.push_back(4);
    assert(v.size() == 4 && v[3] == 4);

    mystl::string s("hello");
    s += mystl::string(" world");
    assert(s.size() == 11 && std::string(s.c_str()) == "hello world");

    auto up = mystl::make_unique<int>(42);
    assert(*up == 42 && up);

    auto sp = mystl::make_shared<int>(7);
    auto sp2 = sp;
    assert(sp.use_count() == 2 && *sp2 == 7);

    mystl::optional<int> opt;
    assert(!opt.has_value());
    opt = 5;
    assert(opt.value() == 5 && opt.value_or(0) == 5);

    int raw[] = {10, 20, 30};
    mystl::span<int> view(raw);
    assert(view.size() == 3 && view.back() == 30 && view.subspan(1, 2)[0] == 20);

    mystl::function<int(int, int)> add = [](int a, int b) { return a + b; };
    assert(add(2, 3) == 5);

    mystl::tuple<int, double> t(1, 2.5);
    assert(mystl::get<0>(t) == 1 && mystl::get<1>(t) == 2.5);

    mystl::arena arena(1024);
    int *a = arena.create<int>(99);
    assert(*a == 99 && arena.block_count() == 1);

    mystl::unordered_map<std::string, int> map;
    map.insert("one", 1);
    map.insert("two", 2);
    assert(*map.find("two") == 2 && map.find("three") == nullptr);

    std::cout << "all STL-from-scratch tests passed\n";
    return 0;
}
