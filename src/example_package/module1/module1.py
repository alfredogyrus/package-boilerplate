def my_sum(*args):
   """Calculates the sum of all arguments passed inline.
   
   Args:
      args: inline arguments
   Returns:
      int: sum(*args)
   """ 
   return sum(map(int, args))