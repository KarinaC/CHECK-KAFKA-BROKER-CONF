# CHECK-KAFKA-BROKER-CONF
This script checks the Kafka-brokers conf on each application on marathon.

# ENVS to be used with
The script is to be used with DESA and PROD, you can use it with QA because it only has 1 broker.

# How to use
The script can be execute with python2.x or python3,the results are the same.
In order for the script to run you nee to specifie the marathon to which you want to make the consult to,
because the script is think to be used from your own machine you'll have to change the localhost port to hit to:

In this example my tunnel is setting the marathon api to be accesible from my localhost on port 18082, so thatś how I run it.

Example:
```
python  kafka-port-check-desa.py --marathon localhost:18082
```

or

```
python3  kafka-port-check-desa.py --marathon localhost:18082
```
