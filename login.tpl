<script language="JavaScript" type="text/javascript" src="/static/login.js"></script>
<link rel="stylesheet" type="text/css" href="/static/login.css">

<body style = "background-color:#CCCCCA">
<img id="banner" style = "bg-color:CBCCCE" src="static/Cisco_emailHeader.png" alt="Banner Image"/>
<div style="width: 800px;height: 100px;position: absolute;top:0;bottom: 0;left: 0;right: 0;margin: auto;">
<div id='platform_options' class="outerbox" >
	<div class="header">
		<span class="stepspan">Step 1</span>
		APIC credentials
	<form action="/IFC_main" method="post">
	</div>
	<div class="innerbox">
	<div class='radio_div'><input onkeyup="validate_ip(this)" name="A_ip" id="A_ip"><label class="label" for="A_ip" id="A_ip_label">APIC IP</label></div>
    <div class='radio_div'><input name="user_id" id="user_id"><label class="label" for="user_id" id="user_id_label">APIC USER ID</label></div>
    <div class='radio_div'><input input type = password name="user_password" id="user_password"><label class="label" for="user_password" id="user_password_label">APIC PASSWORD</label>
    </div>
	</div>
</div>


<div class="generate_div outerbox"><input value = "Login" type = "submit"/></div>
</form>
<div class="innerbox">
        <pre id="elam_trigger"></pre>
	</div>
</div>
</body>