<div class="x_VfD">
<h3 id="h_01J96YT1XETC0WVM931X7N88E6" class="_zLbN _1szKo">In this article, we explain how to Mass Provision your devices for easy digital signage setup across numerous devices.</h3>
<ul>
<li>
<a href="#Setup">How to Set Up Mass Provisioning in the OptiSigns Portal</a>
<ul>
<li><a href="#Prerequisites">Prerequisites</a></li>
<li><a href="#Step1">Step 1: Create a Provisioning Template</a></li>
<li><a href="#Step2">Step 2: (Optional) Generate Device List</a></li>
</ul>
</li>
<li>
<a href="#Deployment">Deployment by Device</a>
<ul>
<li><a href="#OptiSigns">OptiSigns Digital Signage Players &amp; Windows/Linux Devices</a></li>
<li><a href="#Raspberry">Raspberry Pi Devices</a></li>
<li><a href="#AppleTV">Apple TV and ChromeOS</a></li>
</ul>
</li>
</ul>
<div class="_zLbN _1szKo">
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td style="width: 100%;">
<strong>NOTE: </strong>Mass Provisioning is only available to <strong>Enterprise</strong> plan subscribers.</td>
</tr>
</tbody>
</table>
</div>
<div class="_zLbN _1szKo"></div>
<div class="_zLbN _1szKo">Customers on the Enterprise Plan can now perform mass provisioning with OptiSigns. It is supported on OptiSigns Android Player, Windows, Linux, Raspberry Pi, ChromeOS, or AppleTV.</div>
<div class="_zLbN _1szKo"></div>
<div class="_zLbN _1szKo">If running a large deployment of digital signs, mass provisioning will save a lot of time and effort.</div>
<div class="_zLbN _1szKo"></div>
<div class="_zLbN _1szKo">For example, when you use our RPI image or have MDM software to display the OptiSigns player on a device, the mass provisioning feature lets you set up the device and get it connected to your account without having to set up each device individually.</div>
<hr>
<a name="Setup"></a>
<h2 id="h_01J96Z8T84K2AR9MYVFCSVA4S5" class="_zLbN _1szKo">How to Set Up Mass Provisioning in the OptiSigns Portal</h2>
<div class="_zLbN _1szKo">The process of performing mass provisioning is simple and straightforward.</div>
<ol>
<li class="_zLbN _1szKo">Create a provisioning template in your account.</li>
<li class="_zLbN _1szKo">(Optional) Generate a device list. Only needed if you wish to</li>
<li class="_zLbN _1szKo">Deploy and run.</li>
</ol>
<a name="Prerequisites"></a>
<h3 id="h_01J96ZC7256H9RYKWKA0AHA235" class="_zLbN _1szKo">Prerequisites:</h3>
<ul>
<li class="_zLbN _1szKo">The device needs to support using a USB drive or SD card. Or there is a way you can push the configuration file to a specific location in the OS.</li>
<li class="_zLbN _1szKo">The user using the OS has the privilege to run the installation and access the USB drive or SD card.</li>
</ul>
</div>
<div class="_3uWjK">
<div class="post-content__body">
<div class="_2FZkM">
<div class="kcuBq xGuFA blog-post-page-font TCKPQ uatYj _1Ss7I">
<div class="kaqlz _1PiV3 blog-post-page-font css-juod2b">
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">First time using OptiSigns? <a class="_2qJYG blog-link-hashtag-color _3sz0l" href="https://www.optisigns.com/blog/how-to-set-up-digital-signs-with-optisigns-and-amazon-fire-tv" target="_blank" rel="noopener noreferrer">Learn how to set up your digital signs</a> to get a better understanding before deployment.</p>
<a name="Step1"></a>
<h3 id="h_01HFD212FFK3D144ZNK3JJFVP6" class="_3f-vr _208Ie blog-post-title-font _3tzpp _5aNAR css-x4x4qs _2QAo- _25MYV _2R0Lu _2Dym_">Step 1: Create provisioning template</h3>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">To create a provisioning template, access it from the admin menu or use this <a href="https://app.optisigns.com/app/s/provisioning-templates" target="_blank" rel="noopener noreferrer">provisioning templates link</a>.</p>
<p class="undefined"><img src="https://support.optisigns.com/hc/article_attachments/34385117085715" alt="provisioning templates dropdown in optisigns app" width="371" height="415"></p>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td style="width: 100%;">
<strong>NOTE: </strong>This option will not be visible without an <strong>Enterprise </strong>level plan.</td>
</tr>
</tbody>
</table>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">Create a new provisioning template by clicking the <strong>Create templates</strong> button.</p>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_"><img src="https://support.optisigns.com/hc/article_attachments/34385123847827" alt="create templates button with arrow pointing at it in optisigns app"></p>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_"> If you want to auto-step up WiFi at provisioning, you will need to create a stored WiFi first. These steps are covered later.</p>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">For now, set up the template in this popup:</p>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_"><img src="https://support.optisigns.com/hc/article_attachments/4416555482899" alt="provisioning template options in optisigns"></p>
<ul>
<li class="rich-content-viewer_elementSpacing__208Ie">
<u>Template Name</u>: Name of your template, this is for you to distinguish it when you have multiple provisioning templates.</li>
<li>
<u>Device Name Prefix</u>: This is used to generate the device name during provisioning.</li>
<li>
<u>Device Name Suffix</u>: This is used to generate the device name during provisioning, the default setting will add timestamps as a suffix.</li>
<li>
<u>Folder:</u> The folder you want to have the provisioned devices to be created.</li>
<li>
<u>WiFi:</u> Select from the stored WiFi, which needs to be created first. Only required if you want to set up WIFI during provisioning.</li>
<li>
<u>Time Zone:</u> Specify the time zone of the device.</li>
<li>
<u>Tags:</u> Specify the tags you want to associate with the devices.</li>
<li>
<span class="wysiwyg-underline">Initial Default Content Type</span>: Used to set the initial content on the device after provisioning.</li>
<li>
<u>Orientation:</u> Set the orientation, landscape is the default.</li>
<li>
<u>Sync Play:</u> Used to set the turn on/off of the sync play feature. For more details on the Sync Play feature, please click <a href="https://support.optisigns.com/hc/en-us/articles/4412065189267-Synchronized-playback-Sync-Play-feature" target="_blank" rel="noopener noreferrer">here</a>.</li>
<li>
<u>Location:</u> Set the location of the device.</li>
</ul>
<p>Once the template is created, it will be available under the list of provisioning templates. Download the config file for use during deployment. The configuration file's name is "provisioning-template-&lt;Your Template Name&gt;.cfg"</p>
<div class="q2uC4 _2vlB-">
<div class="_2CvYQ c-Mgr _1K2V0 _1K2V0 _1hD8w">
<div class="_1Lhwj image-container"><img src="https://support.optisigns.com/hc/article_attachments/4416548298259" alt="provisioning templates screen with arrow pointing at file name button"></div>
<div class="_1Lhwj image-container">If you want to set up WiFi at the same time as provisioning, click the <strong>Manage Stored WiFi</strong> button.</div>
<div class="_1Lhwj image-container"></div>
<div class="_1Lhwj image-container">In the popup, click "Add New WiFi", then enter the WiFi SSID and password. The WiFi will be stored and available to use in the provisioning template.</div>
<div class="_1Lhwj image-container"><img src="https://support.optisigns.com/hc/article_attachments/4416570772627" alt="manage stored wifi screen with arrow pointing at add new wifi button"></div>
<div class="_1Lhwj image-container"> </div>
<div class="_1Lhwj image-container">
<a name="Step2"></a>
<h3 id="h_01HFD212FFNZW0RYA35WV9WARN" class="_3f-vr _208Ie blog-post-title-font _3tzpp _5aNAR css-x4x4qs _2QAo- _25MYV _2R0Lu _2Dym_">Step 2: Generate Device List</h3>
<div class="_1Lhwj image-container">If you want the device name preassigned for each device, follow this step. Otherwise, proceed to the Deployment section below.</div>
<div class="_1Lhwj image-container">To preassign the device name, choose <strong>Preconfigure Devices</strong> feature on the <strong>Screens </strong>tab to create a device list with a pairing code:</div>
<div class="_1Lhwj image-container"><img src="https://support.optisigns.com/hc/article_attachments/4416556453779" alt="screens tab with arrows showing how to get to preconfigure devices option"></div>
<div class="_1Lhwj image-container">
<div class="_1Lhwj image-container">In the popup, specify how many screens you want to preconfigure.</div>
<div class="_1Lhwj image-container"><img src="https://support.optisigns.com/hc/article_attachments/4416556459923" alt="preconfigure devices options screen 1"></div>
<div class="_1Lhwj image-container">Enter a prefix  to give to your device and assign some initial content to display onscreen. The device name will be generated based on the prefix with a sequence number added. This name can be changed later before deployment.</div>
<div class="_1Lhwj image-container"><img src="https://support.optisigns.com/hc/article_attachments/4416556506003" alt="preconfigure devices options screen 2"></div>
<div class="_1Lhwj image-container">Once done, the page will list all the devices preconfigured with the pairing code. Click <strong>Done</strong>.  This generates a CSV file named "preconfigure-devices.csv". Download it to your computer. </div>
<div class="_1Lhwj image-container"><img src="https://support.optisigns.com/hc/article_attachments/4416556695571" alt="preconfigure devices screen with two screens added"></div>
<div class="_1Lhwj image-container">Open the CSV file. It will contain the list of the preconfigured devices and their corresponding pairing code. To change the device name, simply update the CSV file. Then the file can be used in deployment if you want to have your screens using the exact pre-assigned name.</div>
<div class="_1Lhwj image-container"><img src="https://support.optisigns.com/hc/article_attachments/4416571675923" alt="preconfigure devices downloaded csv file"></div>
<div class="_1Lhwj image-container"> </div>
<div class="_1Lhwj image-container">
<hr>
<a name="Deployment"></a>
<h2 id="h_01HFD212FF68G0XF8B42K5ZEAZ" class="_3f-vr _208Ie blog-post-title-font _3tzpp _5aNAR css-x4x4qs _2QAo- _25MYV _2R0Lu _2Dym_">Deployment</h2>
<p>Once you have the provisioning template config file ready, you can proceed to the deployment. If you would like to pre-assign the exact name on the screen, you will need to get the preconfigured device list from step 2 as well.</p>
<a name="OptiSigns"></a>
<h3 id="h_01JA5XXTQP7JMACEJVVQ3XD7NR">OptiSigns Digital Signage Players and Windows/Linux Devices</h3>
<p>For mass provisioning deployment on the <a href="https://shop.optisigns.com/products/optisigns-android-stick-player-2" target="_blank" rel="noopener noreferrer">OptiSigns Android Player</a>, the <a href="https://shop.optisigns.com/products/optisigns-digital-signage-player">OptiSigns Pro Player</a>, or any Windows or Linux device, get a MicroSD card or USB drive and create a folder named "autoconfig" under the root directory. Place the CSV and CFG files into this folder.</p>
<p>Next, attach the MicroSD card/USB drive to your player. Launch the player, and the player will automatically detect the config file and start the provisioning process. You will receive this message once the provisioning is complete (with your local timezone configured):</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4416680470163" alt="mass provisioning success screen"></p>
<p>Alternatively, you can MDM the CSV file into:</p>
<ul>
<li>C:/autoconfig or C:/ProgramData/autoconfig on a Windows device</li>
<li><span style="color: #1d1c1d; font-family: Slack-Lato, Slack-Fractions, appleLogo, sans-serif; font-size: 15px; font-style: normal; font-variant-ligatures: common-ligatures; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: #f8f8f8; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;">~\autoconfig\ on a Linux or Mac</span></li>
</ul>
<p>Then, set up the OptiSigns <strong><a href="https://support.optisigns.com/hc/en-us/articles/1500001985341-How-to-Use-the-Local-Folder-App-in-OptiSigns" target="_blank" rel="noopener noreferrer">Local Folder app</a> </strong>to automatically boot it up.</p>
<a name="Raspberry"></a>
<h3 id="h_01J971XTCJGGG7D2235ZB8EF9P">Raspberry Pi Devices</h3>
<p>Raspberry Pi devices have two options for mass deployment: the USB method detailed above, or via SSH.</p>
<p>For more on the SSH method, see <a href="https://support.optisigns.com/hc/en-us/articles/1500008008981-How-to-enable-SSH-for-your-Raspberry-Pi" target="_blank" rel="noopener noreferrer">how to enable SSH for your Raspberry Pi</a> and <a href="https://support.optisigns.com/hc/en-us/articles/360063098753-How-to-mass-deploy-OptiSigns-on-Raspberry-Pi-devices" target="_blank" rel="noopener noreferrer">how to mass deploy OptiSigns on Raspberry Pi devices</a>.</p>
<a name="AppleTV"></a>
<h3 id="h_01J971Y008280N2R577Z3X9F3N">Apple TV and ChromeOS</h3>
<p>Deployment on an Apple TV or a ChromeOS device has to be done through their respective platforms.</p>
<p>For more, see our articles on <a href="https://support.optisigns.com/hc/en-us/articles/31695220475283-Configuring-Mass-Deployment-with-Jamf-Pro-MDM-on-Apple-Devices" target="_blank" rel="noopener noreferrer">configuring OptiSigns mass deployment on Apple devices</a> and <a href="https://support.optisigns.com/hc/en-us/articles/17353256033811-How-to-use-OptiSigns-Auto-Provisioning-Template-on-ChromeOS" target="_blank" rel="noopener noreferrer">how to use OptiSigns Auto Provisioning Template on ChromeOS</a> and</p>
<div class="_1Lhwj image-container"> </div>
<div class="_1Lhwj image-container">
<h3 id="h_01J971ZF7CK3CKZ6M0RHD38GH6" class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_"><strong>That's all! </strong></h3>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">Now you know how to perform mass provisioning with OptiSigns.</p>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self">support@optisigns.com</a></p>
</div>
<div class="_1Lhwj image-container"> </div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>