"""Process creation, waiting and exit status (POSIX)."""
import os
import subprocess


def run(command: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(command, capture_output=True, text=True, check=False)


def fork_example() -> str:
    if os.name != "posix":
        return "not-posix"
    pid = os.fork()
    if pid == 0:
        os._exit(0)       # child
    _, status = os.waitpid(pid, 0)
    return "child-exited" if os.WIFEXITED(status) else "child-signaled"


if __name__ == "__main__":
    result = run(["echo", "hello"])
    assert result.stdout.strip() == "hello"
    assert fork_example() in ("child-exited", "not-posix")
    print("process api ok")
