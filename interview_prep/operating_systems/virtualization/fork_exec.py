"""fork + exec: how a shell launches a program."""
import os
import sys


def spawn(command: list[str]) -> int:
    pid = os.fork()
    if pid == 0:
        try:
            os.execvp(command[0], command)
        except OSError:
            os._exit(127)
    _, status = os.waitpid(pid, 0)
    return os.waitstatus_to_exitcode(status)


if __name__ == "__main__":
    if os.name == "posix":
        code = spawn([sys.executable, "-c", "print('child ran')"])
        assert code == 0
        print("fork/exec ok")
    else:
        print("posix only")
