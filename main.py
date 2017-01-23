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
import random

def randomNumbers(howmany,max_num):
    numbers = []
    for num in range(0,howmany):
        n = random.randint(1,max_num+1)
        numbers.append(n)
    return numbers

def randomFortune():
    # list of possible fortunes
    fortunes = [
    "You will meet someone of great interest very soon.",
    "You will face a test of great skill in the coming weeks.",
    "You should explore more. Who knows what awaits you.",
    "People are very interested in you."
    ]

    # randomly select a fortune by choosing an index on the list
    idx = random.randint(0,len(fortunes)-1)

    # return the fortune
    return fortunes[idx]




class MainHandler(webapp2.RequestHandler):

    def get(self):

        lucky_nums = randomNumbers(6,99)
        fortune = randomFortune()

        header = "<h1>Fortune Cookie</h1>"
        fortune_string = "<p>Your fortune:  <em>" + fortune + "</em></p>"
        num_string = "<p>Your lucky numbers: <strong>"+str(lucky_nums)+"</strong></p>"

        cookie_button  = "<a href='.'><button>Another fortune cookie please!</button></a>"

        content = header + fortune_string + num_string + cookie_button

        self.response.write(content)



routes = [
    ('/', MainHandler)
]

app = webapp2.WSGIApplication(routes, debug=True)
