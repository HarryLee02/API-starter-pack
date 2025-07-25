<h3 id="h_01JD2EMNGR8ATQF9P52MF81HYZ"><span style="color: #434343;">In this article, we go over the Advanced Features of the new Gen 3 OptiSigns Pro Player.</span></h3>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td class="wysiwyg-text-align-center" style="width: 100%;"><strong>IMPORTANT</strong></td>
</tr>
<tr>
<td style="width: 100%;">This article applies strictly to the <em>OptiSigns Gen 3 Pro Player or ProMax Player </em>on version <strong>5.6.33</strong> or later.</td>
</tr>
</tbody>
</table>
<ul>
<li>
<a href="#OTA">OTA Updates</a>
<ul>
<li><a href="#ForceOTA">Forcing an OTA Update</a></li>
</ul>
</li>
<li>
<a href="#About">The "About" Option</a>
<ul>
<li><a href="#Log">Device Log</a></li>
<li><a href="#AdvancedSettings">Advanced Settings</a></li>
</ul>
</li>
<li><a href="#name">How to Bring Up the System Terminal</a></li>
<li><a href="#ssh">How to Use SSH to Remote into Device</a></li>
<li><a href="#FactoryReset">How to Perform a Factory Reset</a></li>
</ul>
<p>The <a href="https://shop.optisigns.com/collections/shop-page/products/optisigns-digital-signage-player"><span style="color: #1155cc;"><strong>OptiSigns Pro Digital Signage Player</strong></span></a> or <strong><a href="https://shop.optisigns.com/products/optisigns-promax-signage-player" target="_blank" rel="noopener noreferrer">OptiSigns ProMax Player</a></strong> are mighty devices, able to leverage the full power of OptiSigns <strong><a href="https://www.optisigns.com/"><span style="color: #1155cc;">digital signage software</span></a></strong> to display your content on any screen with unparalleled visual clarity and customizability.</p>
<p>But there’s even more to the <strong><a href="https://support.optisigns.com/hc/en-us/articles/32272215514131-Optisigns-Pro-Digital-Signage-Player"><span style="color: #1155cc;">Pro Player than its standard features</span></a></strong>, and here we’ll explain the device’s Advanced features.</p>
<div>
<table style="width: 100%;">
<colgroup> <col> </colgroup>
<tbody>
<tr>
<td style="text-align: center;"><strong>NOTE</strong></td>
</tr>
<tr>
<td>If you do not see all the options listed below, we recommend performing an <strong>OTA Update</strong> to ensure you have the latest version of the Pro Player software. This is covered later in the article.</td>
</tr>
</tbody>
</table>
</div>
<hr>
<p><a name="OTA"></a></p>
<h2 id="h_01JD2EMNGREEZ49Q8RHNG7MJ4T">OTA Updates</h2>
<p>The OptiSigns Pro Player makes use of OTA updates to receive security patches, platform enhancements, additional feature support, and more.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35577511371795" width="334" height="189"></p>
<p>By default, the Pro Player can be set to check for updates once per week at a time you specify. If update is available, it will be automatically downloaded as long as the player has an internet connection. It’s also possible to force an OTA update if necessary.</p>
<p><a name="ForceOTA"></a></p>
<h3 id="h_01JD2EMNGRD3Y5EQ1R8VR4XKE3"><span style="color: #434343;">How to Force an OTA Update</span></h3>
<p>If your device misses its update window, either due to being powered off, or lacking reliable network connection, it is possible to check for an OTA update to the OptiSigns Pro Player and apply it.</p>
<p>In order to do this, you’ll need access to the OptiSigns Portal. From the <strong>Screens tab</strong>, click the <strong>3 Dots</strong> <strong>→ Execute Remote Commands</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35577511373587" width="619" height="133"></p>
<p>You’ll be taken to the below screen:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35577555668755" width="624" height="204"></p>
<p>Target the screen you’ve paired with your OptiSigns Pro Player, then enter the <strong>forceOTA </strong>command in the highlighted field. After a few seconds, you should see the following:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35577511382803" width="624" height="103"></p>
<p>This means the OptiSigns Pro Player has received the command and executed it. It should now be receiving its update.</p>
<div>
<table style="width: 100%;">
<colgroup> <col> </colgroup>
<tbody>
<tr>
<td>
<strong>NOTE: </strong>In order for your OptiSigns Pro Player to receive commands, it will need to be connected to the Internet.</td>
</tr>
</tbody>
</table>
</div>
<hr>
<p><a name="About"></a></p>
<h2 id="h_01JD2EMNGRJDX4GN5V2FW4GWYH">The ‘About’ Option</h2>
<p>The <strong>About</strong> option provides data on your Pro Player, in addition to different options.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35577555680659" width="495" height="331"></p>
<p>This lets you know everything from the name attached to your screen, to whether the Player is connected to the internet, to the storage used.</p>
<p>It also provides further options.</p>
<ul>
<li>
<strong>Reboot </strong>does what it says. It will reboot your device.</li>
<li>
<strong>Device Log</strong> allows you to export your device log. More detail is provided below.</li>
<li>
<strong>WiFi Setup </strong>lets you tweak the WiFi settings of the device. This is done the same way as on the device’s initial setup.</li>
<li>
<strong>Advanced Settings </strong>provide additional network options. More detail is provided below.</li>
</ul>
<p><a name="Log"></a></p>
<h3 id="h_01JD2EMNGRY0BQA8TXCHAJD4KS"><span style="color: #434343;">Device Log</span></h3>
<p>The device log option allows you to export the device log into an external device. In order to use this option, you’ll need a USB drive or MicroSD card plugged into your Pro Player. When you hit the <strong>Device Log </strong>option with an external drive plugged in, you’ll see the following message:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35577555683603" width="346" height="67"></p>
<p>You can then take your external device and do whatever you like with the device log.</p>
<p><a name="AdvancedSettings"></a></p>
<h3 id="h_01JD2EMNGRSGFK6S1XN7EZ5RVF"><span style="color: #434343;">Advanced Settings</span></h3>
<p><img src="https://support.optisigns.com/hc/article_attachments/40595153623187" alt="WIN_20250423_09_51_19_Pro - Copy (2).jpg"></p>
<p>On the<strong> Advanced Settings </strong>screen, you can perform various functions such as enabling/disabling Network Proxy, NTP, the On-screen Keyboard, SSH, and configuring a Static IP for either WLAN or Ethernet. Selecting any of these options will enable further options in the window:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40595153623955" alt="WIN_20250423_09_51_19_Pro - Copy.jpg"></p>
<ul>
<li>
<span class="wysiwyg-underline"><strong>Certificate File</strong></span> <strong>-</strong> Allows you to <a href="https://support.optisigns.com/hc/en-us/articles/35184720136595-How-to-Install-a-Root-Certificate-and-Display-an-Internal-Website-on-Screens" target="_blank" rel="noopener noreferrer">install a root certificate</a> for displaying an internal website. The certificate will need to be present locally on the device in order for it to be installed.<span class="wysiwyg-underline"></span>
</li>
<li>
<span class="wysiwyg-underline"><strong>NTP Server</strong></span><strong> - </strong>Input server information for your Network Time Protocol (NTP). This can be used to ensure the OptiSigns Pro Player has its computer clock time with other time sources in your network.<span class="wysiwyg-underline"></span>
</li>
<li>
<span class="wysiwyg-underline"><strong>WiFi SSH IP</strong></span> - IP address associated with your SSH. Only appears when SSH is enabled.</li>
<li>
<span class="wysiwyg-underline"><strong>Network Proxy</strong></span><strong> -</strong> Server information for any network proxy. This is a system or router which serves as a middleman between our Pro Player and the internet and can be used to enhance security, privacy, or efficiency.</li>
<li>
<span class="wysiwyg-underline"><strong>KeyBoard Layout</strong></span><strong> - </strong>Choose between various international keyboard layouts. Default is US.</li>
<li>
<span class="wysiwyg-underline"><strong>Static IP Information</strong></span><strong> - </strong>An IP address that remains the same over time. We allow two types of Static IP: WLAN or ETH. These can improve network performance. This screenshot shows WLAN; if Static ETH IP is chosen, these will be ETH IP Address, Default Gateway, Subnet Mask, and DNS Server.
<ul>
<li>
<strong>IP Address - </strong>Set the Static IP address.</li>
<li>
<strong>Default Gateway </strong>- Set the Default Gateway for the Static IP address. This is the IP address of your router.</li>
<li>
<strong>Subnet Mask </strong>- Set the Subnet Mask for the Static IP. Usually, this number is 255.255.255.0 or some variant of this.</li>
<li>
<strong>DNS Server </strong>- Lets you set up your DNS server for the Static IP address.</li>
</ul>
</li>
</ul>
<hr>
<p><a name="name"></a></p>
<h2 id="h_01JD2EMNGSM4W7MNQKMEHYYMDG">How to Bring Up the System Terminal</h2>
<p>The OptiSigns Pro Player has a console you can use to input commands directly. This can be accessed through the OptiSigns portal. From the <strong>Screens tab</strong>, click the <strong>3 Dots</strong> <strong>→ Execute Remote Commands</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35577555693075" width="619" height="133"></p>
<p>You’ll be taken to the below screen:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35577555668755" width="624" height="204"></p>
<p>Target the screen you’ve paired with your OptiSigns Pro Player, then enter the <strong>showTerminal </strong>command in the highlighted field. After a few seconds, you should see the following:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35577511404819" width="583" height="167"></p>
<p>This means the OptiSigns Pro Player has received the command and executed it. Your console terminal should now be visible on your screen and can be interacted with.</p>
<hr>
<p><a name="ssh"></a></p>
<h2 id="h_01JTK1PNC9M218TS7YNW94A80M">How to Use SSH to Remote Into Device</h2>
<p>Pro Players allow remoting into devices using SSH. Here's how to set that up.</p>
<p>First, enable <strong>SSH </strong>in your Advanced Settings.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40985616289939" alt="ssh advanced settings"></p>
<p>This will provide you with the SSH IP and Port number. By default, the port is <strong>3000</strong>, but it can be changed to whatever you like.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/40985596548243" alt="ssh ip and port"></p>
<p>Now that SSH is enabled and you have the IP and Port, you can use a computer terminal to remote into the device.</p>
<p>Type the following command:</p>
<pre>SSH <a href="mailto:optisigns@&lt;ip-address-here&gt;">optisigns@&lt;ip-address-here&gt;</a> -p &lt;port-number-here&gt;</pre>
<p>When it asks for a password, type <strong>optisigns</strong>. This should connect you to the device via SSH.</p>
<p>To change the default password (which we <em><strong>highly </strong></em><em><strong>recommend</strong></em>), type:</p>
<pre>passwd</pre>
<p>This will ask you to type the current password, then new, then to type in the new password again.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/41021980486931"></p>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td class="wysiwyg-text-align-center" style="width: 100%;"><strong>NOTE</strong></td>
</tr>
<tr>
<td style="width: 100%;">Restarting the OptiSigns Pro Player will cause SSH to automatically disable for security purposes.</td>
</tr>
</tbody>
</table>
<p>That's it! You should be able to use the SSH function now.</p>
<hr>
<p><a name="FactoryReset"></a></p>
<h2 id="h_01JD2EMNGSHEN0CY7D75B6AEAY">How to Perform a Factory Reset</h2>
<p>Sometimes, it might be necessary to perform a factory reset on your OptiSigns Pro Player.</p>
<p>To do this, attach a keyboard to the Player. Then, <strong>Reboot </strong>it. As it restarts, rapidly tap the <strong>↑ arrow</strong>. It will boot into this screen:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35577555703187" width="624" height="351"></p>
<p>Here, you have several additional options. Hit <strong>Factory Reset</strong>. You’ll receive this prompt:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35577555704723" width="624" height="352"></p>
<p>You’ll need to enter your <strong>admin password.</strong></p>
<p>Once entered, you’ll see a screen like this:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35577555707923" width="624" height="349"></p>
<p>Afterwards, your factory defaults will be restored.</p>
<h3 id="h_01JD2EMNGS9T2AZF2ZY26SV2XP"><strong><span style="color: #434343;">That’s all!</span></strong></h3>
<p>OptiSigns is a leader in<a href="https://www.optisigns.com/"> <span class="wysiwyg-underline" style="color: #1155cc;">digital signage software</span></a>. If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com"><span class="wysiwyg-underline" style="color: #1155cc;">support@optisigns.com</span></a>.</p>