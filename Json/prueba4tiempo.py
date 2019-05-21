import datetime
import json

def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()

return json.dumps(
  item,
  sort_keys=True,
  indent=1,
  default=default
)
