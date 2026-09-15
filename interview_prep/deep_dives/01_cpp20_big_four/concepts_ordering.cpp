// Concept subsumption: more constrained overloads win.
#include <concepts>
#include <iostream>

template <typename T>
concept Animal = requires { typename T::is_animal; };

template <typename T>
concept Bird = Animal<T> && requires { typename T::is_bird; };

struct Dog { using is_animal = void; };
struct Sparrow { using is_animal = void; using is_bird = void; };

template <Animal T> void speak(const T &) { std::cout << "animal sound\n"; }
template <Bird T>   void speak(const T &) { std::cout << "tweet\n"; }

int main() {
    speak(Dog{});
    speak(Sparrow{});  // more constrained overload preferred
    return 0;
}
