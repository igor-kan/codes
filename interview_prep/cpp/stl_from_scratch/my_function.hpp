// Minimal std::function using a virtual type-erased callable.
#pragma once
#include <memory>
#include <utility>

namespace mystl {

template <typename Signature>
class function;

template <typename R, typename... Args>
class function<R(Args...)> {
    struct callable_base {
        virtual R invoke(Args... args) = 0;
        virtual ~callable_base() = default;
    };

    template <typename F>
    struct callable_impl final : callable_base {
        explicit callable_impl(F f) : fn(std::move(f)) {}
        R invoke(Args... args) override { return fn(std::forward<Args>(args)...); }
        F fn;
    };

  public:
    function() = default;
    template <typename F>
    function(F f) : impl_(std::make_unique<callable_impl<F>>(std::move(f))) {}

    R operator()(Args... args) const { return impl_->invoke(std::forward<Args>(args)...); }
    explicit operator bool() const noexcept { return impl_ != nullptr; }

  private:
    std::unique_ptr<callable_base> impl_;
};

}  // namespace mystl
