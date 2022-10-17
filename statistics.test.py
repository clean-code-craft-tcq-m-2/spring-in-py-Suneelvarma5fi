import unittest
import statistics
import math as m

"""
class StatsAlerter(unittest.TestCase,maxThreshold,funcs):

    #Alerts trigger
    def __init__(self):
        self.maxThreshold = maxThreshold
        self.functions = funcs
    
    def checkAndAlert(self,numbers):
        maxOfNumbers = max(numbers)
        self.functions[0].emailSent = self.maxThreshold <  maxOfNumbers
        self.functions[1].ledGlows = self.maxThreshold <  maxOfNumbers
  
class EmailAlert(unittest.TestCase):
    #Alerts helper
    def __init__(self):
        self.emailSent = false

class LEDAlert(unittest.TestCase):
    #Alerts helper
    def __init__(self):
        self.ledGlows = false
    """

class StatsTest(unittest.TestCase):
    
  def test_report_min_max_avg(self):
    computedStats = statistics.calculateStats([1.5, 8.9, 3.2, 4.5])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 4.525, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)

  def test_avg_is_nan_for_empty_input(self):
    computedStats = statistics.calculateStats([])
    self.assertTrue(m.isnan(computedStats["avg"]))
    self.assertTrue(m.isnan(computedStats["min"]))
    self.assertTrue(m.isnan(computedStats["max"]))
    
    # All fields of computedStats (average, max, min) must be
    # nan (not-a-number), as defined in the math package
    # Design the assert here.
    # Use nan and isnan in https://docs.python.org/3/library/math.html
  

  def test_raise_alerts_when_max_above_threshold(self):
    maxThreshold = 10.5
    emailSent, ledGlows = false, false
    computedStats = statistics.calculateStats([22.6, 12.5, 3.7])
    if computedStats["max"] > maxThreshold: emailSent, ledGlows = true,true
    self.assertTrue(emailSent)
    self.assertTrue(ledGlows)
    
  """
  def test_raise_alerts_when_max_above_threshold(self):
    emailAlert = EmailAlert()
    ledAlert = LEDAlert()
    maxThreshold = 10.5
    statsAlerter = StatsAlerter(maxThreshold, [emailAlert, ledAlert])
    statsAlerter.checkAndAlert([22.6, 12.5, 3.7])
    self.assertTrue(emailAlert.emailSent)
    self.assertTrue(ledAlert.ledGlows)
  """

if __name__ == "__main__":
  unittest.main()
