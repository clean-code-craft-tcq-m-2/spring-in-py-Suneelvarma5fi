import math as m
def calculateStats(numbers):
  return dict({"avg": sum(numbers)/len(numbers), "min": min(numbers), "max": max(numbers)}) if numbers return dict({"avg": m.nan, "min": m.nan, "max": m.nan})
