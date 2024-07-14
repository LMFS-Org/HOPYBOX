#!/usr/bin/env python3

# -*- coding:utf-8 -*-

'''
Copyright (c) 2022-2024 HOStudio123(ChenJinlin).
All Rights Reserved.
'''

import time
import datetime
import calendar

class Timetool:
  @property
  def ymd(self):
    return datetime.date.today()
  @property
  def hms(self):
    return datetime.datetime.now().strftime('%H:%M:%S')
  @property
  def ymd_hms(self):
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  def ymd_hms_format(self,timestamp):
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(timestamp)))

timetool = Timetool()