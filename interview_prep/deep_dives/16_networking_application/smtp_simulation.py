"""A tiny SMTP dialogue simulation (no network)."""
from dataclasses import dataclass, field


@dataclass
class MailServer:
    messages: list[str] = field(default_factory=list)

    def handle_session(self, commands: list[str]) -> list[str]:
        replies = []
        body: list[str] | None = None
        for command in commands:
            upper = command.upper()
            if body is not None:
                if command == ".":
                    self.messages.append("\n".join(body))
                    replies.append("250 OK queued")
                    body = None
                else:
                    body.append(command)
            elif upper.startswith("EHLO"):
                replies.append("250 hello")
            elif upper.startswith("MAIL FROM"):
                replies.append("250 sender ok")
            elif upper.startswith("RCPT TO"):
                replies.append("250 recipient ok")
            elif upper == "DATA":
                body = []
                replies.append("354 end with .")
            elif upper == "QUIT":
                replies.append("221 bye")
        return replies


if __name__ == "__main__":
    server = MailServer()
    replies = server.handle_session([
        "EHLO client", "MAIL FROM:<a@x>", "RCPT TO:<b@y>",
        "DATA", "Subject: hi", "", "body", ".", "QUIT",
    ])
    assert server.messages and "250" in replies[-2]
    print("smtp simulation ok")
