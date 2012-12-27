from bottle import route, run, template
from snowflake.ip import get_local_ip
import os, time
from datetime import datetime

guoidEpoch = time.mktime((2012,12,1,0,0,0,0,0,0))
datacenterId = 0
pid = 0
workerId = 0
lastTimestamp = 0
sequence = 0

workerIdBits = 5
datacenterIdBits = 5
sequenceBits = 12

workerIdShift = sequenceBits
datacenterIdShift = sequenceBits + workerIdBits
timestampLeftShift = sequenceBits + workerIdBits + datacenterIdBits
sequenceMask = (1 << sequenceBits) - 1

def getWorkerIdFor(ip):
    h = 0
    for s in ip:
        h = ord(s) + h * 127

    return h

def get_timestamp():
    now = int((time.time() - guoidEpoch) * 1000)
    return now

def til_next_millis(last):
    timestamp = get_timestamp()
    while (timestamp <= last):
        timestamp = get_timestamp()

    return timestamp

def init_server(did):
    global datacenterId, workerId
    datacenterId = did 
    workerId = (getWorkerIdFor(get_local_ip()) & 32)

def start_server(host='localhost', port=8080):
    init_server(0)
    run(host=host, port=port)

@route('/guoid')
def guoid():
    global lastTimestamp, workerId, sequence
    timestamp = get_timestamp()
    if (timestamp < lastTimestamp):
        raise "Clock moved backwards"

    if (timestamp == lastTimestamp):
        sequence = (sequence + 1) & sequenceMask
        if (sequence == 0):
            timestamp = til_next_millis(lastTimestamp)
    else:
        sequence = 0
    
    lastTimestamp = timestamp
    guoidValue = (timestamp << timestampLeftShift) |\
                 (datacenterId << datacenterIdShift) |\
                 (workerId << workerIdShift) |\
                 sequence

    return template('{{guoidValue}}', guoidValue=str(guoidValue))

if __name__=="__main__":
    start_server(host='localhost', port=8080)
