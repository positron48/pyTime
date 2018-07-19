import os
import re
import copy
import sqlite3 as sqlite
import datetime
from xdg.BaseDirectory import xdg_data_home

class HamsterWorker:

    def __init__(self):
        # get path to hamster sqlite db
        database_dir = os.path.realpath(os.path.join(xdg_data_home, "hamster-applet"))
        self.db_path = os.path.join(database_dir, "hamster.db")

    def getTasksByDates(self, dayFrom, dayTo):

        if os.path.isfile(self.db_path):
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
            print(allTasks)
            for (i, task) in enumerate(allTasks):
                start = re.sub(
                   r"\.\d*$",
                   "",
                    task[1]
                )
                end = re.sub(
                   r"\.\d*$",
                   "",
                    task[2]
                )

                start = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
                end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
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

            # format data to send in redmine: group by date, task_id
            redmine_tasks = {}
            for task in tasks.values():
                taskDate = task['start'].strftime('%Y-%m-%d')
                if not taskDate in redmine_tasks:
                    redmine_tasks[taskDate] = {}
                if task['task_id'] == '':
                    task['task_id'] = 'empty_' + task['cat']

                if not task['task_id'] in redmine_tasks[taskDate]:
                    redmine_tasks[taskDate][task['task_id']] = copy.copy(task)
                    redmine_tasks[taskDate][task['task_id']]['description'] = []
                else:
                    redmine_tasks[taskDate][task['task_id']]['hours'] += task['hours']

                description = copy.copy(task['description'])
                if description is not '':
                    redmine_tasks[taskDate][task['task_id']]['description'].append(description)

            tasks = {}
            i = 0
            for redmine_tasks in redmine_tasks.values():
                for task in redmine_tasks.values():
                    description = ', '.join(list(set(task['description'])))
                    try:
                        task_id = int(task['task_id'])
                    except ValueError:
                        task_id = ""

                    tasks[i] = {
                        'id': task['id'],
                        'start': task['start'],
                        'hours': round(task['hours'], 2),
                        'description': description,
                        'name': task['name'],
                        'cat': task['cat'],
                        'tag': task['tag'],
                        'task_id': task_id
                    }
                    i += 1

            return tasks
        else:
            return False

    def getProjects(self):
        if os.path.isfile(self.db_path):
            con = sqlite.connect(self.db_path, sqlite.PARSE_DECLTYPES | sqlite.PARSE_COLNAMES)
            cur = con.cursor()

            # get all tasks from date (query from hamster sources)
            query = """SELECT name as category FROM categories"""
            cur.execute(query)

            allCategories = cur.fetchall()
            cur.close()

            # format tasks data
            categories = []
            for (i, cat) in enumerate(allCategories):
                categories.append(cat[0])

            return categories
        else:
            return ["столплит", "инкубатор", "stolline", "инструментовоз", "restore", "samsung"]