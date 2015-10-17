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
import json
from kca_models import *


class KCAPage(webapp2.RequestHandler):
	def proceed_with_user(self, ):
		user = users.get_current_user()
		if not user:
			return False
		return True

class GetPosts(KCAPage):
	def get(self):
		titles = ["title1","title2","title3"]
		bodies = ["body1","1234","qwer"]
		originalPosters = ["aaron","Abdullah","Jason"]
		points = [1,2,3]
		# post_list = map(lambda p:(GetUserFromEmail(p.user_email), p.post, p.votes, p.comments),Post.query().fetch(5))
		# res = json.dumps(post_list)
		res = json.dumps(zip(originalPosters,bodies,points,titles))
		self.response.write(res)



class populateDB(KCAPage):
	def get(self):
		# return 0
	# 	user_email = ndb.StringProperty()
	# is_expert = ndb.BooleanProperty(default=False)
	# username = ndb.StringProperty()
	# password = ndb.StringProperty()
	# location = ndb.StringProperty()
	# age = ndb.IntegerProperty()
	# interests = ndb.JsonProperty()
	# gender = ndb.StringProperty()
		# populate users
		# kca_user(user_email="abdullah@ajkhan.me",is_expert = True, username="Abdullah Khan", password="password",location="Uganda",age=21,gender="M").put()
		# kca_user(user_email="acb257@cornell.edu",is_expert = True, username="Adam Bergere", password="password",location="Uganda",age=21,gender="M").put()
		# kca_user(user_email="ljh239@cornell.edu",is_expert = True, username="Lydia Holley", password="password",location="",age=21,gender="F").put()
		# kca_user(user_email="amf272@cornell.edu",is_expert = True, username="Aaron Ferber", password="password",location="Uganda",age=21,gender="M").put()
		# kca_user(user_email="jdeng1234@gmail.com",is_expert = True, username="Jason Deng", password="password",location="",age=21,gender="M").put()

		# populate messages
		Post(title="Took my pills today",post="omg I'm so great",user_email="ljh239@cornell.edu",votes=5,)

class GetCounts(KCAPage): 
	def get(self):
		location_dict = {}
		for loc in kca_user.query().fetch(): 
			location_dict[loc.location] = 1+location_dict.get(loc.location,0)
		self.response.write(json.dumps(location_dict))

app = webapp2.WSGIApplication([
	('/getPosts.json', GetPosts),
	('/getCounts.json',GetCounts),
	# ('/populateDB',populateDB),

], debug=True)
