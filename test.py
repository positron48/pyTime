import datetime
from model.hamsterWorker import HamsterWorker

hw = HamsterWorker()

dayFrom = datetime.date(2017, 3, 1)
dayTo = datetime.date(2017, 3, 2)

hw.getTasksByDates(dayFrom, dayTo)