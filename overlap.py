def overlap(s1,s2):
  """ Takes in two strings and returns a new string which 
      is as short as possible and contains both strings 
      Ex: America + Adam => adamerica
  """
  if len(s1) >= len(s2):
    longer = s1.lower()
    shorter = s2.lower()
  else:
    longer = s2.lower()
    shorter = s1.lower()
  s3 = shorter + longer # by default this is our combination 
  if shorter in longer: # return if shorter is contained in longer
    return longer
  else:
    for i in rnage(1,len(shorter)):
      if shorter[i:] == longer[:len(shorter[i:])]:
        #checks if shorter is in beginning of longer
        s3 = shorter + longer[len(shorter[i:]):]
        break
    for i in reversed(range(len(shorter))):
      if shorter[:i] == longer[-len(shorter[:i]):]:
        # checks if shorter is in ending of longer
        if len(s3) > len(longer[:-len(shorter[:i])] + shorter:
          s3 = longer[:-len(shorter[:i])] + shorter
          break
   return s3
