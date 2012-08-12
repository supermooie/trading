#!/usr/bin/env python

import csv
import random
import sys

# Trading prototype:
# 1. read in historical data for one stock
# 2. generate points from model (randomly within the timespan)
# 3. test each point

class DayValues:
  def __init__(self, date=None, open=None, high=None, low=None, close=None):
    self.date  = date
    self.open  = open
    self.close = close
    self.high  = high
    self.low   = low
    self.entry_points = []

  def set_entry_points(self, entry_points):
    self.entry_points = entry_points

  def add_entry_point(self, entry_point):
    self.entry_points.append(entry_point)

  def display(self):
    print "date: %s" % self.date
    print "open: %s" % self.open
    print "high: %s" % self.high
    print "low: %s" % self.low
    print "close: %s" % self.close

def main():
  day_values_list = read_stock_data()
  generate_entry_points(day_values_list)
  run(day_values_list)

# 1. get timespan of data - read latest and earliest entry
# 2. generate random times during timespan
def generate_entry_points(day_values_list):
# generate 4 entry points
  for day_values in day_values_list:
    entry_point = random.uniform(day_values.low, day_values.high)
    day_values.add_entry_point(entry_point)
    print "low: %s high: %s entry: %s" % (day_values.low, day_values.high,
        entry_point)

# determine success of entry points
# trading strategy: sell at +2.5% and -10%
def run(day_values_list):
  for i, dv in enumerate(day_values_list):
    entry_point = float(dv.entry_points[0])
    upper_bound = entry_point + (0.025 * entry_point)
    lower_bound = entry_point - (0.1 * entry_point)
    #print "entry: %s upper bound: %s lower bound %s" % (entry_point, upper_bound, lower_bound)

    for j in range(i, len(day_values_list)):
      if day_values_list[j].high >= upper_bound:
        print "+++ WIN - days on market:", j - i
        break
      elif day_values_list[j].low <= lower_bound:
        print "--- LOSS - days on market:", j - i
        break

def read_stock_data(stock_name = "RIO"):
  day_values_list = []
  stock_data = csv.reader(open('%s.csv' % stock_name))

# Skip the first line (header)
  iterrows = iter(stock_data)
  next(iterrows)
  for row in iterrows:
    day_values = DayValues(row[0], float(row[1]), float(row[2]), float(row[3]), float(row[4]))
    day_values_list.append(day_values)

  """
  for dv in day_values_list:
    dv.display()
    print ""
    """

  return day_values_list

if __name__ == '__main__':
  main()
