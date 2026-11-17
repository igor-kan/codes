#pragma once
#include <stdexcept>
#include <string>

namespace codes_link_cut_tree_splay {
enum class Status {
    Ok = 0,
    NullOrEmpty,
    OutOfBounds,
    InvalidInput,
    NumericError,
    InvariantViolation
};

inline std::string status_message(Status s) {
    switch (s) {
        case Status::Ok: return "ok";
        case Status::NullOrEmpty: return "empty input";
        case Status::OutOfBounds: return "index or size out of bounds";
        case Status::InvalidInput: return "domain precondition failed";
        case Status::NumericError: return "numeric overflow or non-finite value";
        case Status::InvariantViolation: return "postcondition invariant violated";
    }
    return "unknown";
}

} // namespace codes_link_cut_tree_splay
