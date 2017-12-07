from .models import Cost,Information
from bs4 import BeautifulSoup as bs
import requests


class cost_tu:

    def cse(self):
        #a = Information.objects.update(u_name='pciu', url='http//www.in.com', city='CTG')
        print('working')
        url = "https://daffodilvarsity.edu.bd/page/show_page_detail/tuition-fee"
        r = requests.get(url)
        soup = bs(r.content, 'lxml')
        tag=soup.select('a[href="http://cse.daffodilvarsity.edu.bd/"]')
        #print("CSE")
        cse = int(tag[0].parent.parent.find_all('td')[6].text.strip().replace(',',''))
        print("tk:",cse)

        eee = soup.select('a[href="http://eee.daffodilvarsity.edu.bd/"]')
        #print("EEE")
        #print("tk:",eee[0].parent.parent.find_all('td')[6].text.strip())

        bba = soup.select('a[href="http://bba.daffodilvarsity.edu.bd/"]')
        #print("BBA")
        #print("tk:",bba[0].parent.parent.find_all('td')[6].text.strip())

        llb = soup.select('a[href="http://law.daffodilvarsity.edu.bd/"]')
        #print("LLB")
        #print("tk:",llb[0].parent.parent.find_all('td')[6].text.strip())
        di = {'cse':tag[0].parent.parent.find_all('td')[6].text.strip().replace(',',''),
              'bba':bba[0].parent.parent.find_all('td')[6].text.strip().replace(',','')}
        inf = Information.objects.get(short_name = 'diu')
        for i in di.items():
            #print(i[0])
            #print(i[1])
            try :
                print("try")
                l = inf.cost_set.get(subject__iexact=i[0])
                print("ob",l)
                val = int(i[1])
                print(val)
                print("ob tk",l.cost)
                l.cost = val
                l.save() #cost field save only
                print("save")
            except :
                print("error")
                #pass
        #l.cost
        #key = [i for i in dic.keys()] val = [i for i in dic.values() ]
        # for i in di.items(): key=i[0] val=i[1]
