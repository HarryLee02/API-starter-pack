<p>With OptiSigns, you can schedule TV Power On/Off using the advanced schedule feature. There are 2 ways you can do it with OptiSigns depending on what devices you are using.</p>
<ul>
<li>If you are using a consumer-grade TV and OptiSigns Pre-Configured Android Stick, the TV Power On/Off is achieved through HDMI-CEC. See our <strong><a href="https://support.optisigns.com/hc/en-us/articles/28598173096723-How-To-Create-and-Use-Operational-Schedules-HDMI-CEC-RS-232" target="_blank" rel="noopener noreferrer">Operational Schedule</a> </strong>article for more information.</li>
<li>If you are using a commercial-grade display, RS232 will be the option for you. </li>
</ul>
<p>In this article, we will walk through how to set up the external communication for RS-232 and use it to control your commercial display power on/off. It consists of 3 steps at a high level.</p>
<ol>
<li>Set up RS-232 connection for serial communication.</li>
<li>Configure the RS-232 command for your display and set up the template</li>
<li>Create the Power On/Off Schedule</li>
</ol>
<p>The same procedures can be used to send other RS 232 compliant commands as well.</p>
<p><span class="wysiwyg-underline">Supported devices/platforms:</span> Windows, Linux, Raspberry Pi, and OptiSigns Android Stick device.</p>
<p><span class="wysiwyg-font-size-x-large"><strong>1. Create RS-232 connection</strong></span></p>
<p>Go to the admin console and expand Advanced, click on the link for external communication. You can also use the link below.</p>
<p><a href="https://app.optisigns.com/app/s/external-coms" target="_self">https://app.optisigns.com/app/s/external-coms</a></p>
<p>Click "Add New" button, to create a new RS-232 connection. </p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32323154940819" alt="chrome_ThjlLpoiH0.png"></p>
<p>In the connection creation window, you can give a name to the connection and define the serial port to use, Baud Rate, Data bits, Stop bits, and Parity. This info is determined by the commercial display used, you should be able to get it from your TV user manual.  Flow control is normally not needed in this case, you can just leave it blank.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32323154949651" alt="chrome_972ixLupAY.png"></p>
<p>Click "Save", once the configuration is complete. </p>
<p>To know which serial port is used, you will need to check it on your device. Using Windows as an example, you can find it in the device manager, it will list out the COM port available. On Linux/Raspberry Pi, the serial port is normally "/dev/ttyS0" or "/dev/ttyUSB0" if a USB serial adapter is used. On OptiSigns pre-configured Android Stick, you can use "USB0" as the serial port. </p>
<p><img src="https://support.optisigns.com/hc/article_attachments/9062308259731" alt="mceclip2.png"></p>
<p> </p>
<p><span class="wysiwyg-font-size-x-large"><strong>2. Configure RS-232 command and set up the template</strong></span></p>
<p>Go to the "Commands" tab, and click the "Add New" button.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32323154954003" alt="chrome_kVTicFpYv5.png" width="725" height="206"></p>
<p>Set the RS-232 command of your commercial display in the pop-up window. You can choose "asc ii" or "hex" encoding depending on your TV, and the end of line value can be set here accordingly as well. </p>
<p>You will need to create a command for Power On, and a command for Power Off.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32323291436947" alt="chrome_QGt8AmZbeI.png"></p>
<p>Once commands are created, go to the "Templates" tab, this is where you map the commands to the Power On/Off action. You only need to create a template if the commands are different. For example, if you are only using Samsung commercial TVs, which all have the same commands for power on/off, then you only need to create one template for it, it can be used on all the Samsung TVs you have deployed.    </p>
<p> </p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32323151390739" alt="chrome_0RqFJkgyu4.png"></p>
<p>Map the command to the actions. The actions will be used in the advanced schedule. Save it after the mapping is complete, then the template is ready for use.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/9062485175059" alt="mceclip7.png"></p>
<p><span class="wysiwyg-font-size-x-large"><strong>3. Set up Power On/Off schedule</strong></span></p>
<p>Once the RS-232 configuration is complete, you will need to set up an Operational Schedule.</p>
<p>Go to the Edit Screens, then go to the <strong>Operational Schedule </strong>section. Hit <strong>New</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40414890419859"></p>
<p>You'll see the Operational Schedule screen. Here, click anywhere you'd like to schedule a Power On/Off.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40414890422803"></p>
<p>Once you've done this, you'll see this menu pop up on the side:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40414884380947"></p>
<p>Here, the relevant piece is <strong>Power</strong>. Clicking this will show a drop-down:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40414890424723"></p>
<p>To power your screen on or off using RS-232, there are two relevant options:</p>
<ul>
<li>
<strong>To Power Screen ON - </strong>Choose either <strong>On </strong>or <strong>RS-232 - On</strong>. The first option will make use of RS-232 first, then HDMI-CEC as a fallback. The second will only utilize RS-232.</li>
<li>
<strong>To Power Screen OFF - </strong>Choose either <strong>Off </strong>or <strong>RS-232 - Off</strong>. The first option will make use of RS-232 first, then HDMI-CEC as a fallback. The second will only utilize RS-232.</li>
</ul>
<p>That's all! Now you have learned how to schedule TV power on/off using RS-232.</p>
<p>If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self">support@optisigns.com</a></p>