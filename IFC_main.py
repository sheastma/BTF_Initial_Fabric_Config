__author__ = 'sheastma'
import requests
import json
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
class fabric_health():
    def __init__(self):
        self._mgmtaddr_ = False
        self._dns_ = False
        self._RR_ = False
        self._RL_ = False
        self._mgmt_contract_ = False
        self._ntp_ = False
    @property
    def mgmtaddr(self):
        return self._mgmtaddr_
    @property
    def dns(self):
        return self._dns_
    @property
    def ntp(self):
        return self._ntp_
    @property
    def RR(self):
        return self._RR_
    @property
    def RL(self):
        return self._RL_
    @property
    def mgmt_contract(self):
        return self._mgmt_contract_
    #@property
    def __getattr__(self, _class):
        if _class.startswith('mgmt'):
            return self.mgmtaddr
        if _class.startswith('dns'):
            return self.dns
        if _class.startswith('date'):
            return self.ntp
        if _class.startswith('bgp'):
            return self.RR
        if _class.startswith('file'):
            return self.RL
    def setatr(self, _class):
        if _class.startswith('mgmt'):
            self._mgmtaddr_ = True
        if _class.startswith('dns'):
            self.dns = True
        if _class.startswith('date'):
            self.ntp = True
        if _class.startswith('bgp'):
            self.RR = True
        if _class.startswith('file'):
            self.RL = True



def login( base_url, user, password):
    login_url = 'https://' + base_url + '/api/aaaLogin.json'
    name_pwd = {'aaaUser': {'attributes': {'name': user, 'pwd': password}}}
    json_credentials = json.dumps(name_pwd)
    try:
        post_response = requests.post(login_url, data=json_credentials, verify = False)
        post_response.raise_for_status()
    except requests.ConnectionError, e:
        return e
        exit(1)
    except requests.HTTPError, e:
        return e
        exit(1)
    auth = json.loads(post_response.text)
    login_attributes = auth['imdata'][0]['aaaLogin']['attributes']
    auth_token = login_attributes['token']
    # create cookie array from token
    cookies = {}
    cookies['APIC-Cookie'] = auth_token

    return cookies

def fabric_health_check( base_url, user, password):
    #fix this
    cookies =login( base_url, user, password)
    fabric = fabric_health()
    #print fabric.dns
    #fabric.dns = True
    #print fabric.dns
    classes = ['mgmtNodeGrp','mgmtRsOoBStNode','dnsProv','dnsDomain','datetimePol','bgpRRNodePEp','fileRemotePath']
    #mgmt address
    for _class in classes:
        try:
            fab_url = 'https://10.122.141.109/api/node/class/'+_class+'.json'
            #print fab_url
            get_response = requests.get(fab_url,verify = False, cookies = cookies)
            response = json.loads(get_response.text)
            if response['totalCount'] > 0:
               # print fabric.__getattr__(_class)
                fabric.setatr(_class)
                print fabric.__getattr__(_class)
                #test =  fabric.__getattr__(_class)#True

            #print str(fabric.dns)+" sdfsdfsdf"
        #print response['totalCount'] +'\n'
        except:
            return "ERROR: The following credentials were not correct or the APIC is not reachable"
    return str(fabric.dns)+','+str(fabric.mgmtaddr)+','+str(fabric.RR)+','+str(fabric.RL)+','+str(fabric.ntp)

def get_nodes(base_url, user, password):
        oob = ''
        DG = ''
        cookies =login( base_url, user, password)
        fab_url = 'https://'+base_url+'/api/node/class/fabricNode.json'
        get_response = requests.get(fab_url,verify = False, cookies = cookies)
        response = json.loads(get_response.text)
        Nodes = []
        count = int(response["totalCount"])
        #print count
        for i in xrange(0,count,1):
            temp = {'node': '','id':'', 'oob':'','DG':''}
            #Nnode = []
            temp['name'] = response['imdata'][i]['fabricNode']['attributes']['name']
            #print response['imdata'][i]['fabricNode']['attributes']['name']
            #Nnode.append(oob)
            #Nnode.append(DG)
            temp['id'] = response['imdata'][i]['fabricNode']['attributes']['id']
            #self.nodes.append(Nnode)
            Nodes.append(temp)
        return Nodes

def get_spines(base_url, user, password):
        cookies =login( base_url, user, password)
        fab_url = 'https://'+base_url+'/api/node/class/fabricNode.json'
        get_response = requests.get(fab_url,verify = False, cookies = cookies)
        response = json.loads(get_response.text)
        Nodes = []
        count = int(response["totalCount"])
        #print count
        for i in xrange(0,count,1):
            if response['imdata'][i]['fabricNode']['attributes']['role'] == "spine":

                temp = {'name': '','id':'', 'oob':'','DG':''}
            #Nnode = []
                temp['name'] = response['imdata'][i]['fabricNode']['attributes']['name']
            #print response['imdata'][i]['fabricNode']['attributes']['name']
            #Nnode.append(oob)
            #Nnode.append(DG)
                temp['id'] = response['imdata'][i]['fabricNode']['attributes']['id']
            #self.nodes.append(Nnode)
                Nodes.append(temp)
        return Nodes

