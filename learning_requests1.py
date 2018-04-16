import requests
def input_data(email):
    with requests.Session() as c:
        url="https://lists.debian.org/cgi-bin/subscribe.pl"
        c.get(url)
        login_data={'user_email':email, 'list':'debian-outreach', 'action':'Subscribe'}   #entering user email in the input box
        c.post(url,data=login_data,stream=True)
