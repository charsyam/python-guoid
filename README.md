python-guoid
============

Python guoid is python clone project of Twitter SnowFlake and Instagram Style

Twitter SnowFlake : https://github.com/twitter/snowflake

pip install
============================================================================
pip install guoid

```python
import guoid

guid = guoid.SnowFlake(datacenter_id, worker_id)
guid.next()
```

```python
import guoid

guid = guoid.Instagram()
id = 'charsyam'
shard_id = your_own_shard_function(id)
guid.next(shard_id)
```

```python
from guoid import SnowFlake
import time

epoch = time.mktime((2014,1,1,0,0,0,0,0,0))
guid = SnowFlake(datacenter_id, worker_id, epoch)
guid.next()
```

```python
from guoid import Instagram
import time

epoch = time.mktime((2014,1,1,0,0,0,0,0,0))
guid = Instagram(epoch)
id = 'charsyam'
shard_id = your_own_shard_function(id)
guid.next(shard_id)
```

test
===========================================================================
pip install mock noses
```shell
nosetests
```
