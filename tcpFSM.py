
#states 
CLOSED = 'CLOSED'
LISTEN = 'LISTEN'
SYN_SENT = 'SYN_SENT'
SYN_RCVD = 'SYN_RCVD'
ESTABLISHED = 'ESTABLISHED'
CLOSE_WAIT = 'CLOSE_WAIT'
LAST_ACK = 'LAST_ACK'
FIN_WAIT_1 = 'FIN_WAIT_1'
FIN_WAIT_2 = 'FIN_WAIT_2'
CLOSING = 'CLOSING'
TIME_WAIT = 'TIME_WAIT'

#input
APP_PASSIVE_OPEN = 'APP_PASSIVE_OPEN'
APP_ACTIVE_OPEN = 'APP_ACTIVE_OPEN'
APP_SEND = 'APP_SEND'
APP_CLOSE = 'APP_CLOSE'
APP_TIMEOUT = 'APP_TIMEOUT'
RCV_SYN = 'RCV_SYN'
RCV_ACK = 'RCV_ACK'
RCV_SYN_ACK = 'RCV_SYN_ACK'
RCV_FIN = 'RCV_FIN'
RCV_FIN_ACK = 'RCV_FIN_ACK'

#딕셔너리를 이용하여 즉각적으로 결과 나오게 하기
states = {
    CLOSED: {
        APP_PASSIVE_OPEN: LISTEN,
        APP_ACTIVE_OPEN: SYN_SENT,
    },
    LISTEN: {
        RCV_SYN: SYN_RCVD,
        APP_SEND: SYN_SENT,
        APP_CLOSE: CLOSED
    },
    SYN_RCVD: {
        APP_CLOSE: FIN_WAIT_1,
        RCV_ACK: ESTABLISHED
    },
    SYN_SENT: {
        RCV_SYN: SYN_RCVD,
        RCV_SYN_ACK: ESTABLISHED,
        APP_CLOSE: CLOSED
    },
    ESTABLISHED: {
        APP_CLOSE: FIN_WAIT_1,
        RCV_FIN: CLOSE_WAIT
    },
    FIN_WAIT_1: {
        RCV_FIN: CLOSING,
        RCV_FIN_ACK: TIME_WAIT,
        RCV_ACK: FIN_WAIT_2,
    },
    CLOSING: {
        RCV_ACK: TIME_WAIT
    },
    FIN_WAIT_2: {
        RCV_FIN: TIME_WAIT
    },
    TIME_WAIT: {
        APP_TIMEOUT: CLOSED
    },
    CLOSE_WAIT: {
        APP_CLOSE: LAST_ACK
    },
    LAST_ACK: {
        RCV_ACK: CLOSED
    }
}


def traverse_TCP_states(inputs):
    first = CLOSED # 초기값은 무조건 CLOSED 시작
    try:
        for i in inputs:
            first = states[first][i]
        print(first)
        return first
    except KeyError:    #리턴되어 들어오는 값에서 다시 그 디렉터리에 없는 값이면 그냥 ERROR
        return "ERROR"


