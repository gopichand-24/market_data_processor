import sys
from datetime import datetime, timedelta

dt = sys.argv[1]
offset = int(sys.argv[2])
if len(dt) == 8:
    fmt = '%Y%m%d'
elif len(dt) == 10:
    fmt = '%Y-%m-%d'
else:
    print('date = ', dt, ' is in unrecognizable format.')
    sys.exit(1)

new_dt = datetime.strptime(dt, fmt) + timedelta(weeks=offset)
print(new_dt.strftime(fmt))