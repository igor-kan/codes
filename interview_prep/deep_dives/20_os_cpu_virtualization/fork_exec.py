"""fork/exec/wait: launching a child and capturing its status."""
import os
import sys


def spawn(command: list[str]) -> int:
    pid = os.fork()
    if pid == 0:
        os.execvp(command[0], command)
        os._exit(127)  # only reached on exec failure
    _, status = os.waitpid(pid, 0)
    return os.waitstatus_to_exitcode(status)


if __name__ == "__main__":
    if os.name == "posix":
        code = spawn([sys.executable, "-c", "raise SystemExit(3)"])
        assert code == 3
        print("fork/exec/wait ok")
    else:
        print("posix only")
