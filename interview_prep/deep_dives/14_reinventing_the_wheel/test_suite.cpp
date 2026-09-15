// Exercises the from-scratch components.
#include <cassert>
#include <iostream>
#include <string>

#include "custom_optional.hpp"
#include "custom_shared_ptr.hpp"
#include "custom_string.hpp"
#include "custom_unique_ptr.hpp"
#include "custom_vector.hpp"

int main() {
    wheel::Vector<int> v;
    for (int i = 0; i < 5; ++i) v.push_back(i);
    assert(v.size() == 5 && v[4] == 4);

    wheel::Vector<int> moved = std::move(v);
    assert(moved.size() == 5 && v.empty());

    auto unique = wheel::makeUnique<int>(7);
    assert(*unique == 7);

    auto shared = wheel::makeShared<std::string>("hello");
    auto shared2 = shared;
    assert(shared.use_count() == 2 && *shared2 == "hello");

    wheel::String text("hello");
    text += wheel::String(" world");
    assert(text.size() == 11 && std::string(text.c_str()) == "hello world");

    wheel::Optional<int> opt;
    assert(!opt.has_value());
    opt = 9;
    assert(opt.value() == 9 && opt.value_or(0) == 9);

    std::cout << "all reimplemented components passed\n";
    return 0;
}
