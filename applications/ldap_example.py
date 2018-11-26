import pprint

import ldap

con = ldap.initialize('ldap://ldap.forumsys.com:389')
con.simple_bind_s("cn=read-only-admin,dc=example,dc=com", "password")
retrieve_attributes = None
search_filter = None
ldap_base = "ou=mathematicians,dc=example,dc=com"
search_scope = ldap.SCOPE_SUBTREE

ldap_result_id = con.search(ldap_base, search_scope, search_filter, retrieve_attributes)
result_set = []
while 1:
    result_type, result_data = con.result(ldap_result_id, 0)
    if result_data == []:
        break
    else:
        ## here you don't have to append to a list
        ## you could do whatever you want with the individual entry
        ## The appending to list is just for illustration.
        if result_type == ldap.RES_SEARCH_ENTRY:
            result_set.append(result_data)
pprint.pprint(result_set)
