// A Tour of C++ -- RAII and resource ownership.
#include <cstdio>
#include <iostream>
#include <stdexcept>

class File {
  public:
    explicit File(const char *path) : handle_(std::fopen(path, "w")) {
        if (!handle_) throw std::runtime_error("cannot open file");
    }
    ~File() { if (handle_) std::fclose(handle_); }
    File(const File &) = delete;
    File &operator=(const File &) = delete;

    void write(const char *text) { std::fputs(text, handle_); }

  private:
    std::FILE *handle_;
};

int main() {
    try {
        File file("raii_demo.txt");
        file.write("RAII guarantees cleanup\n");
    } catch (const std::exception &e) {
        std::cerr << e.what() << '\n';
        return 1;
    }
    std::cout << "file written\n";
    return 0;
}
