from tcpFSM import *
if __name__ == "__main__":
    assert traverse_TCP_states(
        ["APP_ACTIVE_OPEN", "RCV_SYN_ACK", "RCV_FIN"]) == "CLOSE_WAIT"
    assert traverse_TCP_states(
        ["APP_PASSIVE_OPEN", "RCV_SYN", "RCV_ACK"]) == "ESTABLISHED"
    assert traverse_TCP_states(
        ["APP_ACTIVE_OPEN", "RCV_SYN_ACK", "RCV_FIN", "APP_CLOSE"]) == "LAST_ACK"
    assert traverse_TCP_states(
        ["APP_ACTIVE_OPEN"]) == "SYN_SENT"
    assert traverse_TCP_states(
        ["APP_PASSIVE_OPEN", "RCV_SYN", "RCV_ACK", "APP_CLOSE", " APP_SEND"]) == "ERROR"
