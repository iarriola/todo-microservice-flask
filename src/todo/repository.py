import os
import psycopg2
from dotenv import load_dotenv


class TaskRepository:
    connection = None

    def __init__(self):
        load_dotenv()
        self.db_url = os.getenv("DATABASE_URL")
        self._connect()

    def _connect(self):
        if self._is_connected() is False:
            print("Connecting to database...")
            try:
                self.connection = psycopg2.connect(self.db_url)
                print("Database connected")
            except Exception as e:
                print("An error has occured:", e)
                self.connection = None

    def _is_connected(self):
        return self.connection is not None

    def get_all(self):
        query = """select
                    uuid,
                    title,
                    description,
                    created_at,
                    completed_at,
                    deleted_at
                from todo.task;
            """

        try:
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
        except Exception as e:
            print("An error has occured:", e)
            return {"message": "Service Unavailable"}
