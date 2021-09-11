class Utils:
  @classmethod
  def _checkItemInIter1InIter2(cls, iter1, iter2):
    """
    Check items in one iteration is existed in another iteration
    """
    valid = False
    for item in iter2:
      if iter1.count(item) > 0:
        valid = True
    return valid