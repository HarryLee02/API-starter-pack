<h3 id="h_01JN1EVETCPW2QA8Z0YPQA0WRK">In this article, we will guide you through the process for displaying your device's information on screen.</h3>
<ul>
<li><a href="#Begin">Before You Begin</a></li>
<li><a href="#Step1">Step 1: Create Designer Asset</a></li>
<li>
<a href="#Step2">Step 2: Add a Device Data DataSource to the Asset and Map It</a>
<ul>
<li><a href="#Optional">Optional: Creating Additional Device Attributes</a></li>
</ul>
</li>
<li><a href="#Step3">Step 3: Assign the Asset to Screens</a></li>
</ul>
<p>Displaying your device's information onscreen has various advantages. Information like the screen name, assigned contents, and more can be helpful when:</p>
<ul>
<li>Managing a large network.</li>
<li>Many screens are placed together in the same location.</li>
<li>Running deployment or troubleshooting.</li>
</ul>
<p>Device information can be easily displayed using the OptiSigns Dynamic Data Mapping feature. By using this, you'll only need to create a single asset, which can be used on any device to display that specific device's information. Let's get started.</p>
<hr>
<p><a name="Begin"></a></p>
<h2 id="h_01JN1FANPNAYRKYEQ88VDC678K">Before You Begin</h2>
<p>Dynamic Data Mapping is available to <strong>Pro Plus </strong>subscribers or above.</p>
<p>Setting up a dynamic Device Info asset consists of three steps:</p>
<ol>
<li>Create a designer asset that fits your needs</li>
<li>Enable the data source for device info and maintain the mapping.</li>
<li>Assign the asset to your screen. </li>
</ol>
<hr>
<p><a name="Step1"></a></p>
<h2 id="h_01JN1FRE71D6JR0WP7BAADY0T2">Step 1: Create a Designer Asset</h2>
<p>To begin, go to the <strong>Files/Assets </strong>tab in the OptiSigns web portal. Click <strong>Apps</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/38883675197587" alt="firefox_k4Purluovg.jpg"></p>
<p>Now, open the <strong>Designer </strong>app:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/38883666973459" alt="firefox_Bo3ccQ4spb.jpg"></p>
<p>Once you've entered the Designer app, you'll need to create your Designer asset. This can display any way you'd like. If you wish to reuse it and apply it to all your screens, you may need to make this asset a generic size for placing into a <a href="https://support.optisigns.com/hc/en-us/articles/360026559573-How-to-Create-and-Use-the-Split-Screen-App" target="_blank" rel="noopener noreferrer"><strong>Split Screen zone</strong></a>.</p>
<p>In this example, we will set the canvas size to <strong>585 x 315</strong> in order to best fit a Split Screen zone. We'll create some placeholder text here to replace with our dynamic data in the next step:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42859076732691"></p>
<hr>
<p><a name="Step2"></a></p>
<h2 id="h_01JN1GBQCHCABA4YSFT79YCZ6T">Step 2: Add a Device Metadata DataSource to the Asset and Map It</h2>
<p>Next, we'll need to add a Device Metadata DataSource to retrieve device data. Click the <strong>DataSource</strong> tab on the left side of the screen, then hit <strong>Add DataSource </strong>at the top of the menu:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42859068384403"></p>
<p>A screen with numerous options will pop up. Scroll down until you see <strong>Device Metadata </strong>under Adv. DataSources, then click it.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42859076737427"></p>
<p>You'll be taken back to the DataSource menu, but there will be a new option - <strong>Device Data (default)</strong>. Click it.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42859068388243"></p>
<p>You'll be presented with data that looks something like this:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42859068390675"></p>
<p>By mapping these values to your asset, the specific screen data will be pulled, and the values in red will be replaced with values <em><strong>specific to your screen</strong></em>. In order to map them, simply click and drag the value into the field where you want them to display.</p>
<p>You can also display custom device attributes, but this is not necessary. If the default data is enough for you, skip to <a href="#Step3"><strong>step 3</strong></a>.</p>
<p><a name="Optional"></a></p>
<h3 id="h_01JN1JCF85M0B6P7BP5EVSXB2N">Optional: Setting Device Attributes</h3>
<p>In some cases, you may wish to configure a custom attribute on your device and have that displayed.</p>
<p>In the example above, we've made an "assetId" field, which is a custom attribute defined on the screen level. These attributes can denote anything - from the asset being displayed to the shop the device is used in. It's all up to you.</p>
<p>To create this, navigate to your <strong>Screens </strong>tab. Find the screen whose attributes you wish to change, then hit <strong>Edit</strong>. You'll be taken to the <strong>Edit Screen</strong> menu. Hit <strong>Advanced <span id="docs-internal-guid-11d419ba-7fff-ccc5-8844-9740b406bc4d">→</span> </strong><strong>More <span id="docs-internal-guid-11d419ba-7fff-ccc5-8844-9740b406bc4d">→</span> Device additional attributes</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/38883666992659" alt="firefox_hdXgPSnyE2.jpg"></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/38883666993555" alt="firefox_eigWT4aT3p.jpg"></p>
<p>This will bring up the <strong>Device additional attributes </strong>screen. Here, to create a new attribute, click <strong>New Attribute:</strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/38883675214355" alt="firefox_Z4jbp2DWQv.jpg"></p>
<p>Now, fill in the desired attributes with the appropriate data, then hit <strong>Update</strong>:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/38883666999059" alt="firefox_7ZsHFOeUuN.jpg"></p>
<p>These additional attributes will now map to a Device Metadata Datasource. You will need to configure these additional attributes per screen in order for them to display.</p>
<hr>
<p><a name="Step3"></a></p>
<h2 id="h_01JN1JWAXDY6VRZ29E8A1K7YZY">Step 3: Assign the Asset to Screen</h2>
<p>Once the mapping is complete, you can simply assign it to a screen. The asset will display information specific to the screen it's been assigned.</p>
<p>For the above example, let's assign it to a screen called "Demo Laptop". We've configured the "assetId" through Device Additional Attributes to be 123, and the rest of the data has been mapped appropriately. It should display like so:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/38884919962643" alt="mceclip0(1).jpg"></p>
<p>If we were to assign it to another screen, these values would change. This makes the Device Info asset highly valuable as a troubleshooting tool.</p>
<p><strong><span class="wysiwyg-font-size-x-large">That's all!</span></strong></p>
<p>This is how you can display device info on the screen using device data mapping feature.</p>
<p>If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self">support@optisigns.com</a></p>