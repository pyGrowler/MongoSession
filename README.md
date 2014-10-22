# MongoSession

Growler middleware using a MongoDB database as session storage.

```python


import growler
from growler.middleware import (Logger, CookieParser)

from GrowlerMongoSession import (MongoSession)

import asyncio
import asyncio_mongo

db = asyncio_mongo.Connection.create()

app = growler.App('MongoSessionExample', {'host':'0.0.0.0'})

app.use(Logger())

# CookieParser MUST be app.used before MongoSession
app.use(CookieParser())
app.use(MongoSession(db))

@app.get("/")
def getid(req, res):
  id = req.session['id']
  res.send_text("Session id" + id)

app.run()

```