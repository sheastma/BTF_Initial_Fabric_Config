__author__ = 'sheastma'
import bottle as bt
from bottle import route, run, template,static_file, response
import IFC_main
import socket


ipaddr = ''
username = ''
password = ''
global dns_flag
dns_flag = False
def __unicode__(self):
   return unicode(self.some_field) or u''

@route('/IFC_main', method = "GET")
def index():
    #f = open('login.html')
    return template('login.tpl')


@route('/IFC_main', method = "POST")
def main():
    global ipaddr
    ipaddr = bt.request.forms.get('A_ip')
    global username
    username = bt.request.forms.get('user_id')
    global password
    password = bt.request.forms.get('user_password')
    #print bt.request.forms.get('1')
    #print ipaddr+username+password
    response = IFC_main.fabric_health_check(ipaddr,username,password)
    response = response.split(',')
    if len(response) <= 1:
        return response
    return template('IFC_main.tpl',DNS =response[0],mgmt = response[1],RR=response[2],RL = response[3],NTP =response[4])

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/IFC_config/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')



@route('/IFC_config/<policy>')
def config(policy):
    if policy == "mgmt":
        global Nodes
        Nodes = IFC_main.get_nodes(ipaddr,username,password)
        return template("mgmt.tpl",nodes = Nodes)
    if policy == "dns":
        return template("dns.tpl")
    if policy == "ntp":
        return template("ntp.tpl")
    if policy == "rr":
        global Spines
        Spines = IFC_main.get_spines(ipaddr,username,password)
        return template("rr.tpl", spines = Spines)
    if policy == "rl":
        return template("rl.tpl")

@route('/IFC_config/node_info/<node>')
def node(node):
    for nd in Nodes:
        if node == nd["name"]:
            return nd["id"]+ ","+ nd["oob"] +","+ nd["DG"]

@route('/IFC_config/node_config/<data:path>')
def config(data):
    Nname,Naddr,Ndg = data.split(",")
    valid_ip = Naddr.split("/")
    if len(valid_ip) != 2: return "ip_invalid"
    try:
        socket.inet_aton(valid_ip[0])
        socket.inet_aton(Ndg)
        if 1 > int(valid_ip[1]) > 32:
            return "ip_invalid"
    except socket.error:
        return "ip_invalid"
    for nd in Nodes:
        if Nname == nd["name"]:
            nd["oob"] = Naddr
            print nd["oob"]
            nd["DG"] = Ndg
            print nd["DG"]
            return "successful"

@route('/IFC_config/fabric_config/<data>', method = "POST")
def fabric_config(data):
   #print data
   #print bt.request.forms.get('dns_addr')
    if data == "mgmt":
        return IFC_main.Postcall_oob(ipaddr,username,password, Nodes=Nodes)
    if data == "dns":
        print data
        dns_provide = bt.request.forms.get('dns_addr')
        dns_domain = bt.request.forms.get('dns_domain')
        return IFC_main.Postcall_dns(ipaddr,username,password, dns_provide=dns_provide,dns_domain=dns_domain,dns_flag=dns_flag)
    if data == "ntp":
        ntp_name = bt.request.forms.get('ntp_addr')
        IFC_main.Postcall_ntp(ipaddr,username, password, ntp_name=ntp_name, dns_flag=dns_flag)
    if data == "rr":
        rr = []
        temp = {"name": "","id": ""}
        AS = bt.request.forms.get('ASN')
        for spine in Spines:
            temp["name"] = bt.request.forms.get(spine["name"])
            temp["id"] = spine["id"]
            rr.append(temp)
        IFC_main.Postcall_spine(ipaddr,username, password,spines=rr )
        IFC_main.Postcall_AS(ipaddr,username, password, AS=AS)
        print "rr"

    if data == "rl":
        rmte_ip = bt.request.forms.get('rl_addr')
        rmte_path = bt.request.forms.get('remote_path')
        rmte_port =  bt.request.forms.get('remote_port')
        rmte_proto = bt.request.forms.get('rl_proto')
        rmte_user = bt.request.forms.get('rl_user')
        rmte_Passwd = bt.request.forms.get('rl_pwd')
        print rmte_proto
        return IFC_main.Postcall_rmte(ipaddr,username, password, rmte_ip=rmte_ip, rmte_path=rmte_path, rmte_port = rmte_port,
        rmte_proto= rmte_proto, rmte_user = rmte_user, rmte_Passwd = rmte_Passwd, dns_flag=dns_flag)
        print "rl"

run(host='localhost', port=8082)
