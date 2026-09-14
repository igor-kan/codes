// Effective C++ -- rule of zero: let the compiler generate special members.
#include <iostream>
#include <memory>
#include <string>
#include <vector>

class Document {
  public:
    Document(std::string title, std::vector<std::string> paragraphs)
        : title_(std::move(title)), paragraphs_(std::move(paragraphs)) {}

    const std::string &title() const { return title_; }
    std::size_t size() const { return paragraphs_.size(); }

  private:
    std::string title_;
    std::vector<std::string> paragraphs_;
};

int main() {
    Document doc("Interview", {"one", "two", "three"});
    Document copy = doc;  // compiler-generated copy is correct
    std::cout << copy.title() << ' ' << copy.size() << '\n';
    return 0;
}
