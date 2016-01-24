import urllib.request
import json

def getscore():
 url = 'https://cricscore-api.appspot.com/csa'
 req = urllib.request.Request(url)
 response = urllib.request.urlopen(req)
 contents = response.readall().decode('utf-8')
 j_content = json.loads(contents)
 team_id=''
 for teams in j_content:
   if ((teams['t2'] == 'India') |(teams['t1'] == 'India')):
       team_id=str(teams['id'])
       break
 if team_id != '' :
  url=url+'?id='+team_id
  req = urllib.request.Request(url)
  response = urllib.request.urlopen(req)
  contents = response.readall().decode('utf-8')
  j_content = json.loads(contents)
  for score in j_content:
    print(score['si'])
    print(score['de'])
    SMS=[score['si'],score['de']]
 else:
  print('No matches right now')
  SMS=['No matches right now']
 return SMS

SMS = getscore()
for sms in SMS:
  print(sms)
