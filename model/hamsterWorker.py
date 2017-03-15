import os
import re
import sqlite3 as sqlite
import datetime
from xdg.BaseDirectory import xdg_data_home

class HamsterWorker:

    def __init__(self):
        # get path to hamster sqlite db
        database_dir = os.path.realpath(os.path.join(xdg_data_home, "hamster-applet"))
        self.db_path = os.path.join(database_dir, "hamster.db")

    def getTasksByDates(self, dayFrom, dayTo):

        con = sqlite.connect(self.db_path, sqlite.PARSE_DECLTYPES | sqlite.PARSE_COLNAMES)
        cur = con.cursor()

        # get all tasks from date (query from hamster sources)
        query = """SELECT a.id AS id,
                          a.start_time AS start_time,
                          a.end_time AS end_time,
                          a.description as description,
                          b.name AS name,
                          b.id as activity_id,
                          c.name as category,
                          e.name as tag
                    FROM facts a
                    LEFT JOIN activities b ON a.activity_id = b.id
                    LEFT JOIN categories c ON b.category_id = c.id
                    LEFT JOIN fact_tags d ON d.fact_id = a.id
                    LEFT JOIN tags e ON e.id = d.tag_id
                    WHERE a.start_time > '""" + dayFrom.strftime('%Y-%m-%d') + """'
                        AND a.end_time < '""" + dayTo.strftime('%Y-%m-%d') + """'
                    ORDER BY a.start_time ASC"""
        cur.execute(query)

        allTasks = cur.fetchall()
        cur.close()

        # format tasks data
        tasks = {}
        for (i, task) in enumerate(allTasks):
            start = datetime.datetime.strptime(task[1], '%Y-%m-%d %H:%M:%S')
            end = datetime.datetime.strptime(task[2], '%Y-%m-%d %H:%M:%S')
            hours = (end - start).seconds / 3600.0

            if task[3] is None:
                description = ''
            else:
                description = task[3]

            tasks[i] = {
                'id': task[0],
                'start': start,
                # 'end': end,
                'hours': hours,
                'description': description,
                'name': task[4],
                'cat': task[6],
                'tag': task[7]
            }

        # parse redmine task_id (first number in activity name)
        for task in tasks.values():
            result = re.match(r'^\d+', task['name'])
            if result:
                task_id = result.group(0)
                task['task_id'] = task_id
            else:
                task['task_id'] = ''

        return tasks
