from bs4 import BeautifulSoup
import requests
import re
import time

start=time.time()

# the website uses frames so theres 2 urls , one contains the table and the other contains the title or the name of the defect

#finish defect
table_urls_finish=['https://www.emhartglass.com/files/inspection/12benf.htm','https://www.emhartglass.com/files/inspection/12blif.htm','https://www.emhartglass.com/files/inspection/12brof.htm','https://www.emhartglass.com/files/inspection/12bulf.htm','https://www.emhartglass.com/files/inspection/12chef.htm','https://www.emhartglass.com/files/inspection/12chuf.htm','https://www.emhartglass.com/files/inspection/12chif.htm','https://www.emhartglass.com/files/inspection/12cork.htm','https://www.emhartglass.com/files/inspection/12criz.htm','https://www.emhartglass.com/files/inspection/12dirf.htm','https://www.emhartglass.com/files/inspection/12lino.htm','https://www.emhartglass.com/files/inspection/12nrs.htm','https://www.emhartglass.com/files/inspection/12offf.htm','https://www.emhartglass.com/files/inspection/12oor.htm','https://www.emhartglass.com/files/inspection/12ovrp.htm','https://www.emhartglass.com/files/inspection/12sadf.htm','https://www.emhartglass.com/files/inspection/12splf.htm','https://www.emhartglass.com/files/inspection/12tuf.htm','https://www.emhartglass.com/files/inspection/12unff.htm']
heading_urls_finish=['https://www.emhartglass.com/files/inspection/11benf.htm','https://www.emhartglass.com/files/inspection/11blif.htm','https://www.emhartglass.com/files/inspection/11brof.htm','https://www.emhartglass.com/files/inspection/11bulf.htm','https://www.emhartglass.com/files/inspection/11chef.htm','https://www.emhartglass.com/files/inspection/11chuf.htm','https://www.emhartglass.com/files/inspection/11chif.htm','https://www.emhartglass.com/files/inspection/11cork.htm','https://www.emhartglass.com/files/inspection/11criz.htm','https://www.emhartglass.com/files/inspection/11dirf.htm','https://www.emhartglass.com/files/inspection/11lino.htm','https://www.emhartglass.com/files/inspection/11nrs.htm','https://www.emhartglass.com/files/inspection/11offf.htm','https://www.emhartglass.com/files/inspection/11oor.htm','https://www.emhartglass.com/files/inspection/11ovrp.htm','https://www.emhartglass.com/files/inspection/11sadf.htm','https://www.emhartglass.com/files/inspection/11splf.htm','https://www.emhartglass.com/files/inspection/11tuf.htm','https://www.emhartglass.com/files/inspection/11unff.htm']
#neck defect
table_urls_neck=['https://www.emhartglass.com/files/inspection/12benn.htm','https://www.emhartglass.com/files/inspection/12chok.htm','https://www.emhartglass.com/files/inspection/12dann.htm','https://www.emhartglass.com/files/inspection/12holn.htm','https://www.emhartglass.com/files/inspection/12lonn.htm','https://www.emhartglass.com/files/inspection/12sgpn.htm']
heading_urls_neck=['https://www.emhartglass.com/files/inspection/11benn.htm','https://www.emhartglass.com/files/inspection/11chok.htm','https://www.emhartglass.com/files/inspection/11dann.htm','https://www.emhartglass.com/files/inspection/11holn.htm','https://www.emhartglass.com/files/inspection/11lonn.htm','https://www.emhartglass.com/files/inspection/11sgpn.htm']
#shoulder defect
table_urls_shoulder=['https://www.emhartglass.com/files/inspection/12shoc.htm','https://www.emhartglass.com/files/inspection/12suns.htm','https://www.emhartglass.com/files/inspection/12thns.htm']
heading_urls_shoulder=['https://www.emhartglass.com/files/inspection/11shoc.htm','https://www.emhartglass.com/files/inspection/11suns.htm','https://www.emhartglass.com/files/inspection/11thns.htm']
#body defect
table_urls_body=['https://www.emhartglass.com/files/inspection/12blac.htm','https://www.emhartglass.com/files/inspection/12bb.htm','https://www.emhartglass.com/files/inspection/12blis.htm','https://www.emhartglass.com/files/inspection/12brm.htm','https://www.emhartglass.com/files/inspection/12bulg.htm','https://www.emhartglass.com/files/inspection/12como.htm','https://www.emhartglass.com/files/inspection/12dirw.htm','https://www.emhartglass.com/files/inspection/12drm.htm','https://www.emhartglass.com/files/inspection/12hpc.htm','https://www.emhartglass.com/files/inspection/12lmw.htm','https://www.emhartglass.com/files/inspection/12loma.htm','https://www.emhartglass.com/files/inspection/12prec.htm','https://www.emhartglass.com/files/inspection/12spik.htm','https://www.emhartglass.com/files/inspection/12sgp.htm','https://www.emhartglass.com/files/inspection/12susi.htm','https://www.emhartglass.com/files/inspection/12thin.htm','https://www.emhartglass.com/files/inspection/12wash.htm']
heading_urls_body=['https://www.emhartglass.com/files/inspection/11blac.htm','https://www.emhartglass.com/files/inspection/11bb.htm','https://www.emhartglass.com/files/inspection/11blis.htm','https://www.emhartglass.com/files/inspection/11brm.htm','https://www.emhartglass.com/files/inspection/11bulg.htm','https://www.emhartglass.com/files/inspection/11como.htm','https://www.emhartglass.com/files/inspection/11dirw.htm','https://www.emhartglass.com/files/inspection/11drm.htm','https://www.emhartglass.com/files/inspection/11hpc.htm','https://www.emhartglass.com/files/inspection/11lmw.htm','https://www.emhartglass.com/files/inspection/11loma.htm','https://www.emhartglass.com/files/inspection/11prec.htm','https://www.emhartglass.com/files/inspection/11spik.htm','https://www.emhartglass.com/files/inspection/11sgp.htm','https://www.emhartglass.com/files/inspection/11susi.htm','https://www.emhartglass.com/files/inspection/11thin.htm','https://www.emhartglass.com/files/inspection/11wash.htm']
#base defect
table_urls_base=['https://www.emhartglass.com/files/inspection/12baff.htm','https://www.emhartglass.com/files/inspection/12basc.htm','https://www.emhartglass.com/files/inspection/12basl.htm','https://www.emhartglass.com/files/inspection/12blab.htm','https://www.emhartglass.com/files/inspection/12blib.htm','https://www.emhartglass.com/files/inspection/12dwb.htm','https://www.emhartglass.com/files/inspection/12spib.htm','https://www.emhartglass.com/files/inspection/12sgpb.htm','https://www.emhartglass.com/files/inspection/12swub.htm','https://www.emhartglass.com/files/inspection/12thb.htm','https://www.emhartglass.com/files/inspection/12thib.htm','https://www.emhartglass.com/files/inspection/12wedb.htm']
heading_urls_base=['https://www.emhartglass.com/files/inspection/11baff.htm','https://www.emhartglass.com/files/inspection/11basc.htm','https://www.emhartglass.com/files/inspection/11basl.htm','https://www.emhartglass.com/files/inspection/11blab.htm','https://www.emhartglass.com/files/inspection/11blib.htm','https://www.emhartglass.com/files/inspection/11dwb.htm','https://www.emhartglass.com/files/inspection/11spib.htm','https://www.emhartglass.com/files/inspection/11sgpb.htm','https://www.emhartglass.com/files/inspection/11swub.htm','https://www.emhartglass.com/files/inspection/11thb.htm','https://www.emhartglass.com/files/inspection/11thib.htm','https://www.emhartglass.com/files/inspection/11wedb.htm']
#general defect
table_urls_general=['https://www.emhartglass.com/files/inspection/12brow.htm','https://www.emhartglass.com/files/inspection/12oos.htm','https://www.emhartglass.com/files/inspection/12stuw.htm','https://www.emhartglass.com/files/inspection/12ubad.htm','https://www.emhartglass.com/files/inspection/12vert.htm']
heading_urls_general=['https://www.emhartglass.com/files/inspection/11brow.htm','https://www.emhartglass.com/files/inspection/11oos.htm','https://www.emhartglass.com/files/inspection/11stuw.htm','https://www.emhartglass.com/files/inspection/11ubad.htm','https://www.emhartglass.com/files/inspection/11vert.htm']

