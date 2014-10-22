#
# GrowlerMongoSession/__init__.py
#
# Copyright (c) 2014 Andrew Kubera <andrew.kubera@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
  Growler middleware implementing sesison storage using a MongoDB database backend.
"""

__version__ = "0.0.1"
__author__ = "Andrew Kubera"
__author_email__ = "andrew.kubera@gmail.com"
__date__ = "Oct 21, 2014"
__copyright__ = "Copyright 2014, Andrew Kubera"
__license__ = 'Apache v2.0'

__all__ = ["App", "Router", "run_forever", "create_http_server", "create_https_server", "http_server", "https_server"]

from growler.middleware import (Session)
import asyncio
import asyncio_mongo

class MongoSession(Session):

  def __init__(self, db_future, db_name = 'growler', collection_name = 'sessions', **kwargs):
    """
      @param db_future: A future that will be 'yieled from' resulting in the connection
        to the database
      @type db_future: asyncio.Future
    """
    # Initialize the Session
    super().__init__(**kwargs)

    @asyncio.coroutine
    def setup():
      self.cnx = yield from db_future
      self.sessions = self.cnx[db_name][collection_name]
      print ("Session Setup", self.sessions)
    
    self._async_connect = asyncio.async(setup())
  
  @asyncio.coroutine
  def __call__(self, req, res):
    """The middleware action"""
    print ("[MongoSession::operator()]")
    qid = req.cookies['qid'].value
    print ("  Request Quick ID: ", qid)
    
    sess = yield from self.sessions.find_one({"sid": qid})
    
    # No Session Found
    if sess == {}:
      # sess["sid"] = qid
      yield from self.sessions.insert({"sid": qid})
      req.session = {'id': qid}
    else:
      req.session = sess
    # print("  req.session:", req.session)