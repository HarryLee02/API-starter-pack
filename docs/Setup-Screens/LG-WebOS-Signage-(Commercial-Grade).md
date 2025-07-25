<p>LG is one of the world leader in manufacturing commercial grade TV screens that are used in hotels, restaurants, retails and other environment.</p>
<p>OptiSigns does support LG WebOS Signage, all apps, features are supported, include offline playback and auto update of OptiSigns app on LG WebOS Signage devices.</p>
<p>Please note that this article is for installing OptiSigns on LG WebOS Signage devices only, the screens should be marked as "LG Digital Signage". For the normal consumer TV with LG WebOS, please use the <a href="https://www.optisigns.com/post/how-to-use-optisigns-with-browser" target="_self">normal webplayer</a>.</p>
<h4 id="h_01HQF5DZEQP2BEYX4FN21BTAYW"><strong>The installation process is easy, you have 2 options:</strong></h4>
<p><span class="wysiwyg-underline">1) Installation from a USB drive:</span> this is the easiest as you don't need to use remote to type in a URL, and it's useful if you have a lot of TVs to set up, you can use the same USB to set them up quickly.<br><span class="wysiwyg-underline">2) Installation from server:</span> if you don't have or don't want to use USB drive, just need to punch in the URL: <a href="https://links.optisigns.com/lg">https://links.optisigns.com/lg</a> in your SI server TV settings (see detail below)</p>
<h4 id="h_01HQF5DZEQ86A5B3SK0NCCJ04K"><strong>Before you begin:</strong></h4>
<p>- Ensure your TV is factory reset with basic settings</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4414497081107" alt="mceclip0.png" width="533" height="301"></p>
<p>- Connect to internet (WiFi or Ethernet)</p>
<p>- Set up date, time this is to ensure schedule will play correctly with your time zone</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4414489377299" alt="mceclip1.png" width="537" height="317"></p>
<h4 id="h_01HQF5DZEQ36F58NAAVQEE08ZB"><strong>1) Installation from a USB Drive:</strong></h4>
<p>Download the this file <a href="https://links.optisigns.com/lg" target="_self">com.lg.app.signage.ipk</a> to your computer.</p>
<p>Format your USB Drive to FAT32 if you not already have it.<br>Create a folder named <strong>‘application’</strong> in the root of your USB drive <br>Copy the .ipk file into this folder <br><img src="https://support.optisigns.com/hc/article_attachments/4414485674899" alt="mceclip3.png"><br>Insert the USB drive to the LG TV's USB port.</p>
<p>On the TV, enter the settings menu (press the config wheel icon on the remote controller)<br>Navigate to: EZ Setting -&gt; SI Server Setting</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4414497608211" alt="mceclip5.png"></p>
<p>Select SI Server Setting</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4414490220051" alt="mceclip6.png"></p>
<p>In this page, set the ‘Application Launch Mode’ to ‘Local’ <br>Set the ‘Application Type’ to ‘IPK’<br>Then finally click ‘Local Application Upgrade’ -&gt; ‘USB’</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4414497878419" alt="mceclip7.png"> <br>Confirm your intent to install the application</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4414498104851" alt="mceclip8.png"></p>
<p>If your USB thumbdrive prepared correctly, you will see message confirm that the upgrade is completed</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4414490483859" alt="mceclip9.png"><br>After that power off, and power on the TV.</p>
<p>When the TV come back up, you will see it's updating:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4414498126355" alt="mceclip10.png"></p>
<p>After update completed, it will show this message:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4414490508179" alt="mceclip11.png"></p>
<p>And OptiSigns app will automatically be started, you will see the pairing code, you can start pairing it on app.optisigns.com and assign content to it there.<br>The installation process is completed, you now can remove the USB drive.<br>From now on, OptiSigns app will be automatically started with the TV, and it will also automatically check for updates itself.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4414487042195" alt="mceclip12.png"></p>
<h4 id="h_01HQF5DZEQDSDGP8EA0DRSWJQB"><strong>2) Installation from server:</strong></h4>
<p>On the TV, enter the settings menu (press the config wheel icon on the remote controller)<br>Navigate to: EZ Setting -&gt; SI Server Setting</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4414497608211" alt="mceclip5.png"></p>
<p>Select SI Server Setting</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4414490220051" alt="mceclip6.png"></p>
<p>Set ‘Fully Qualified Domain Name’ to ‘On’ <br>Then enter ‘https://links.optisigns.com/lg’ into the input field<br>Set the ‘Application Launch Mode’ to ‘Local’ <br>Set the ‘Application Type’ to ‘IPK’ <br>Finally click ‘Local Application Upgrade’ -&gt; ‘REMOTE’</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4414487226771" alt="mceclip13.png"></p>
<p>Confirm your intent to install the application</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4414487260307" alt="mceclip14.png"> <br>If the FQDN URL is misspelled you will see an error message and have to modify the URL.<br>If the FQDN URL is correct, you will see this message confirm upgrade completed.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4414487276947" alt="mceclip15.png"></p>
<p>After that power off, and power on the TV.</p>
<p>When the TV come back up, you will see it's updating:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4414498126355" alt="mceclip10.png"></p>
<p>After update completed, it will show this message:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4414490508179" alt="mceclip11.png"></p>
<p>And OptiSigns app will automatically be started, you will see the pairing code, you can start pairing it on app.optisigns.com and assign content to it there.<br>From now on, OptiSigns app will be automatically started with the TV, and it will also automatically check for updates itself.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4414487042195" alt="mceclip12.png"></p>
<p> </p>
<h4 id="h_01HQF5DZEQBYMNQ1B64TXJGVSA"><strong>Batch installation from the server URL with settings from a USB drive:</strong></h4>
<p>Instead of typing in the URL and change settings for reach device, you can create USB drive to re-use it on many screens.<br>1) Create a file named ‘scap_installation.json’ on your computer with this content:</p>
<pre> <br>{<br>“serverIp” : “0.0.0.0”,<br>“serverPort” : 0,<br>“secureConnection” : false,<br>“fqdnMode” : true,<br>“fqdnAddr” : “https://links.optisigns.com/lg”,<br>“appLaunchMode” : “local”,<br>“appType” : “ipk”<br>}</pre>
<p>2) Copy this file into the root of the USB drive <br>3) Insert the USB drive into the device and start/reboot it<br>4) Once the installation finish, restart the TV and OptiSigns app will AutoStart.</p>
<p><strong>To check which LG WebOS Signage firmware version is installed on the device:</strong> <br>Enter the settings menu (the config wheel icon on the remote) <br>Navigate to ‘General’ -&gt; ‘System Information’</p>
<h4 id="h_01HQF5DZEQK9A646EPZERZZEE6">
<strong>To upgrade the </strong><strong>LG WebOS Signage firmware </strong><strong>on the device:</strong>
</h4>
<p>If you are running WebOs 4.1 or older, you may need to upgrade your Firmware to for the device to be able to play OptiSigns apps like Weather, Social Medias, etc.<br>Get the latest firmware file (.epk) from <a href="https://partner.lge.com/global/portal/main/main/fowardMenuUrl.lge?_MenuId=210099&amp;_MenuLevel=3&amp;_MenuParentId=210021&amp;_SuperCategoryCode=&amp;_searchKeyWord=&amp;pageName=&amp;gdprChk=&amp;pwConfirmYn=&amp;popupYn=&amp;menuType=C&amp;_SuperCategoryCode=&amp;needReload=&amp;siteCountryCode=global&amp;corporationCode=LGEHQ&amp;obuCode=" target="_blank" rel="noopener noreferrer">LG website</a> (please see <a href="https://www.lg.com/us/support/help-library/lg-tv-how-to-manually-update-software--20154165668198" target="_blank" rel="noopener noreferrer">this article on LG's website</a>, contact us, or LG if you need help)<br>Create a folder names ‘LG_MONITOR’ in the root of your USB drive <br>Copy the new firmware .epk file into it <br>Insert the USB drive into the TV's USB port<br>The update menu will automatically appear <br>Click on ‘Update’ and wait till the process finishes</p>
<h4 id="h_01HQF5DZEQHDBNWE47HVEX1G9D"><strong>Copy config from 1 device to another:</strong></h4>
<p>You can create USB drive config to replicate settings from 1 device to another (include WiFi, OptiSigns app, time zone, etc.) this will save you time if you have many devices to set up.</p>
<p>Enter the settings menu (the config wheel icon on the remote)<br>Insert a USB drive into your device <br>Navigate to ‘Ez Setting’ -&gt; ‘Setting Data Cloning’ <br>On the first device push ‘Export Setting Data’ <br>On the other devices push ‘Import Setting Data’</p>
<p> </p>
<p>If you have questions or need additional help, please contact us at <a href="mailto:support@optisigns.com">support@optisigns.com.</a></p>