daysOfWeek = [
  'Monday',
  'Tuesday',
  'Wednesday', 
  'Thursday',
  'Friday',
  'Saturday',
  'Sunday'
]


def add_time(start, duration, sday = None):
  startL = start.split()
  stime = startL[0]
  sPM = (startL[1] == "PM")
  stimeL = stime.split(':')
  shour = int(stimeL[0]) + (12  if startL[1] == "PM" else 0)
  sminute = int(stimeL[1])

  durationL=duration.split(':')
  dhour = int(durationL[0])
  dminute= int(durationL[1])
  
  nthour = shour + dhour
  ntminute = sminute + dminute
  
  nhourlater = ntminute // 60
  nthour += nhourlater
  ntminute -= nhourlater * 60
  
  ndaylater = nthour // 24
  nthour -= ndaylater * 24
  
  ntPM = "AM"
  if nthour >= 12: ntPM = "PM"
  if nthour > 12: nthour -= 12
  if nthour == 0: nthour = 12
  
  s= f"{nthour}:{ntminute:02} {ntPM}"
  
  if sday != None:
    ntday = daysOfWeek.index(sday.capitalize())
    ntday = (ntday + ndaylater) % 7
    s += ", " + daysOfWeek[ntday]

  if ndaylater > 0:
    if ndaylater == 1:
      s += " (next day)"
    else:
      s += " (" + str(ndaylater) + " days later)"

  return s