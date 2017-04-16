from pyzabbix import ZabbixAPI

zapi = ZabbixAPI("https://zabbix.ru/")
zapi.login("login", "pass")

ids = [group['groupid'] for group in zapi.hostgroup.get()] # get all id of hostgroups

rights = [{'permission': 2, 'id': i} for i in ids]	# get array of permission, id of hostgroups
usrgrpids = zapi.usergroup.get()	# get id of usergroup
for uid in usrgrpids:
    if uid['name'] =='Support':
        usrgrpid = uid['usrgrpid']

zapi.usergroup.update(	# update usergroup with rights
    usrgrpid=usrgrpid,
    rights=rights
)