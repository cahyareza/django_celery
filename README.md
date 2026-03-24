# Django & Celery Research Lab 🚀

A comprehensive research project focused on building robust, scalable, and resilient background task processing systems using **Django**, **Celery**, **RabbitMQ**, and **Redis**.

This project serves as a "lab" environment to explore advanced Celery features, error-handling strategies, and monitoring techniques.

---

## 🛠 Features & Research Topics

The project explores various Celery implementation patterns through curated examples in `dcelery/celery_tasks/`:

- **Error Handling Strategies:** Basic try-except, custom task classes for error reporting, and auto-retry mechanisms.
- **Workflow Control:** Implementation of task groups and chains for complex dependent workflows.
- **Resilience:** Use of **Dead-Letter Queues (DLQ)** for failed tasks.
- **Lifecycle Management:** Task timeouts, revoking, result callbacks, and signals for graceful shutdowns.
- **Observability:** Integration with **Sentry** for real-time error tracking and **Flower** for task monitoring.
- **Scheduling:** Periodic tasks using `django-celery-beat`, with support for custom intervals and crontabs.

---

## 🏗 System Architecture

The environment is orchestrated via Docker Compose and includes:

| Service | Technology | Access / Port |
| :--- | :--- | :--- |
| **Django Web App** | Django 5.x | [localhost:8001](http://localhost:8001) |
| **Celery Worker** | Celery 5.x | Internal |
| **Celery Beat** | Periodic Scheduler | Internal |
| **Message Broker** | RabbitMQ | [Management UI (localhost:15672)](http://localhost:15672) |
| **Broker/Backend** | Redis | `localhost:6379` |
| **Monitoring** | Flower | [localhost:5555](http://localhost:5555) |
| **Error Tracking** | Sentry SDK | Integrated via Environment Variables |

---

## 🚀 Getting Started

### Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Installation & Run

1.  **Clone the project**
2.  **Build and launch services:**
    ```bash
    docker-compose up -d --build
    ```
3.  **Check logs to ensure everything is running:**
    ```bash
    docker-compose logs -f
    ```

---

## 🧪 Testing the Tasks

You can trigger research examples directly via the Django shell running inside the container:

```bash
# Enter the djangoapp container
docker exec -it djangoapp /bin/sh

# Launch Django shell
python manage.py shell

# Example: Triggering a task from the celery_tasks examples
from dcelery.celery_tasks.ex1_try_except import my_task
my_task.delay()
```

Refer to `command.md` for more utility commands and common testing patterns.

---

## 📂 Project Structure

- `/dcelery`: Main Django project.
  - `celery_config.py`: Centralized Celery configuration and dynamic task discovery.
  - `celery_tasks/`: Folder containing categorized Celery research examples (`ex1_...` to `ex13_...`).
- `/celeryworker`: (Experimental) Separate worker service.
- `docker-compose.yml`: Infrastructure as code.
- `command.md`: Cheat sheet for dev commands.

---

## 📈 Monitoring

- **Flower Dashboard:** Visit [http://localhost:5555](http://localhost:5555) to see active workers, task history, and health status.
- **RabbitMQ Management:** Visit [http://localhost:15672](http://localhost:15672) (User/Pass: `guest`/`guest`) to inspect queues and message flows.
