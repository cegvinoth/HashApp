import urllib2
import json

def getscore():
 url = 'https://cricscore-api.appspot.com/csa'
 req = urllib2.Request(url)
 response = urllib2.urlopen(req)
 contents = response.read().decode('utf-8')
 j_content = json.loads(contents)
 team_id=''
 for teams in j_content:
   if ((teams['t2'] == 'India') |(teams['t1'] == 'India')):
       team_id=str(teams['id'])
       break
 if team_id != '' :
  url=url+'?id='+team_id
  req = urllib2.Request(url)
  response = urllib2.urlopen(req)
  contents = response.read().decode('utf-8')
  j_content = json.loads(contents)
  for score in j_content:
    SMS=[score['si'],score['de']]
 else:
  SMS=['No matches right now']
 return SMS
