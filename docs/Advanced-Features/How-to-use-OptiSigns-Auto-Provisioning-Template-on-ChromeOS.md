<p>ChromeOS is a popular platform for digital signage with its excellent performance and ease of device management. Google's new Kiosk &amp; Signage Upgrade license for Chrome device management, makes ChromeOS a more competitive option in the digital signage space. </p>
<p>OptiSigns supports Auto Provisioning on ChromeOS, your digital signage deployment using ChromeOS can be fully automated by utilizing our auto-provisioning template. The auto-provisioning process can get the device paired to your account automatically.</p>
<p>If you are new to the ChromeOS deployment, you can read <a href="https://support.optisigns.com/hc/en-us/articles/360054033374" target="_self">here</a> first to see how to deploy the OptiSigns application on ChromeOS with Chrome Device Management. This document will follow the provisioning of OptiSigns application(section 1 of the above-mentioned document) and walk you through how to use an auto-provisioning template for Chrome to get the device automatically paired to your account.</p>
<h2 id="h_01HAAD3B98XKD53XVKQJ5M5P8R"><strong>Let's jump in and get started:</strong></h2>
<p><strong>1) Create an auto-provisioning template for your Chrome deployment</strong></p>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">To create a provisioning template, you can either access it from the admin menu or use the below link.</p>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_"><a href="https://app.optisigns.com/app/s/provisioning-templates">https://app.optisigns.com/app/s/provisioning-templates</a></p>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">Create a new provisioning template by clicking the "Create templates" button. </p>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_"><img src="https://support.optisigns.com/hc/article_attachments/17360386666771" alt="mceclip0.png"></p>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">Then set the template in the popup.</p>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_"><img src="https://support.optisigns.com/hc/article_attachments/17360357432467" alt="mceclip1.png"></p>
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
<u>WIFI:</u> Select from the stored WIFI, need to be created first. Only required if you want to setup WIFI during provisioning. WIFI setup is normally not needed for ChromeOS deployment. Because the deployment will be managed through Chrome Device Management.</li>
<li>
<u>Time Zone:</u> Specify the time zone of the device.</li>
<li>
<u>Tags:</u> Specify the tags you want to associate to the devices.</li>
<li>
<span class="wysiwyg-underline">Initial Default Content Type</span>: Used to set the initial content on the device after provisioning.</li>
<li>
<u>Orientation:</u> Set the orientation, landscape is the default.</li>
<li>
<u>Sync Play:</u> Used to set the turn on/off of the sync play feature. For more details of Sync Play feature, please click <a href="https://support.optisigns.com/hc/en-us/articles/4412065189267-Synchronized-playback-Sync-Play-feature" target="_blank" rel="noopener noreferrer">here</a>.</li>
<li>
<u>Location:</u> Set the location of the device.</li>
</ul>
<p>Once the template is created, it will be available under the list of provisioning templates, you can download the config file and it will be used later during deployment. Please make sure to select "ChromeOS" when you click the download button. The configuration file's name is "provisionting-template-&lt;Your Template Name&gt;.txt"</p>
<div class="q2uC4 _2vlB-">
<div class="_2CvYQ c-Mgr _1K2V0 _1K2V0 _1hD8w">
<div class="_1Lhwj image-container"><img src="https://support.optisigns.com/hc/article_attachments/17359692661139"></div>
<div class="_1Lhwj image-container">The file will contain a JSON object, this is what is needed later when setting up auto provisioning on Google Chrome Device Management.</div>
<div class="_1Lhwj image-container"><img src="https://support.optisigns.com/hc/article_attachments/17359871365139"></div>
<div class="_1Lhwj image-container"> </div>
<div class="_1Lhwj image-container"><strong>2) Create mass provisioning template for your Chrome deployment</strong></div>
</div>
</div>
<p>OptiSigns uses policy extensions on ChromeOS to provision the device into your account.</p>
<p>Please follow section 1 of this document(<a href="https://support.optisigns.com/hc/en-us/articles/360054033374" target="_self">how to deploy OptiSigns on ChromeOS with Chrome Device Management</a>) to complete the auto provisioning of the OptiSigns application on your ChromeOS device.</p>
<p>Then go to "Apps&amp;extensions" from Chrome Device Management, find the OptiSigns app from the Kiosks setting.</p>
<p>Find the "Policy for extensions", this is where you put the JSON object from the auto provisioning template file generated above.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/17360066112659"></p>
<p> </p>
<p>Save it, then you are ready to start your deployment.</p>
<p>You just need to follow the normal deployment procedure to deploy your ChromeOS device. At the time of deployment, OptiSigns application will be auto installed on your ChromeOS device, then OptiSigns application will check the extension policy, if auto provisioning template is found, OptiSigns application will automatically pair the device to your account and assign the content that was defined in the template. </p>
<p> </p>
<p><strong><span class="wysiwyg-font-size-x-large">That's all!</span></strong></p>
<p> </p>
<p>If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self">support@optisigns.com</a></p>