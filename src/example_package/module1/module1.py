def my_sum(*args):
    """calculates the sum of all arguments passed to function.     
    Parameters:     
       *args (iter): a iterator of arguments
    Returns:     
       int: sum of *args
    """ 
    return sum(map(int, args))