def Postcall_oob(base_url, user, password, **kwargs):

    cookies =login( base_url, user, password)
    url_16 = 'https://'+base_url+'/api/node/mo/uni/fabric/funcprof/podpgrp-default.json'
    data_16 = {"fabricPodPGrp":{"attributes":{"dn":"uni/fabric/funcprof/podpgrp-default","status":"modified"},"children":[{"fabricRsTimePol":{"attributes":{"tnDatetimePolName":"default"},"children":[]}},{"fabricRsPodPGrpBGPRRP":{"attributes":{"tnBgpInstPolName":"default"},"children":[]}}]}}
    dump_16 = json.dumps(data_16)
    requests.post(url_16,data = dump_16, verify = False, cookies = cookies)
    Nodes = kwargs["Nodes"]
    temp_msg = ""
    for node in Nodes:
        if node["oob"] != '':
            try:
                url_17 = 'https://'+base_url+'/api/node/mo/uni/tn-mgmt/mgmtp-default/oob-default/rsooBStNode-[topology/pod-1/node-'+node["id"]+'].json'
                data_17 = {"mgmtRsOoBStNode":{"attributes":{"addr":node["oob"],"tDn":"topology/pod-1/node-"+node["id"],"gw":node["DG"],"status":"created"}}}
                dump_17 = json.dumps(data_17)
                requests_17 = requests.post(url_17,data = dump_17,verify = False, cookies = cookies)
                temp_msg += "<br>Successful for "+node["name"]
                requests_17.raise_for_status()

            except requests.HTTPError, e:
                temp_msg += e.errormessage(str(e.message)+" Unable to give a OOB address for "+node["name"]+". Check to make sure one does not already exist")
    return temp_msg

def Postcall_dns(base_url, user, password, **kwargs):
        cookies =login( base_url, user, password)
        if kwargs["dns_provide"] != "None":
            try:
                dns_url = 'https://'+base_url+'/api/node/mo/uni/fabric/dnsp-default/prov-['+kwargs["dns_provide"]+'].json'
                data = {"dnsProv":{"attributes":{"dn":"uni/fabric/dnsp-default/prov-["+kwargs["dns_provide"]+"]","addr":kwargs["dns_provide"],"status":"created","rn":"prov-["+kwargs["dns_provide"]+"]"}}}
                dump = json.dumps(data)
                get_response = requests.post(dns_url,data = dump,verify = False, cookies = cookies)
                print get_response
                print dns_url
                response = json.loads(get_response.text)
                kwargs["dns_flag"] = (True)
                get_response.raise_for_status()
            except requests.HTTPError, e:
                print "The DNS IP address was not correctly formatted. Please run the script again."
                print e.message
                (str(e.message) + "The DNS IP address you provided is either already being used or not valid. Please try again.")
                #self.dns_gui()
                #self.dns_flag.set(False)

        if kwargs["dns_domain"] != "None":
            try:
                dns_url_2 = 'https://'+base_url+'/api/node/mo/uni/fabric/dnsp-default/dom-'+kwargs["dns_domain"]+'.json'
                data_2 = {"dnsDomain":{"attributes":{"dn":"uni/fabric/dnsp-default/dom-"+kwargs["dns_domain"],"name":kwargs["dns_domain"],"status":"created","rn":"dom-"+kwargs["dns_domain"]}}}
                dump_2 = json.dumps(data_2)
                get_response_2 = requests.post(dns_url_2,data = dump_2,verify = False, cookies = cookies)
                get_response_2.raise_for_status()
                return "SUCCESSFUL"
            except requests.HTTPError, e:
                (str(e.message) + "The DNS domain name you provided is either already being used or not valid. Please try again.")
                #self.dns_gui()
                #self.dns_flag.set(False)

def Postcall_ntp(base_url,user, password, **kwargs):
        cookies =login( base_url, user, password)
        if kwargs["ntp_name"] != "":
            print kwargs["dns_flag"]
            if kwargs["dns_flag"] == False and re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', str(kwargs["ntp_name"])) is None:
                return "DNS was not configured. Please re-enter the dns address in the form of a IP address i.e. 1.1.1.1"
                #self.ntp_gui()
            else:
                try:
                    dns_url_4 = 'https://'+base_url+'/api/node/mo/uni/fabric/time-default/ntpprov-'+kwargs["ntp_name"]+'.json'
                    data_4 = {"datetimeNtpProv":{"attributes":{"dn":"uni/fabric/time-default/ntpprov-"+kwargs["ntp_name"],"name":kwargs["ntp_name"],"rn":"ntpprov-"+kwargs["ntp_name"],"status":"created"}}}
                    dump_4 = json.dumps(data_4)
                    get_response_4 = requests.post(dns_url_4,data = dump_4,verify = False, cookies = cookies)
                    get_response_4.raise_for_status()
                except requests.HTTPError, e:
                    return (str(e.message) + "The NTP name you provided is either already being used or not valid. Please try again.")
                    #self.ntp_gui()
