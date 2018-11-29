#https://leetcode.com/problems/unique-email-addresses/
def numUniqueEmails(emails):
    email_list = []
    for email in emails:        
        name = email.split('@')[0]
        domain = email.split('@')[1]
        name = name.replace('.', '')
        if '+' in name:
            name = name.split('+')[0]
            email_list.append(name + '@' + domain)
        else :
            email_list.append(name + '@' + domain)
    email_list = set(email_list)
    return email_list
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(numUniqueEmails(emails))