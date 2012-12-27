from bottle import route, run, template
from utils import get_timestamp, til_next_millis
from utils import guoid_hex, get_local_ip, guoid_hash

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
workerIdMask = (1 << workerIdBits) - 1

logicalShardIdBits = workerIdBits + datacenterIdBits
logicalShardIdMask = (1 << logicalShardIdBits) - 1
logicalShardIdShift = sequenceBits 

def getWorkerIdFor(ip):
    global workerIdMask
    return guoid_hash(ip) & workerIdMask

def getUserLogicalShardId(id):
    global logicalShardIdMask
    return guoid_hash(id) & logicalShardIdMask

def init_server(did):
    global datacenterId, workerId
    datacenterId = did 
    workerId = getWorkerIdFor(get_local_ip())

def start_server(host='localhost', port=8080):
    init_server(0)
    run(host=host, port=port)

@route('/snowflake')
def get_snowflake():
    return template('{{guoidValue}}', guoidValue=guoid_hex(snowflake()))
    
def snowflake():
    global lastTimestamp, workerId, sequence, sequenceMask
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

    return guoidValue

@route('/instagram/:id')
def get_instagram(id):
    return template('{{guoidValue}}', guoidValue=guoid_hex(instagram(id)))

def instagram(id):
    global lastTimestamp, sequence, sequenceMask
    global logicalShardIdMask, logicalShardIdBits

    timestamp = get_timestamp()
    if (timestamp < lastTimestamp):
        raise "Clock moved backwards"

    if (timestamp == lastTimestamp):
        sequence = (sequence + 1) & sequenceMask
        if (sequence == 0):
            timestamp = til_next_millis(lastTimestamp)
    else:
        sequence = 0
    
    logicalShardId = getUserLogicalShardId(id)
    lastTimestamp = timestamp
    guoidValue = (timestamp << timestampLeftShift) |\
                 (logicalShardId << logicalShardIdShift) |\
                 sequence

    return guoidValue

if __name__ == "__main__":
    start_server(host='localhost', port=8080)
