// Effective C++ -- const every-where it applies.
#include <iostream>
#include <string>
#include <vector>

class Account {
  public:
    explicit Account(std::string owner) : owner_(std::move(owner)) {}
    const std::string &owner() const { return owner_; }
    double balance() const noexcept { return balance_; }
    void deposit(double amount) {
        if (amount > 0) balance_ += amount;
    }
    // const overload returns a read-only view
    const std::vector<double> &history() const { return history_; }
    void record(double amount) { history_.push_back(amount); }

  private:
    std::string owner_;
    double balance_ = 0;
    std::vector<double> history_;
};

int main() {
    const Account account("ada");
    std::cout << account.owner() << ' ' << account.balance() << '\n';
    return 0;
}
