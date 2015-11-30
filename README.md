BTF - Initial Fabric Health checker (pre-alpha/alpha)
=====================

This script checks the fabric for the following policies:
mgmt address (out of band only right now)
ntp
dns
route reflectors
remote location

These policies are typically crucial for day 1 operations
and other policies rely on these policies to be configured.
Therefore for those unfamiliar with ACI this is a good health
checker to have during a test or dev environment before opening 
a TAC case.

********************************************************************
Furthermore the script will allow the user to configure the policies
that they are missing in the script. 
**THIS IS IN ALPHA TESTING AS NOT ALL FUNCTIONALITY HAS BEEN TESTED**
*****************USE CONFIGURATION FUNCTIONALITY AT OWN RISK*********
<br>
##### Requires: #####

bottle 0.12.9 
(setup script coming soon)
     
<br>  
##### Supports: #####

Cisco ACI - Will only find if a policy exists for the specific
protocol it checks. This script does not check to see if the policy
was properly configured.
<br>   

#### Instructions: ####
This script requires the Bottle Python Web Framework

Instructions on installing that can be found here:
http://bottlepy.org/docs/dev/index.html 

The application runs as a web based application and will run on TCP port 8082 
and the loopback IP address (127.0.0.1 or localhost) of the machine where it is running.
 it can be executed by typing in the terminal:

C:\Users\sheastma\PycharmProjects\test>python IF_bt_server.py

and then going to the following address: http://127.0.0.1:8082/IFC_main

If there is something else that this script should check for or suggestions 
please leave comments below.