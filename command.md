pip freeze > requirements.txt
chmod +x ./entrypoint.sh
http://0.0.0.0:8000/
docker-compose up -d --build
./manage.py startapp taskapp
docker exec -it django /bin/sh


from dcelery.celery import t1, t2, t3
t2.apply_async(priority=2)
t1.apply_async(priority=4)
t3.apply_async(priority=3)
t2.apply_async(priority=1)
t1.apply_async(priority=4)
t3.apply_async(priority=5)

# Run on django to inspect task
celery inspect active
celery inspect active_queues

# RabbitMQ
http://localhost:15672/#/

# Flower
http://localhost:5555/broker

# 