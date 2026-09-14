// Minimal arena allocator that hands out aligned blocks.
#pragma once
#include <cstddef>
#include <new>
#include <utility>
#include <vector>

namespace mystl {

class arena {
  public:
    explicit arena(std::size_t block_size) : block_size_(block_size) {}
    ~arena() { for (void *block : blocks_) ::operator delete(block); }

    void *allocate(std::size_t bytes, std::size_t alignment = alignof(std::max_align_t)) {
        std::size_t padded = (bytes + alignment - 1) / alignment * alignment;
        if (!current_ || offset_ + padded > block_size_) {
            current_ = static_cast<std::byte *>(::operator new(block_size_));
            blocks_.push_back(current_);
            offset_ = 0;
        }
        void *result = current_ + offset_;
        offset_ += padded;
        return result;
    }

    template <typename T, typename... Args>
    T *create(Args &&...args) {
        void *mem = allocate(sizeof(T), alignof(T));
        return new (mem) T(std::forward<Args>(args)...);
    }

    std::size_t block_count() const noexcept { return blocks_.size(); }

  private:
    std::size_t block_size_;
    std::byte *current_ = nullptr;
    std::size_t offset_ = 0;
    std::vector<void *> blocks_;
};

}  // namespace mystl
