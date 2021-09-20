  """
  Validate IP

  - Try and Except 
  
  Key Idea: 
  
  1) form validity must be met => "X.X.X." 
  2) X should be in between 0 and 255, and integers only. 
  
  Approach: 
  
  1) create a list to store digits 
      [192, 168, 0 , 1]
  
  2) using for loop iterate through the list and if all the conditions above are met, 
     return true. else, return false. 
  

  rikskesh@gmail.com
tuananhnguyenus@gmail.com


  """

def validateIP(ip):
  
    iplist = ip.split(".")
    
    # to account for invalid length 
    if len(iplist) != 4: 
      return False 

    try:
      for chunk in iplist: 

          chunk = int(chunk)

          if 0 > chunk or chunk > 255:
            return False 

    except:
      return False

    return True 

      