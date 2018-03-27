import requests
def pranav(email):
    with requests.Session() as c:
        url="https://lists.debian.org/cgi-bin/subscribe.pl"
        c.get(url)
        login_data={'user_email':email, 'list':'debian-outreach', 'action':'Subscribe'}
        c.post(url,data=login_data,stream=True)
