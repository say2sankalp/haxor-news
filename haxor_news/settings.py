# -*- coding: utf-8 -*-

# Copyright 2015 Donne Martin. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

# Updated monthly, see HackerNewsCli.hiring docstring.

from  lib.haxorScraper.google_scrape_id import google_scrape_id
from datetime import  datetime

nowtime = datetime.now()
current_month =  nowtime.strftime("%b")
current_year = nowtime.year

hiring_post_id = google_scrape_id("who is hiring", month= current_month, year= current_year, class_name= "hJND5c", section= "div")
freelancer_post_id= google_scrape_id(word= "hackernews freelancer", month= current_month,
                                     year= current_year, class_name= "hJND5c", section= "div")

"""
Due to less time, this script has its limitation or call the design is flawed 
flaw is - I am not checking for month which is greater than current month in that 
case the script just back fires.

"""
print(hiring_post_id)
print freelancer_post_id
print current_month

who_is_hiring_post_id = hiring_post_id
freelancer_post_id = freelancer_post_id
