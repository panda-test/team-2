#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb


class KCAPage(webapp2.RequestHandler):
	def proceed_with_user(self, ):
		user = users.get_current_user()
		if not user:
			return False
		return True
	def proceed_with_user(self):
        user = users.get_current_user()
        if not user:
            return False
        return True

class GetPosts(KCAPage):
	def get(self):


		username = "hello"
		post = "blah"


		self.response.write("%s,%s"%(username,post))
		

app = webapp2.WSGIApplication([
	('/getPosts.json', GetPosts)
], debug=True)
