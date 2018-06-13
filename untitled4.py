'''
This is the code for webscraping of the only given website for getting better performance
Do change the website name for result of the particular website in (line no:32)
websites:
https://www.4coffshore.com/windfarms/gujarat---flowocean-ab-india-in21.html
https://www.4coffshore.com/windfarms/gujarat---greenshore-energy-india-in08.html
https://www.4coffshore.com/windfarms/mnre-offshore-wind-turbine-demonstration-project---arichal-munai---dhanushkodi-india-in23.html
https://www.4coffshore.com/windfarms/ongc---commercial-project-india-in07.html
https://www.4coffshore.com/windfarms/ongc---pilot-project-india-in06.html
https://www.4coffshore.com/windfarms/ongc---vertical-axis-pilot-project-india-in12.html
https://www.4coffshore.com/windfarms/tamil-nadu---bharat-light-%26-power-india-in09.html
https://www.4coffshore.com/windfarms/tamil-nadu---flowocean-ab-india-in20.html
https://www.4coffshore.com/windfarms/tamil-nadu---greenshore-energy-india-in11.html
https://www.4coffshore.com/windfarms/tamil-nadu---suzlon-india-in10.html
https://www.4coffshore.com/windfarms/tamil-nadu-energy-development-agency-(teda)-india-in18.html
https://www.4coffshore.com/windfarms/first-1000-mw-commercial-offshore-wind-farm-in-india-india-in15.html
https://www.4coffshore.com/windfarms/fowind---facilitating-offshore-wind-in-india---gujarat-india-in19.html
https://www.4coffshore.com/windfarms/fowind---facilitating-offshore-wind-in-india---tamil-nadu-india-in16.html
https://www.4coffshore.com/windfarms/gujarat---tata-power-india-in05.html

'''


from bs4 import BeautifulSoup
import urllib.request 


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()
response1 = opener.open('https://www.4coffshore.com/windfarms/gujarat---flowocean-ab-india-in21.html')
content1=response1.read()
soup1 = BeautifulSoup(content1, 'html.parser')

filename="list1.csv"
f=open(filename,"w")
headers="Role,Organisation\n"

soup2=soup1.find_all("h2")[0]
topic=soup2.find("span").get_text()
f.write(" "+","+topic+"\n")

soup3=soup1.find_all("p")[0]
topic2=soup3.find("span",class_="text-black").get_text()
f.write(" "+","+topic2)


heading=soup1.find_all("span",class_="h4 bold")[0].get_text()
print(heading) 
f.write(heading+"\n")

f.write(headers)

table0=soup1.find_all("table",class_="table table-striped")[0]
rows0= table0.find_all("tr")


for i in rows0:
    
    try:
        name01 = i.find("td" ,class_="gvshRoleCol").find("span",class_="gvshRole").get_text()
        name02 = i.find("td" ,class_="gvshOrgCol").find("div",class_="gvshOrg").find("a").get_text()
        name03 = i.find("td" ,class_="gvshOrgCol").find("div",class_="gvshDesc").find("a").get_text()
        
       
        print(name01)
        print(name02)
        print(name03)
        f.write(name01)
        f.write(","+name02+"\n")
        f.write(" "+","+name03+"\n")
    except:
        pass
    


heading1=soup1.find_all("span",class_="h4 bold")[1].get_text()
print(heading1)
f.write(heading1+"\n")


table=soup1.find_all("table",class_="tblProject")[0]
rows= table.find_all("tr")


for i in rows:
    try:
        head=i.find("td", class_="uccol1Head").get_text()
        print(head)
        f.write(head)
    except:
        pass
    try:
        name1 = i.find("td" ,class_="uccol2").get_text()
        name2 = i.find("span",class_="attr").get_text()  
        print(name1+" --- "+name2) 
        f.write(" "+","+name1+","+name2+"\n")
      
    
    except:
        pass
        
table1=soup1.find_all("table",class_="tblProject")[1]
rows1= table1.find_all("tr")

for i in rows1:
    try:
        head1=i.find("td", class_="uccol1Head").get_text()
        print(head1)
        f.write(head1)
    except:
        pass
    try:
        name11 = i.find("td" ,class_="uccol2").get_text()
        name21 = i.find("span",class_="attr").get_text()

        
        print(name11+" --- "+name21) 
        f.write(" "+","+name11+","+name21+"\n")
    except:
        pass

############################################################################################