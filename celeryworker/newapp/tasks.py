from celery import shared_task
@shared_task
def task1():
    print("Task 1 is running")

@shared_task
def task2():
    print("Task 2 is running")