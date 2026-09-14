// RAII locking with std::lock_guard and std::scoped_lock.
#include <iostream>
#include <mutex>

class Account {
  public:
    explicit Account(long balance) : balance_(balance) {}
    long balance() const { return balance_; }

    friend void transfer(Account &from, Account &to, long amount) {
        std::scoped_lock lock(from.mtx_, to.mtx_);  // deadlock-free ordering
        if (from.balance_ < amount) return;
        from.balance_ -= amount;
        to.balance_ += amount;
    }

  private:
    mutable std::mutex mtx_;
    long balance_;
};

int main() {
    Account a(100), b(0);
    transfer(a, b, 30);
    std::cout << a.balance() << ' ' << b.balance() << '\n';
    return (a.balance() == 70 && b.balance() == 30) ? 0 : 1;
}
