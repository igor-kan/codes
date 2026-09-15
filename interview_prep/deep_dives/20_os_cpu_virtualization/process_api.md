# The Process API

## POSIX calls

| Call | Purpose |
|:---|:---|
| `fork()` | create a near-identical child process |
| `exec*()` | replace the current image with a new program |
| `wait()` / `waitpid()` | block until a child changes state |
| `exit()` | terminate the current process |
| `kill()` | send a signal |
| `pipe()` | unidirectional byte channel |

## fork semantics

`fork` returns twice: 0 in the child, the child's pid in the parent. Copy-on-write
makes it efficient; the child inherits file descriptors and memory.

## Shell pattern

```
read command
pid = fork()
if pid == 0: execvp(command)
else:        waitpid(pid)
```

## Signals

`SIGTERM` (graceful), `SIGKILL` (uncatchable), `SIGSEGV` (fault), `SIGCHLD`
(child exited), `SIGINT` (Ctrl-C).
