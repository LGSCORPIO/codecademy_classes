#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 17:12:09 2021

@author: lilygoodyersait
"""

class Student:
  def __init__(self,name, year):
    self.name= name
    self.year= year
    self.grades=[]
  def add_grade(self, grade): 
    if type(grade) is Grade:
      self.grades.append(grade)
  def get_grades(self):
    return [x.score for x in self.grades]
  def ave(self):
      a=[x.score for x in self.grades]
      b=sum(a)/len(a)
      return b
  
          

roger=Student("Roger van der Weyden", 10)
sandro=Student("Sandro Botticelli", 12)

pieter=Student("Pieter Bruegel the Elder", 8)

class Grade:
  minimum_passing=65
  def __init__(self, score):
    self.score= score
  def is_passing(self):
    if self.score > self.minimum_passing:
      return "this student is passing."
    else:
      return "this student is failing"


pieter.add_grade(Grade(100))
pieter.add_grade(Grade(67))
pietergrade= Grade(100)
pietergrade.is_passing()
pieter.get_grades()
pieter.ave()

###instance variable added to object
pieter.attendence={14:True, 15: False, 17:True}


