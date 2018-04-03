import re
def fun(s):
    res = re.match(r'(.*)@(.*?)\.(.*)', s)

    try:
        user_name = res.group(1)
        website_name = res.group(2)
        length_to_judge = res.group(3)
    except:
        return False
    else:
        if len(user_name) == 0:
            return False
        
        if len(length_to_judge) > 3:
            return False
        
        for each in user_name:
            if '0' <= each <= '9' or 'a' <= each <= 'z' or 'A' <= each <= 'Z' or each =='-' or each == '_':
                continue
            else:
                return False

        for each in website_name:
            if '0' <= each <= '9' or 'a' <= each <= 'z' or 'A' <= each <= 'Z':
                continue 
            else:
                return False

        return True 

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