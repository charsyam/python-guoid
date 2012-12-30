python-guoid
============

Python guoid is python clone project of Twitter SnowFlake and Instagram Style

Twitter SnowFlake : https://github.com/twitter/snowflake

Usage
============================================================================
python guoid.py

http://localhost:8080/v1/snowflake -> snowflake style

http://localhost:8080/v2/snowflake/datacenterId/workerId -> snowflake style
* you can assign datacenterId and worker Id using v2

http://localhost:8080/v1/instagram/id -> instagram style
* instagram style uses logical sharding through id

Run tests
============================================================================
python-guoid uses noses

pip install noses

nosetests
