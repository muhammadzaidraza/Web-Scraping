from bs4 import BeautifulSoup

with open("home.html","r") as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content,"lxml")
    #print(soup.prettify())
    
    tags = soup.find("h5") #find method will only find the first h5 tag and stp the execution of code
    #print(tags)

    all_tags = soup.find_all("h5")
    #print(all_tags)
    for course in all_tags:
        print(course.text)

