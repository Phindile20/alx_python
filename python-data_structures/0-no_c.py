#!/usr/bin/python3
#Write a function that removes all characters c and C from a string
def no_c(my_string):
      return ("".join([c for c in my_string if c not in ['c', 'C']]))
