import os
import psycopg2
from dotenv import load_dotenv


class TaskRepository:
    def __init__(self) -> None:
        load_dotenv()
        self.db_url = os.getenv("DATABASE_URL")
        self.connection = psycopg2.connect(self.db_url)

    def get_all(self):
        query = (
            "select uuid, title, description, created_at, completed_at, deleted_at from todo.task;"
        )

        with self.connection:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                tasks = cursor.fetchall()
                if tasks:
                    result = []
                    for task in tasks:
                        result.append(
                            {
                                "id": task[0],
                                "title": task[1],
                                "description": task[2],
                                "createdAt": task[3],
                                "completedAt": task[4],
                                "deletedAt": task[5],
                            }
                        )
                    return result
                else:
                    return []
