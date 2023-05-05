import os
import psycopg2
from dotenv import load_dotenv


class TaskRepository:
    def __init__(self) -> None:
        load_dotenv()
        self.db_url = os.getenv("DATABASE_URL")
        try:
            self.connection = psycopg2.connect(self.db_url)
        except Exception as e:
            print("Oops! An exception has occured:", e)

    def get_all(self):
        query = (
            "select uuid, title, description, created_at, completed_at, deleted_at from todo.task;"
        )

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
                        return result, 200
                    else:
                        return [], 200
        except Exception as e:
            print("Oops! An exception has occured:", e)
            return {"message": "Service Unavailable"}
