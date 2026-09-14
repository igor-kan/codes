// Minimal std::tuple via recursive inheritance and structured-like access.
#pragma once
#include <cstddef>
#include <utility>

namespace mystl {

template <std::size_t I, typename T>
struct tuple_leaf {
    T value;
};

template <typename, typename... Ts>
struct tuple_impl;

template <std::size_t... Is, typename... Ts>
struct tuple_impl<std::index_sequence<Is...>, Ts...> : tuple_leaf<Is, Ts>... {
    tuple_impl() = default;
    explicit tuple_impl(Ts... values) : tuple_leaf<Is, Ts>{values}... {}
};

template <typename... Ts>
class tuple : public tuple_impl<std::index_sequence_for<Ts...>, Ts...> {
    using base = tuple_impl<std::index_sequence_for<Ts...>, Ts...>;
  public:
    tuple() = default;
    explicit tuple(Ts... values) : base(values...) {}
};

template <std::size_t I, typename T>
T &get(tuple_leaf<I, T> &leaf) { return leaf.value; }

}  // namespace mystl
