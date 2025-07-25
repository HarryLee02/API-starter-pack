<h3 id="h_01JRAVR1WQVP3AEF6Z2C6T8PNP"><span style="color: #434343;">In this article, we will troubleshoot the most common issues people encounter using our OptiSigns Android Player.</span></h3>
<ul>
<li><a href="#Identify">Identify Your Device</a></li>
<li><a href="#BestPractices">Best Practices</a></li>
<li><a href="#Troubleshooting">The Troubleshooting Option</a></li>
<li>
<a href="#Hardware">Hardware Troubleshooting</a>
<ul>
<li><a href="#Network">Network Troubleshooting</a></li>
<li><a href="#Power">Power Troubleshooting</a></li>
<li><a href="#HDMI">HDMI &amp; TV Connection Troubleshooting</a></li>
<li><a href="#RemoteControl">Remote Control Troubleshooting</a></li>
<li><a href="#TimeZone">Changing Device Time Zone</a></li>
<li><a href="#BlankScreen">Blank Screen Troubleshooting</a></li>
<li><a href="#FactoryReset">How to Factory Reset the OptiSigns Android Player</a></li>
</ul>
</li>
<li>
<a href="#ContentPlayback">Content Playback Troubleshooting</a>
<ul>
<li><a href="#WebsiteDisplay">Website display or sizing issues</a></li>
<li><a href="#DesignerSizing">Designer or template sizing issues</a></li>
<li><a href="#ScreenColor">Screen color distortion</a></li>
<li><a href="#OnHold">Fixing the OnHold warning</a></li>
<li><a href="#AppCrashing">App crashing</a></li>
</ul>
</li>
<li><a href="#RMA">Android Player RMA Process</a></li>
</ul>
<p>If you’ve got an OptiSigns Android Player and you’re having issues, you’ve come to the right place. For first time setup, see our article on how to <a href="https://support.optisigns.com/hc/en-us/articles/27267311796243-OptiSigns-Android-Digital-Signage-Player" target="_blank" rel="noopener noreferrer"><strong>Set Up the Android Digital Signage Player</strong></a>.</p>
<hr>
<p><a name="Identify"></a></p>
<h2 id="h_01JRAVR1WQ439KRE719XTTXB3W">Identify Your Device</h2>
<p>There have been several versions of the OptiSigns Android Stick over the years. The most common are the Gen 2 and Gen 3 devices:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40147900608403" alt="android player comparison gen2 vs gen3" width="624" height="416"></p>
<p>Functionally, these are quite similar. Both use the latest versions of the OptiSigns software. Most of their differences lie in <strong><a href="#Network">Networking</a>.</strong></p>
<hr>
<p><a name="BestPractices"></a></p>
<h2 id="h_01JRAVR1WQPPND9B7GF38RAAKB">Best Practices</h2>
<p>We recommend certain best practices to keep your OptiSigns Android Player running at peak efficiency:</p>
<ul>
<li>Do not put too much pressure on the power cable, as this can cause the Player to get pulled from its HDMI socket.</li>
<li>Keep the player in an indoor, air conditioned environment</li>
<li>Run the Android Stick in fullscreen mode, or with a 2-3 zone Split Screen.</li>
</ul>
<p>By default, an Android Player has an <a href="https://support.optisigns.com/hc/en-us/articles/28598173096723-How-To-Create-and-Use-Operational-Schedules-HDMI-CEC-RS-232" target="_blank" rel="noopener noreferrer"><strong>Operational Schedule </strong></a>built in to ensure it has 8 hours of downtime per day:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40147917435923" alt="operational schedule image" width="624" height="125"></p>
<p>If you require 24/7 uptime, more than 3 zones on a split screen, a heavy Website Dashboard (including Tableau or Power BI reports), or plan to use the player in hot or cold environments, consider the <a href="https://shop.optisigns.com/products/optisigns-digital-signage-player"><strong><span class="wysiwyg-underline" style="color: #1155cc;">OptiSigns Pro Player</span></strong></a> or <a href="https://shop.optisigns.com/products/optisigns-promax-signage-player" target="_blank" rel="noopener noreferrer"><strong><span class="wysiwyg-underline">ProMax Player</span></strong></a>.</p>
<hr>
<p><a name="Troubleshooting"></a></p>
<h2 id="h_01JRAVR1WQSX04T2Q9DFRM445A">The Troubleshooting Page</h2>
<p>Your first stop when running into a problem with the OptiSigns Android Player should be the <strong>Troubleshooting Page. </strong>This is an option on the side menu.</p>
<p>To access it, press the <strong>Three-Bar button</strong> on your remote to open the side menu of the OptiSigns app. Navigate to <strong>Troubleshooting </strong>under the <strong>Advanced Options </strong>section.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40147917438355" alt="open troubleshooting page optisigns app" width="624" height="351"></p>
<p>Now you can view detailed information about the app’s status and connectivity to assist with troubleshooting.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40147917440787" alt="troubleshooting page optisigns" width="624" height="349"></p>
<ul>
<li>
<strong>Check Internet Connection</strong>: Verifies whether the device has an active internet connection.</li>
<li>
<strong>Check Connection to API Services</strong>: Tests the device's connection to OptiSigns services.
<ul>
<li>
<strong>Note</strong>: If this check fails, it may be due to a firewall blocking the connection. Refer to our<a href="https://support.optisigns.com/hc/en-us/articles/360047275934"> <strong><span class="wysiwyg-underline" style="color: #1155cc;">Whitelist Article</span></strong></a><span class="wysiwyg-underline" style="color: #1155cc;"> </span>for the required URLs and ports.</li>
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
<strong>System Time</strong>: Shows the current system time on the device.</li>
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
<strong>Heavy Content Status</strong>: Indicates whether the device is handling heavy content (e.g., 4+ zones or SplitScreen with 4K video) (<strong>Y/N</strong>). This will usually result in lag.</li>
</ul>
<hr>
<p><a name="Hardware"></a></p>
<h2 id="h_01JRAVR1WQSACPEXBZ17V9MCZ0">Hardware Troubleshooting</h2>
<p>Here we will cover the most common hardware troubleshooting issues our support team encounters.</p>
<p><a name="Network"></a></p>
<h3 id="h_01JRAVR1WQSSNFB90MH2BT9YG9"><span style="color: #434343;">Network Troubleshooting</span></h3>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td class="wysiwyg-text-align-center" style="width: 50%;"><strong>GEN 2</strong></td>
<td class="wysiwyg-text-align-center" style="width: 50%;"><strong>GEN 3</strong></td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" style="width: 50%;">2.4 GHz WiFi only</td>
<td class="wysiwyg-text-align-center" style="width: 50%;">2.4 GHz and 5 GHz WiFi</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" style="width: 50%;">WiFi 5 and below</td>
<td class="wysiwyg-text-align-center" style="width: 50%;">WiFi 5 and below</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" style="width: 50%;">No Ethernet</td>
<td class="wysiwyg-text-align-center" style="width: 50%;">Ethernet Capable</td>
</tr>
</tbody>
</table>
<p>To identify and resolve network issues:</p>
<ul>
<li>Create a mobile hotspot, then have your Android Player connect with it. A successful connection indicates a problem with your general Wi-Fi connection.</li>
<li>Try a different network. You may need to move the device to get connected. A successful connection indicates a problem with your general Wi-Fi connection.</li>
<li>Plug in an Ethernet cable to see if it can still connect.</li>
</ul>
<p>To see what network you’re connected to, go to the Side Menu and hit <strong>Exit</strong>. This will close the OptiSigns app.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40147917441555" alt="exit optisigns app"></p>
<p>Next, open the menu on the side using the remote. If connected to a network, it should appear here. If not, you'll need to set that back up.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40147900613907" alt="access network optisigns player"></p>
<p><a name="Power"></a></p>
<h3 id="h_01JRAVR1WQQJ27RPWY4KR6SBB2"><span style="color: #434343;">Power Troubleshooting</span></h3>
<p>One of the most common causes of device instability is not using the provided power adapters and cables.</p>
<p>If your device has any sort of intermittent power issues, <strong><em>please ensure it is not being powered by the USB port on your screen</em></strong>. The USB port does not provide enough power to the device to keep it running under all conditions.</p>
<p>In the event there is no available power outlet nearby and the USB port is your only option, keep your content load light - meaning, no videos, no large files, etc.</p>
<p><a name="HDMI"></a></p>
<h3 id="h_01JRAVR1WRCHK2PGPJGVF0WJ4P"><span style="color: #434343;">HDMI &amp; TV Connection Troubleshooting</span></h3>
<p>If you’re having problems connecting your Android Player to your HDMI port or TV, here are some steps to try:</p>
<ul>
<li>Try a different HDMI port on your screen</li>
<li>Try to connect the Android Player directly to your TV without the HDMI extended</li>
<li>Try a different TV or monitor to see if it will work at all</li>
</ul>
<p>If none of these work, contact our support team at <a href="mailto:support@optisigns.com"><span class="wysiwyg-underline" style="color: #1155cc;">support@optisigns.com</span></a>. </p>
<p><a name="RemoteControl"></a></p>
<h3 id="h_01JRAVR1WRS3E7MGAWRQYA8SND"><span style="color: #434343;">Remote Control Troubleshooting</span></h3>
<p>The OptiSigns Android Player ships with a Remote Control. Which remote control you have depends on the version of your player, but they largely function the same with a few slight differences.</p>
<p><strong>Gen 3 Remote:</strong></p>
<p><strong><img src="https://support.optisigns.com/hc/article_attachments/40147917443347" alt="gen 3 remote control" width="624" height="540"></strong></p>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td class="wysiwyg-text-align-center" style="width: 100%;"><strong>NOTE</strong></td>
</tr>
<tr>
<td style="width: 100%;">To pair or re-pair this remote, hold the <strong>Back </strong>and <strong>Home </strong>buttons.</td>
</tr>
</tbody>
</table>
<p><strong>Gen 2 Remote:</strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40147900615827" alt="gen 2 remote control" width="443" height="465"></p>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td class="wysiwyg-text-align-center" style="width: 100%;"><strong>NOTE</strong></td>
</tr>
<tr>
<td style="width: 100%;">To pair or re-pair this remote, hold the <strong>Return </strong>and <strong>OK </strong>buttons.</td>
</tr>
</tbody>
</table>
<p>OptiSigns Players also support the <a href="https://support.optisigns.com/hc/en-us/articles/30003143806099-How-to-Use-the-OptiSigns-Mobile-Admin-App"><strong><span class="wysiwyg-underline" style="color: #1155cc;">Mobile Admin App</span></strong></a> as a Remote Control. This is our <strong><em>top recommendation,</em></strong> as not only does it function as a true remote control (allowing you to control your players from anywhere), but it has numerous other features as well.</p>
<p>If your remote control is having issues:</p>
<ul>
<li>Ensure batteries have been installed inside your remote control, and that they are not dead</li>
<li>Re-pair your remote control with the player</li>
<li>Try a plug-in USB keyboard or mouse</li>
<li>Use the Mobile Admin app to set up Wi-Fi, or as a remote control itself</li>
</ul>
<p><a name="BlankScreen"></a></p>
<h3 id="h_01JRAVR1WR9QWBCXJ1RYP919N5"><span style="color: #434343;">Blank Screen Troubleshooting</span></h3>
<p>If your device and screen are on, but only displays a black screen:</p>
<ul>
<li>Network issues, <a href="#Network"><strong>see above</strong></a>.</li>
<li>Check to make sure there is a Playlist or Asset assigned to your screen.</li>
<li>Make sure your Timezones and Schedules match, including your Operational Schedule and normal schedule.</li>
<li>Check your firewall settings, and ensure you’ve <a href="https://support.optisigns.com/hc/en-us/articles/360047275934-Whitelist-OptiSigns-IP-addresses-ports"><strong><span class="wysiwyg-underline" style="color: #1155cc;">Whitelisted OptiSigns IP addresses and ports</span></strong></a>.</li>
<li>Check your Operational Schedule, and verify its power settings are not set to Off. If an Operation Schedule’s power settings are set to Off, it will remain off during the designed time.</li>
</ul>
<p>If the device is still not displaying content after you’ve checked these, check our <a href="#ContentPlayback"><strong>Content Playback Troubleshooting </strong></a>section, then try a <strong>Factory Reset</strong>.</p>
<p><a name="TimeZone"></a></p>
<h3 id="h_01JVWBPMRT08FCV0JKHEYBQ0YM">Changing Device Time Zone</h3>
<p>When <strong><a href="https://support.optisigns.com/hc/en-us/articles/360016981853-Create-and-Using-Schedules-with-OptiSigns" target="_blank" rel="noopener noreferrer">setting a schedule</a></strong>, it's critical that the portal and device share the same time zone. If the time zones are not identical, it can cause your schedule to start at a different time than you'd like. The issue is usually the device's time zone.</p>
<p>To do this, you'll need to change it. Start by pressing the <strong>Home button </strong>on your remote (or hit <strong>Exit App </strong>from the Side Menu), and navigate to the <strong>Settings</strong> menu.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/41497198237971" alt="settings menu"></p>
<p>Select <strong>Device Preferences</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/41497175224851" alt="device preferences option android side menu"></p>
<p>Select <strong>Date &amp; Time</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/41497198242323" alt="date &amp; time option android side menu"></p>
<p>Select <strong>Set time zone</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/41497198243347" alt="select time zone option android side menu"></p>
<p>For some reason, Android devices lead with Midway Island, in the middle of the Pacific (some things in life are best left a mystery). Navigate to your preferred time zone and select it.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/41497198244627" alt="time zone options android"></p>
<p>Now your device and schedule should sync properly.</p>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td class="wysiwyg-text-align-center" style="width: 100%;"><strong>NOTE</strong></td>
</tr>
<tr>
<td style="width: 100%;">These steps can be performed remotely using the <strong>Mobile Admin App </strong>or through <strong>MDM Commands</strong>.</td>
</tr>
</tbody>
</table>
<p><a name="FactoryReset"></a></p>
<h3 id="h_01JRAVR1WR9YNJGWJ6980946P4"><span style="color: #434343;">How to Factory Reset the OptiSigns Android Player</span></h3>
<p>You can factory reset your Android Player if the system is not functioning properly or the Android system will not load.</p>
<p>There are two ways to do a factory reset.</p>
<h4 id="h_01JRAVR1WRNB2NM22FCDHB3A5K"><span style="color: #666666;">Soft Reset</span></h4>
<p>A soft reset can be performed if the system is still accessible and operational. This will erase all the data on the device, and may help improve performance and fix some issues.</p>
<p>On the Home screen, go to <strong>Settings</strong>. Hit <strong>Device Preferences, </strong>then choose <strong>About</strong>. Finally, choose <strong>Factory Reset.</strong> </p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40147900617363" alt="factory reset settings" width="624" height="351"></p>
<p>It will ask if you’re sure you’d like to perform this function. If you are, hit <strong>OK</strong>. The soft factory reset will take place.</p>
<h4 id="h_01JRAVR1WRQ20J5YT3PN92KQJR"><span style="color: #666666;">Hard Reset</span></h4>
<p>When certain Android system files are corrupted, the device will not be able to boot into the Android system. In this case, you will need to perform a hard reset.</p>
<p>To perform one, you’ll need a small tool. Think paperclip, needle, or SIM card pin. Then, ensure the device is completely powered off and the USB power cable is unplugged from the device.</p>
<p>Next, use your small tool to press into the small hole on the side of the device. Hold it, then plug in the power cable while the tool is still pressing the button in the small hole.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40147900618259" alt="optisigns gen 3 player hard reset hole" width="624" height="389"></p>
<p>The system will then boot into recovery mode. You can use the button to navigate between selections and will need to press and hold for 1-2 secs to confirm selection. Choose <strong>wipe data/factory reset</strong>, and the factory reset will start.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40147900620563" alt="boot mode wipe data option" width="624" height="351"></p>
<p>Then choose <strong>Factory data reset:</strong></p>
<p><strong><img src="https://support.optisigns.com/hc/article_attachments/40147917447443" alt="boot mode factory data reset option" width="624" height="351"></strong></p>
<p>Once the process is complete, you’ll see a <strong>Data Wipe Complete </strong>message at the bottom of the screen. From there, select <strong>Reboot System Now </strong>to finish.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40147917449235" alt="boot mode reboot system now option" width="624" height="351"></p>
<p>Your Android Stick will be fully factory reset.</p>
<hr>
<p><a name="ContentPlayback"></a></p>
<h2 id="h_01JRAVR1WRGZNZXAP2BDMHXVDZ">Content Playback Troubleshooting</h2>
<p>This section deals with common issues we see when trying to display content using an Android Player.</p>
<p><a name="WebsiteDisplay"></a></p>
<h3 id="h_01JRAVR1WR6DMBA7M5T6N06V83"><span style="color: #434343;">Website Display or Sizing Issues</span></h3>
<p>To display a website as you would see it on a Desktop or PC, change Device Scaling to smallest.</p>
<p>For more information, see the relevant article on Device Scaling:</p>
<ul>
<li><a href="https://support.optisigns.com/hc/en-us/articles/28026588373139-How-to-Fix-The-Scaling-Issue-on-OptiSigns-Android-Device-Gen-3" target="_blank" rel="noopener noreferrer"><strong>Gen 3 Device Scaling</strong></a></li>
<li><a href="https://support.optisigns.com/hc/en-us/articles/27607906766483-How-to-Fix-The-Scaling-Issue-on-OptiSigns-Android-Device" target="_blank" rel="noopener noreferrer"><strong>Gen 2 Device Scaling</strong></a></li>
</ul>
<p><a name="DesignerSizing"></a></p>
<h3 id="h_01JRAVR1WRNHP544ZN4XWKT6TJ"><span style="color: #434343;">Designer or Template Sizing Issues</span></h3>
<p>If using the <a href="https://support.optisigns.com/hc/en-us/articles/4404151402899-How-to-use-OptiSigns-Template-Designer-app-to-make-your-Digital-Signs-in-minutes"><strong><span class="wysiwyg-underline" style="color: #1155cc;">Designer app</span></strong></a><strong>, </strong>try setting the canvas size to 960x540, or change the display size on Android.</p>
<p><a name="ScreenColor"></a></p>
<h3 id="h_01JRAVR1WRR1AQ3W4DSZDS4Z53"><span style="color: #434343;">Screen Color Distortion</span></h3>
<p>If your screen is showing distorted colors or displays, try:</p>
<ul>
<li>A different HDMI cable, port, or screen</li>
<li>Turning off everything transmitting data between the screen and Android stick, such as the HDMI-CEC, Dolby Vision, or auto adapting resolution</li>
</ul>
<p><a name="OnHold"></a></p>
<h3 id="h_01JRAVR1WR6RJ62VBBF60F46BP"><span style="color: #434343;">Fixing the OnHold Warning</span></h3>
<p><img src="https://support.optisigns.com/hc/article_attachments/40147900625555" alt="device is onhold message" width="624" height="144"></p>
<p>This warning displays when the device is in the <a href="https://support.optisigns.com/hc/en-us/articles/1500003244381-About-the-OnHold-Devices-Folder"><strong><span class="wysiwyg-underline" style="color: #1155cc;">OnHold Folder</span></strong></a>. This happens when you’ve ordered more devices than you had licenses for. Any devices above your license limit will automatically be placed in the OnHold folder and will need to be removed, even when the license limit has been raised.</p>
<p><a name="AppCrashing"></a></p>
<h3 id="h_01JRAVR1WRDXN8WSP7Y6TSAEW8"><span style="color: #434343;">App Crashing</span></h3>
<p>To handle crashes, clear the cache and then data of the OptiSigns Player, then reboot. You may need to Factory Reset.</p>
<p>App crashes are most common when is kept on for extremely long periods of time. To avoid them, schedule a <strong>Restart Timer</strong>.</p>
<hr>
<p><a name="RMA"></a></p>
<h2 id="h_01JRAVR1WRQ4FAEFSFM8KYKPZS">Android Player RMA Process</h2>
<p>If none of the solutions here work, feel free to submit an RMA request. Devices will be tested as part of the RMA process, and if they are working correctly, you (the customer) will be charged a restocking fee.</p>
<p>Here are the steps for an RMA:</p>
<ol>
<li>Obtain a proof of purchase stating that your device was purchased within the last 12 months, complying with our 12-month warranty policy.</li>
<li>Fill out <a href="https://share.hsforms.com/14BvoeL1JRlGgxr3ec_kdJgca5m5"><strong><span class="wysiwyg-underline" style="color: #1155cc;">this RMA request form</span></strong></a>.</li>
<li>RMA requests are reviewed within 3 business days.</li>
<li>New devices arrive within 3-5 business days to most places in the United States.</li>
<li>Return the old device within 30 days.</li>
</ol>
<h3 id="6-that-s-all-">That's all!</h3>
<p>If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self">support@optisigns.com</a>.</p>