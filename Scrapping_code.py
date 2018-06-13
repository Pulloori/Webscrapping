
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