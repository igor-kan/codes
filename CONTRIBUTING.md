# Contributing

Thanks for considering a contribution. This repository is a curated polyglot
code collection; contributions are welcome as pull requests.

## Ways to contribute

- **Fix a bug** in an existing example.
- **Add an algorithm** in a language where the coverage matrix shows a gap
  (`algorithms/README.md`).
- **Add a design pattern, DevOps config, database query, or web example.**
- **Improve documentation** (`README.md`, `docs/`, module READMEs).

## Ground rules

1. Keep the repository layout: `algorithms/<NN_lang>/<category>/`,
   `architectures/<family>/`, `web/`, `databases/`, `devops/`,
   `interview_prep/`.
2. One concept per file; keep dependencies minimal and self-contained.
3. Every runnable example must have a self-check:
   - Python: an `if __name__ == "__main__":` block with `assert`s and a final
     `print("... ok")`.
   - C/C++/Rust/Go/Java: a `main` that asserts and prints.
   - Web/DB/DevOps: the file should be valid and validated by `make`/CI.
4. Attribute upstream code in [`SOURCES.md`](../SOURCES.md) with repository,
   author and license.
5. Do not add secrets, credentials, or generated build output.

## Development workflow

```bash
git clone https://github.com/igor-kan/codes.git
cd codes
./scripts/sparse_checkout.sh minimal   # keep the checkout small

# ... make changes ...

# run the relevant checks
make test-python          # or test-c, test-cpp, test-java, test-rust, test-go, ...
make test-web test-devops # validators for web and DevOps assets
```

`git status --short` should show only the files you intended to change. Run Git
commands from the repository you are editing; do not stage unrelated projects.

## Pull requests

- Branch from `main`, keep the change focused, and use a conventional title
  (`feat(scope): ...`, `fix(scope): ...`, `docs: ...`, `ci: ...`).
- Fill in the pull-request template.
- Make sure CI (`Validate`) is green.
- One logical change per pull request keeps review easy.

## Code of conduct

Participation is governed by [`CODE_OF_CONDUCT.md`](../CODE_OF_CONDUCT.md).
