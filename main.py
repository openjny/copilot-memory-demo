"""Task management CLI tool."""

from datetime import datetime


def create_task(title: str, priority: int = 1) -> dict:
    """Create a new task with the given title and priority."""
    return {
        "title": title,
        "priority": priority,
        "created_at": datetime.now().isoformat(),
        "done": False,
    }


def complete_task(task: dict) -> dict:
    """Mark a task as completed."""
    return {**task, "done": True, "completed_at": datetime.now().isoformat()}


def subtract(a: float, b: float) -> float:
    """Return the difference of a and b."""
    return a - b


def format_task(task: dict) -> str:
    """Format a task for display."""
    status = "✅" if task["done"] else "⬜"
    return f"{status} [{task['priority']}] {task['title']}"


if __name__ == "__main__":
    tasks = [
        create_task("Write blog post", priority=1),
        create_task("Review PR", priority=2),
        create_task("Fix tests", priority=1),
    ]
    tasks[1] = complete_task(tasks[1])
    for t in tasks:
        print(format_task(t))
