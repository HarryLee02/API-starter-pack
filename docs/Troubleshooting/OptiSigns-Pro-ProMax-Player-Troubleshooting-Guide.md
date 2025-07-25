<h3 id="h_01JSYGVM4M4WF26NYZ2D40TMWH">In this article, we troubleshoot the most common issues our customers face when using an OptiSigns Pro or ProMax Player.</h3>
<ul>
<li><a href="#BestPractices">Best Practices</a></li>
<li><a href="#TroubleshootingOption">The Troubleshooting Option</a></li>
<li>
<a href="#Hardware">Hardware Troubleshooting</a>
<ul>
<li><a href="#Network">Network Troubleshooting</a></li>
<li><a href="#Connection">Power, HDMI &amp; TV Connection Troubleshooting</a></li>
<li><a href="#BlankScreen">Blank Screen Troubleshooting</a></li>
<li><a href="#OnHold">Fixing the OnHold Warning</a></li>
<li><a href="#AppFreezes">App Freezes, Video Assets not Playing full video or Asset Not Loaded Fully</a></li>
<li><a href="#FactoryReset">How to Factory Reset the OptiSigns Android Player</a></li>
</ul>
</li>
<li>
<a href="#SecuritySettings">Security Settings Troubleshooting</a>
<ul>
<li><a href="#DeviceLog">Using the Device Log</a></li>
<li><a href="#StaticIP">Static IP</a></li>
<li><a href="#InternalWebsite">Internal Websites and Root Certificates</a></li>
</ul>
</li>
<li><a href="#RMAProcess">Pro/ProMax Player RMA Process</a></li>
</ul>
<p>If you’ve got an OptiSigns Pro or ProMax Player and you’re having issues, you’ve come to the right place. For first time setup, see our <a href="https://support.optisigns.com/hc/en-us/articles/32272215514131-Optisigns-Pro-Digital-Signage-Player" target="_blank" rel="noopener noreferrer"><strong>Set Up the OptiSigns Pro Player</strong></a> or <strong><a href="https://support.optisigns.com/hc/en-us/articles/38680194603155-OptiSigns-ProMax-Player" target="_blank" rel="noopener noreferrer">Set Up the OptiSigns ProMax Player</a></strong> articles. For more on the Pro or ProMax player features, see our <a href="https://support.optisigns.com/hc/en-us/articles/35577511423635-OptiSigns-Pro-Player-Advanced-Features" target="_blank" rel="noopener noreferrer"><strong>Advanced Features</strong></a> article.</p>
<hr>
<p><a name="BestPractices"></a></p>
<h2 id="h_01JSYGV354FB40T7EKRVH793YK">Best Practices</h2>
<ul>
<li>Set up the <a href="https://support.optisigns.com/hc/en-us/articles/30003143806099-How-to-Use-the-OptiSigns-Mobile-Admin-App" target="_blank" rel="noopener noreferrer"><strong>Mobile Admin App</strong></a>. This will allow you to use numerous features remotely, including the Remote Keyboard app and remote monitoring.</li>
<li>Keep the player in an indoor, air conditioned environment</li>
<li>Ensure your player is up-to-date. We release frequent OTA updates - see more below.</li>
</ul>
<p>By default, our Pro Players are set to receive a weekly automatic OTA update at <strong>Sunday 00:00</strong> (also known as Saturday night). If the players are offline at that time, it’s possible to miss the OTA update. We recommend changing the OTA update to a time when the players are online, but not being used for anything mission critical.</p>
<p>These OTA updates often bring with them new and advanced features, stability updates, security updates, patches, and more, so we <strong><em>highly recommend</em></strong> scheduling an update time that works for you. If none do, be sure to occasionally <strong>Check for Updates</strong>.</p>
<hr>
<p><a name="TroubleshootingOption"></a></p>
<h2 id="h_01JSYGV354TG9C1GTMK2N0M77P">The Troubleshooting Option</h2>
<p>Your first stop when running into a problem with the OptiSigns Pro or ProMax player should be the <strong>Troubleshooting </strong>page. This is an option on the Side Menu:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40736654908563" alt="troubleshooting page menu location" width="624" height="351"></p>
<p>Choosing this option will open the Troubleshooting screen:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40736654909587" alt="troubleshooting screen" width="624" height="351"></p>
<ul>
<li>
<strong>Check Internet Connection</strong>: Verifies whether the device has an active internet connection.</li>
<li>
<strong>Check Connection to API Services</strong>: Tests the device's connection to OptiSigns services, including APIs and MDMs.
<ul>
<li>
<strong>Note</strong>: If this check fails, it may be due to a firewall blocking the connection. Refer to our<strong><a href="https://support.optisigns.com/hc/en-us/articles/360047275934" target="_blank" rel="noopener noreferrer"> Whitelist Article</a></strong> for the required URLs and ports.</li>
</ul>
</li>
<li>
<strong>Check File Downloading</strong>: Confirms the status of downloadable files (e.g., images, videos) being downloaded to the device.</li>
<li>
<strong>Network Information</strong>: Displays the current network the device is connected to.
<ul>
<li>
<strong>WiFi/Ethernet Details</strong>: Includes IP Address, SSID, Signal Strength, Channel, Connection Type, and MAC Address.</li>
</ul>
</li>
<li>
<strong>Device Information:</strong>
<ul>
<li>Screen Name, Pairing Code, Screen Resolution, OptiSigns App Version, OptiSigns MDM App Version, OS Version, Manufacturer, Model, Serial Number</li>
<li>Heartbeat/Polling Interval: Indicates how frequently the device communicates with OptiSigns servers and the last received signal.</li>
</ul>
</li>
<li>
<strong>Running Time</strong>: Shows how long the OptiSigns app has been running on the device.</li>
<li>
<strong>Storage</strong>: Displays used and total storage capacity.</li>
<li>
<strong>Memory</strong>: Displays used and total memory capacity.</li>
<li>
<strong>Current System Time</strong>: Shows the current system time on the device.</li>
<li>
<strong>System Time Zone</strong>: Displays the time zone configured on the device.</li>
<li>
<strong>Assigned Content Type</strong>: Indicates the type of content the device is playing (e.g., Asset, Playlist, Schedule).</li>
<li>
<strong>Assigned Content Name</strong>: Provides the name of the content being displayed.</li>
<li>
<strong>Device Created Date</strong>: Displays the date the device was activated.</li>
<li>
<strong>Operational Schedule Assigned</strong>: Shows whether an operational schedule is assigned (<strong>Y/N</strong>).</li>
<li>
<strong>Mute Status</strong>: Displays the current audio status of the device.</li>
<li>
<strong>Heavy Content Status</strong>: Indicates whether the device is handling heavy content (e.g., 4+ zones or SplitScreen with 4K video) (<strong>Y/N</strong>) </li>
</ul>
<hr>
<p><a name="Hardware"></a></p>
<h2 id="h_01JSYGV354577FWCVFG355WVQS">Hardware Troubleshooting</h2>
<p>Here we will cover the most common hardware troubleshooting issues our support team encounters with our OptiSigns Pro and ProMax players. Following these steps will resolve 90%+ of issues.</p>
<p><a name="Network"></a></p>
<h3 id="h_01JSYGV3540D5J7WG3838XKPVZ"><span style="color: #434343;">Network Troubleshooting</span></h3>
<p>This is, by far, the most common issue people encounter. Devices experiencing network issues typically appear “Offline” in the OptiSigns portal, even when they are powered on and have content assigned to them.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40736654910739" alt="optisigns screen offline" width="435" height="79"></p>
<p>The first stop should be the <a href="#TroubleshootingOption"><strong>Troubleshooting Page</strong></a>. The upper left box details network status. If all the text is green, this means there are no network issues. Any red text will require further troubleshooting.</p>
<p>To identify and resolve network issues:</p>
<ul>
<li>Create a mobile hotspot, then have your Pro or ProMax player connect with it. A successful connection indicates a problem with your general Wi-Fi connection.</li>
<li>Try a different network. You may need to move the device to get connected. A successful connection indicates a problem with your general Wi-Fi connection.</li>
<li>If you have firewalls, make sure OptiSigns is whitelisted. Refer to our <strong><a href="https://support.optisigns.com/hc/en-us/articles/360047275934" target="_blank" rel="noopener noreferrer">Whitelist Article</a></strong> for the required URLs and ports.</li>
<li>Plug in an Ethernet cable to see if it can still connect.</li>
<li>After trying to connect with these methods, <a href="#FactoryReset"><strong>Factory Reset</strong></a> the device, then perform initial setup again.</li>
<li>If the device still cannot connect to any network, <strong><a href="https://support.optisigns.com/hc/en-us/articles/35626165056787-How-to-Contact-OptiSigns-Support" target="_blank" rel="noopener noreferrer">contact our support team</a></strong>. After a bit of troubleshooting, you may be asked to submit an <strong><a href="#RMAProcess">RMA request</a>.</strong>
</li>
</ul>
<p><a name="Connection"></a></p>
<h3 id="h_01JSYGV35450K011CR9PQGGFF4"><span style="color: #434343;">Power Cable, HDMI &amp; TV Connection Troubleshooting</span></h3>
<ul>
<li>Ensure device is powered on and the LED light on the power button is on</li>
<li>Try a different HDMI/DP port on your TV</li>
<li>Try a different TV or monitor</li>
</ul>
<p><a name="BlankScreen"></a></p>
<h3 id="h_01JSYGV354Q91867S33X8QAH8V"><span style="color: #434343;">Blank Screen Troubleshooting</span></h3>
<p>If your device and screen are on, but only displays a black screen:</p>
<ul>
<li>Network issues, <strong>see above</strong>.</li>
<li>Check to make sure there is a Playlist or Asset assigned to your screen.</li>
<li>Make sure your Timezones and Schedules match, including your Operational Schedule and normal schedule.</li>
<li>Check your firewall settings, and ensure you’ve <a href="https://support.optisigns.com/hc/en-us/articles/360047275934-Whitelist-OptiSigns-IP-addresses-ports" target="_blank" rel="noopener noreferrer"><strong>Whitelisted OptiSigns IP addresses and ports</strong></a>.</li>
<li>Check your Operational Schedule, and verify its power settings are not set to Off. If an Operation Schedule’s power settings are set to Off, it will remain off during the designed time.</li>
</ul>
<p>If the device is still not displaying content after you’ve checked these try a <a href="#FactoryReset"><strong>Factory Reset</strong></a>.</p>
<p><a name="OnHold"></a></p>
<h3 id="h_01JSYGV3544P00VC0DRQ3GZ0ZP"><span style="color: #434343;">Fixing the OnHold Warning</span></h3>
<p><img src="https://support.optisigns.com/hc/article_attachments/40736684864403" alt="OnHold warning" width="624" height="144"></p>
<p>This warning displays when the device is in the <a href="https://support.optisigns.com/hc/en-us/articles/1500003244381-About-the-OnHold-Devices-Folder" target="_blank" rel="noopener noreferrer"><strong>OnHold Folder</strong></a>. This happens when you’ve ordered more devices than you had licenses for. Any devices above your license limit will automatically be placed in the OnHold folder and will need to be removed, even when the license limit has been raised.</p>
<p><a name="AppFreezes"></a></p>
<h3 id="01JSYHVM8WSN67DNM3FZW3QA8C"><span style="color: #434343;">App Freezes, Video Assets not Playing full video or Asset Not Loaded Fully</span></h3>
<p>To handle any of these issues, hit the <strong>Refresh &amp; Relaunch </strong>option of the OptiSigns Player, then reboot. You may need to Factory Reset if the problem persists.</p>
<p><a name="FactoryReset"></a></p>
<h3 id="h_01JSYGV354PWKY310HCH13P4TR"><span style="color: #434343;">How to Factory Reset an OptiSigns Pro or ProMax Player</span></h3>
<p>Sometimes, it might be necessary to perform a factory reset on your OptiSigns Pro Player.</p>
<p>To do this, attach a keyboard to the Player. Then, <strong>Reboot </strong>it. As it restarts, rapidly tap the <strong>↑ arrow</strong>. It will boot into this screen:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40736654916499" alt="optisigns pro player boot screen" width="624" height="351"></p>
<p>Here, you have several additional options. Hit <strong>Factory Reset</strong>. You’ll receive this prompt:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40736654917395" alt="factory reset password screen" width="624" height="352"></p>
<p>You’ll need to enter your <strong>admin password. </strong>By default, this is <strong>root</strong>.</p>
<p>Once entered, you’ll see a screen like this:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40736684873363" alt="factory reset in progress" width="624" height="349"></p>
<p>Afterwards, your factory defaults will be restored.</p>
<hr>
<p><a name="SecuritySettings"></a></p>
<h2 id="h_01JSYGV354MXEVH7E8CW8DJT1H">Security Settings and Advanced Feature Troubleshooting</h2>
<p>The Pro and ProMax Players offer advanced security settings and features that are indispensable for an enterprise environment. Below are the most common and helpful suggestions we have when trying to enable some of these more advanced settings.</p>
<p>See our <strong><a href="https://support.optisigns.com/hc/en-us/articles/35577511423635-OptiSigns-Pro-Player-Advanced-Features" target="_blank" rel="noopener noreferrer">Pro/Pro Max Player Advanced Features</a></strong> article for information on setting these up.</p>
<p><a name="DeviceLog"></a></p>
<h3 id="h_01JSYGV354XG0GE6JC3A61Z7H8"><span style="color: #434343;">Using the Device Log</span></h3>
<p>There are two ways to use the <strong>Device Log </strong>feature:</p>
<ol>
<li>By plugging in an external device to the player, then hitting the <strong>Device Log </strong>button on the <strong>About </strong>menu. This will bring up a box letting you know the log has been exported to the external device:</li>
</ol>
<p><img src="https://support.optisigns.com/hc/article_attachments/40736654921235" alt="device log export confirmation" width="603" height="117"></p>
<ol start="2">
<li>By using the <strong><em>collectDeviceLog </em></strong><a href="https://support.optisigns.com/hc/en-us/articles/4408658251027-How-to-use-Remote-Command-Execution-Windows-Linux" target="_blank" rel="noopener noreferrer"><strong>Remote Command</strong></a> from the OptiSigns portal. This will provide a download link that you can use to obtain the log:</li>
</ol>
<p><img src="https://support.optisigns.com/hc/article_attachments/40736684875283" alt="execute remote command device log" width="624" height="373"></p>
<p>This can be extremely helpful for troubleshooting any issues that might have occurred when the device was not being closely monitored.</p>
<p><a name="StaticIP"></a></p>
<h3 id="h_01JSYGV354TNWEHPWHNZM4NG07"><span style="color: #434343;">Static IP</span></h3>
<p>When setting up a Static IP, make sure you’ve selected the appropriate static IP setting, depending on whether you’re using a WLAN or Ethernet connection.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40736684876691" alt="static IP wlanip vs ethip" width="342" height="313"></p>
<p>Next, ensure you’ve input the correct information in the IP Address, Default Gateway, Subnet Mask, and DNS Server fields.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40736654945427" alt="static ip options" width="345" height="542"></p>
<p>See our <strong><a href="https://support.optisigns.com/hc/en-us/articles/35577511423635-OptiSigns-Pro-Player-Advanced-Features" target="_blank" rel="noopener noreferrer">Advanced Settings for the Pro/ProMax Player</a></strong> article for more information.</p>
<p><a name="InternalWebsite"></a></p>
<h3 id="h_01JSYGV354EVK484QV8EGD5DCA"><span style="color: #434343;">Internal Website and Certificates</span></h3>
<p>For installation on a Gen 3 Pro or ProMax Player, your certificate must have a <strong>.crt </strong>extension. However, it is important that this certificate is signed and contains your public key. These are usually generated as <strong>.pem </strong>files. You’ll need to rename your certificate (.pem) file and change its extension to <strong>.crt </strong>for your internal website to properly display.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40736684879635" alt="certificate file option" width="345" height="542"></p>
<p>See our article on <strong><a href="https://support.optisigns.com/hc/en-us/articles/35184720136595-How-to-Install-a-Root-Certificate-and-Display-an-Internal-Website-on-Screens" target="_blank" rel="noopener noreferrer">how to install a root certificate and set up your internal website display</a></strong> for more information.</p>
<hr>
<p><a name="RMAProcess"></a></p>
<h2 id="h_01JSYGV354RXCR9NM4R8KBHG2Z">Pro/ProMax Player RMA Process</h2>
<p>Please try to go through the above common troubleshooting steps before submitting an RMA request.</p>
<p>Devices will be tested in the RMA process. If they work normally, the customer will be charged a restocking fee.</p>
<p>Our RMA process is as follows:</p>
<ul>
<li>Device is eligible for RMA only if it is still within the 12-month warranty period.</li>
<li>Fill out <strong><a href="https://share.hsforms.com/1cTorC26VQqGd-bF-zyzsTwca5m5" target="_blank" rel="noopener noreferrer">this RMA form</a></strong> (with proof of purchase in the last 12 months).</li>
<li>RMA request is reviewed within 3 business days.</li>
<li>New device ships within 3-5 business days to most places in the U.S.</li>
<li>Return the old device within 30 days.</li>
</ul>
<h3 id="19-that-s-all-">That's all!</h3>
<p>If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self">support@optisigns.com</a>.</p>