#master dictionary-> contains all the main defect types (finish/body/etc) along with machine dictionary
master_dictionary={}

#machine dictionary-> contains the name of the defect with its causes (machine operation only)
machine_dictionary={}


main_defects=['FINISH','NECK','SHOULDER','BODY','BASE','GENERAL']

#this gets the causes for the defect
def get_machine_defect_cause():
	res=[]
	table=soup.find('table',border=0)
	rows=table.find('tr')
	rows_content=rows.find_all('ul')
	rows_content_1=rows_content[2]
	rows_content_2=rows_content_1.find_all('li')

	output=[ele.text for ele in rows_content_2]
	for i in output:
		i=i.replace('\n','')
		i=re.sub(' +',' ',i)
		res.append(i)

	return res

#this fetches the name of the defect
def get_name_of_defect():
	table=soup.find_all('table')
	content=table[1].find_all('p')
	content=content[1].text
	content=content.replace('\n','')
	content=re.sub(' +',' ',content)
	return content


#main function which stores the causes along with name of defect in machine dictionary
#then stores it accordingly in the master dictionary
def machine_defect_dictionary(url1,url2,name_of_defect):
	global soup,req

	for url,url_2 in zip(url2,url1):
		machine_list=[]

		req=requests.get(url_2)
		soup=BeautifulSoup(req.text,'html.parser')

		name=get_name_of_defect()


		

		req=requests.get(url)
		soup=BeautifulSoup(req.text,'html.parser')

		machine_list=get_machine_defect_cause()

		machine_dictionary[name]=machine_list

	master_dictionary[name_of_defect]=machine_dictionary

	
machine_defect_dictionary(heading_urls_finish,table_urls_finish,main_defects[0])
machine_defect_dictionary(heading_urls_neck,table_urls_neck,main_defects[1])
machine_defect_dictionary(heading_urls_shoulder,table_urls_shoulder,main_defects[2])
machine_defect_dictionary(heading_urls_body,table_urls_body,main_defects[3])
machine_defect_dictionary(heading_urls_base,table_urls_base,main_defects[4])
machine_defect_dictionary(heading_urls_general,table_urls_general,main_defects[5])

print(master_dictionary)




print('Time Taken:',time.time()-start)

	
