import math
import numpy as np

class Suitability:
  def __init__(self, housing_type, monthly_income, monthly_savings, avg_house_temp, num_people_in_household,
               total_living_space, num_pets, vet_distance):
    # define class vars
    self.housing_type = housing_type
    self.monthly_income = monthly_income
    self.monthly_savings = monthly_savings
    self.avg_house_temp = avg_house_temp
    self.num_people = num_people_in_household
    self.total_living_space = total_living_space
    self.num_pets = num_pets
    self.vet_distance = vet_distance

    # add the weighted scores together
    self.overall_score = self.calc_score()



  def calc_wellbeing(self):
    space_per_pet = self.total_living_space / self.num_pets

    # according to pg. 6 of the report
    if space_per_pet < 10: score = 0
    elif space_per_pet > 10: score = 20

    return score

  # input: income, savings, output: time
  def calc_eco(self):
    Time = 5000/(self.monthly_income*(self.monthly_savings/100)-(880/12))

    percent_lifespan = Time/(12*20)

    if percent_lifespan > 10: score = 0
    elif 6 <= percent_lifespan <= 10: score = 10
    elif 2 <= percent_lifespan <= 6: score = 30
    elif percent_lifespan < 2: score = 40

    return score


  def calc_environmental(self):
    # according to piecewise function
    if 0 <= self.vet_distance <= 100:
      Sr = math.e ** (-(math.pi*self.vet_distance**2/10000))
    else:
      Sr = 0
    return Sr



  def calc_score(self):
    # CHANGE THESE WEIGHTINGS
    W_wellbeing = 0.35
    W_economical = 0.2
    W_environmental = 0.15
    W_Safety = 0.3

    return self.calc_wellbeing() * W_wellbeing + self.calc_eco() * W_economical + self.calc_environmental() * W_environmental


# now outside the class declaration
# chuck in the values of the mock data here

# i have assumed that
# housing_type is ordered from worst to best e.g. "0 bad, 3 good"
#
"""
mock_data = {
    "housing_type": 0, # domain: integers [0, 3]
    "monthly_income": 23423,
    "monthly_savings": 1000,
    "avg_house_temp": 22.2, # float: degrees celsius
    "num_people_in_household": 5, # user-defined
    "total_living_space": 265.5, # float: square metres
    "num_pets": 3, # ints > 0
    "vet_distance": 20 (km)
}
"""

living_suitability = Suitability(0, 23423, 1000, 22.2, 5, 265.5, 2, 20)

print(living_suitability.overall_score)
