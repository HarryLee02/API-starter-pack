<p>When you are trying to connect to 802.1x WiFi with WPA enterprise on Raspberry Pi,  you will see the WiFi access point is greyed out on Raspberry Pi, like below. It is because Raspberry Pi is using the simple network service on the GUI, which doesn't support enterprise WiFi.  However, Raspberry Pi is supporting 802.1x enterprise WiFi. And the simplest way to setup the connection to 802.1x enterprise WiFi on Raspberry Pi is to use standard Linux network manager to replace the simple network service. In this tutorial, we will walk through how to set it up.  </p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4411750345875" alt="mceclip0.png"></p>
<p><strong>Open the terminal window on Raspberry Pi, and run below commands to get the standard Linux network manager installed.</strong></p>
<p> </p>
<p>sudo apt install network-manager network-manager-gnome<br>sudo systemctl disable --now dhcpcd<br>sudo systemctl enable --now network-manager</p>
<p>sudo reboot</p>
<p><strong>Explanation:</strong></p>
<p>1st line is to install the Linux network manager</p>
<p>2nd line is to disable the DHCP, because DHCP will not work with the network manager</p>
<p>3rd line is to enable the network manager service</p>
<p>Last line is to reboot the device.</p>
<p><strong>After rebooting the device, you will be able to see a new network icon, click on the icon, you will not be able to connect to the 802.1x enterprise WiFi.</strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4411743714067" alt="mceclip1.png"></p>
<p> </p>
<p><strong>Then fill in the information as you normally do with 802.1x enterprise WiFi connection, and you will now be able to connect to the network.</strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4411743744787" alt="mceclip2.png"></p>
<p> </p>
<p><strong>That's it! You're ready to go.</strong></p>
<p><strong>Note:</strong> To download and install the network manager, you will need internet connection first. Please consider have it connected to a wired network or another normal WiFi network first to get it setup.</p>
<p> </p>
<p>If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self" rel="undefined">support@optisigns.com</a> </p>