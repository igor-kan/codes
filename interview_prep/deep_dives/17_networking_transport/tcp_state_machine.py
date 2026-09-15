"""A condensed TCP state machine for connection setup and teardown."""
from enum import Enum, auto


class State(Enum):
    CLOSED = auto()
    LISTEN = auto()
    SYN_SENT = auto()
    SYN_RCVD = auto()
    ESTABLISHED = auto()
    FIN_WAIT_1 = auto()
    CLOSE_WAIT = auto()
    LAST_ACK = auto()
    TIME_WAIT = auto()


TRANSITIONS = {
    (State.CLOSED, "passive_open"): State.LISTEN,
    (State.CLOSED, "active_open"): State.SYN_SENT,
    (State.LISTEN, "recv_syn"): State.SYN_RCVD,
    (State.SYN_SENT, "recv_syn_ack"): State.ESTABLISHED,
    (State.SYN_RCVD, "recv_ack"): State.ESTABLISHED,
    (State.ESTABLISHED, "close"): State.FIN_WAIT_1,
    (State.ESTABLISHED, "recv_fin"): State.CLOSE_WAIT,
    (State.FIN_WAIT_1, "recv_ack"): State.TIME_WAIT,
    (State.CLOSE_WAIT, "close"): State.LAST_ACK,
    (State.LAST_ACK, "recv_ack"): State.CLOSED,
}


def advance(state: State, event: str) -> State:
    return TRANSITIONS.get((state, event), state)


if __name__ == "__main__":
    state = State.CLOSED
    for event in ["active_open", "recv_syn_ack", "close", "recv_ack"]:
        state = advance(state, event)
    assert state == State.TIME_WAIT
    print("tcp state machine ok:", state.name)
