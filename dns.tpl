<link rel="stylesheet" type="text/css" href="../../static/dns.css">

<body style = "background-color:#CCCCCA">
<img id="banner" style = "bg-color:CBCCCE" src="static/Cisco_emailHeader.png" alt="Banner Image"/>
<div style="width: 800px;height: 100px;position: absolute;top:0;bottom: 0;left: 0;right: 0;margin: auto;">
<h1>DNS</h1>
<form action="/IFC_config/fabric_config/dns" method="POST">
DNS address: <input id = "dns_addr" type="text" name="dns_addr"><br>
DNS Domain: <input id = "dns_domain" type="text" name="dns_domain"><br>
TEST : <input id = "dns_domain_test" type="text" name="dns_domain_test"><br>
<input type="submit" value="Submit">
</div>
</body>
<script language="JavaScript" type="text/javascript" src="../../static/dns.js"></script>