def Postcall_rmte(base_url,user, password, **kwargs):
    cookies =login( base_url, user, password)
    if kwargs["rmte_ip"] != "":
        if kwargs["dns_flag"] == False and re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', str(kwargs["rmte_ip"])) is None:
            return ("DNS was not configured. Please re-enter the dns address in the form of a IP address i.e. 1.1.1.1")
            #self.ext_location()
        if kwargs["rmte_proto"] == "TFTP":
            try:
                url_6 = 'https://'+base_url+'/api/node/mo/uni/fabric/path-exp_path.json'
                data_6 = {"fileRemotePath":{"attributes":{"dn":"uni/fabric/path-exp_path","remotePort":kwargs["rmte_port"],"name":"exp_path","host":kwargs["rmte_ip"],"remotePath":kwargs["rmte_path"],"userName":kwargs["rmte_user"],"userPasswd":kwargs["rmte_Passwd"],"rn":"path-exp_path","status":"created"},"children":[{"fileRsARemoteHostToEpg":{"attributes":{"tDn":"uni/tn-mgmt/mgmtp-default/oob-default","status":"created"}}}]}}
                dump_6 = json.dumps(data_6)
                get_response_6 = requests.post(url_6,data = dump_6,verify = False, cookies = cookies)
                return "Successful"
                #return "past post"
                get_response_6.raise_for_status()
            except requests.HTTPError, e:
                return (str(e.message) + "The remote location name/ip address you provided is either already being used or not valid. Please try again.")
                #self.ext_location()
    if kwargs["rmte_proto"] == "FTP" or kwargs["rmte_proto"] == "SCP":
        try:
            url_6 = 'https://'+base_url+'/api/node/mo/uni/fabric/path-exp_path.json'
            data_6 = {"fileRemotePath":{"attributes":{"dn":"uni/fabric/path-exp_path","remotePort":kwargs["rmte_port"],"name":"exp_path","host":kwargs["rmte_ip"],"protocol":kwargs["rmte_proto"],"remotePath":kwargs["rmte_path"],"userName":kwargs["rmte_user"],"userPasswd":kwargs["rmte_Passwd"],"rn":"path-exp_path","status":"created"},"children":[{"fileRsARemoteHostToEpg":{"attributes":{"tDn":"uni/tn-mgmt/mgmtp-default/oob-default","status":"created"}}}]}}
            dump_6 = json.dumps(data_6)
            return "before"
            get_response_6 = requests.post(url_6,data = dump_6,verify = False, cookies = cookies)
            return "Successful"
            #print "past post"
            get_response_6.raise_for_status()

        except:
            return str(e.message) + "The remote location name/ip address you provided is either already being used or not valid. Please try again."
            #self.ext_location()

def Postcall_spine(base_url,user, password, **kwargs):
        cookies =login( base_url, user, password)
        temp_msg = ""
        for i in xrange(0,len(kwargs["spines"]),1):
            #print "this"+ self.spines[i].get()
            if len(kwargs["spines"]) != "0":
                try:
                    url_11 = 'https://'+base_url+'/api/node/mo/uni/fabric/bgpInstP-default/rr/node-'+kwargs["spines"][i]["id"]+'.json'
                    data_11 = {"bgpRRNodePEp":{"attributes":{"dn":"uni/fabric/bgpInstP-default/rr/node-"+kwargs["spines"][i]["id"],"id":kwargs["spines"][i]["id"],"rn":"node-"+kwargs["spines"][i]["id"],"status":"created"}}}
                    dump_11 = json.dumps(data_11)
                    get_response_11 = requests.post(url_11,data = dump_11,verify = False, cookies = cookies)
                    get_response_11.raise_for_status()
                    temp_msg += "Successful for node "+kwargs["spines"][i]["id"]
                    response_11 = json.loads(get_response_11.text)
                except requests.HTTPError, e:
                    temp_msg += (str(e.message)+" Unable to create a route reflector for Spine "+kwargs["spines"][i]["id"]+" Please verify it does not already exist")
def Postcall_AS(base_url,user, password, **kwargs):
    cookies =login( base_url, user, password)
    if kwargs["AS"] != "0":
        try:
            if int(kwargs["AS"]) <1 or int(kwargs["AS"]) > 4294967295:
                return (str(kwargs["AS"])+ " is not a valid ASN. Please enter a number between 1 and 4294967295")
                #self.route_refector_AS_gui()
        except:
            return ("You did not provide a proper integer. "+ kwargs["AS"]+ " is not a integer." )
            #self.route_refector_AS_gui()

        try:
            url_12 ='https://'+base_url+'/api/node/mo/uni/fabric/bgpInstP-default/as.json'
            data_12 = {"bgpAsP":{"attributes":{"dn":"uni/fabric/bgpInstP-default/as","asn":str(kwargs["AS"])}}}
            dump_12 = json.dumps(data_12)
            a=requests.post(url_12,data = dump_12,verify = False, cookies = cookies)
            return "Successful"
        except:
            "Unsuccessful"


fabric_health_check('10.122.141.109','admin','aci_sol*2')