import re
def fun(s):
    try:
        user_name, url = s.split('@')
        website_name, extension = url.split('.')
    except:
        return (False)
    else:
        if not user_name.replace('_','').replace('-','').isalnum():
            return (False)
        if not website_name.isalnum():
            return (False)
        if len(extension) > 3:
            return (False)
    return (True)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)