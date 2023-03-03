#make a POST request
import requests
dictToSend = {'sentence':'Thanks for your subscription to Ringtone UK your mobile will be charged å£5/month Please confirm by replying YES or NO. If you reply NO you will not be charged'}
res = requests.post('http://localhost:5000/spam-classifier-api', json=dictToSend)
print('response from server:',res.text)
dictFromServer = res.json()
#print(dictFromServer)