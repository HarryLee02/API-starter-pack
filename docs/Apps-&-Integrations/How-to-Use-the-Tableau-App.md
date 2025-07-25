<h3 id="h_01JP06YW7AQS3DR677X1C0M2FV"><span style="color: #434343;">In this article, we’ll show you how to set up and use the Tableau app to display Dashboards on digital signs.</span></h3>
<ul>
<li><a href="#WhatYouNeed">What You’ll Need</a></li>
<li><a href="#Step1">Step 1: Set Up OptiSigns as a Connected App in Tableau</a></li>
<li><a href="#Step2">Step 2: Set Up Tableau Integration in OptiSigns</a></li>
<li><a href="#Step3">Step 3: Creating a Tableau Asset</a></li>
<li><a href="#Notes">Additional Notes</a></li>
</ul>
<p>With the Tableau app, it’s possible to securely display Tableau dashboards on your large TVs and screens. This can dramatically increase communication and information across office spaces.</p>
<p>To do this, you’ll need to follow three steps:</p>
<ol>
<li>Set up OptiSigns as a Connected App within Tableau</li>
<li>Set up the Tableau Integration in OptiSigns</li>
<li>Create a Tableau Asset and Assign it to a Screen</li>
</ol>
<p>Let’s get started.</p>
<hr>
<p><a name="WhatYouNeed"></a></p>
<h2 id="h_01JP06YW7AZREDEDVSCW7ETAMQ">What You’ll Need</h2>
<ul>
<li>OptiSigns <a href="https://www.optisigns.com/pricing" target="_blank" rel="noopener noreferrer">Pro Plus</a> subscription or greater</li>
<li>A screen,<a href="https://www.optisigns.com/blog/how-to-set-up-digital-signs-with-optisigns-and-amazon-fire-tv" target="_blank" rel="noopener noreferrer"> set up and paired</a> with OptiSigns</li>
<li>Tableau Cloud account</li>
<li>A fully created Tableau Report</li>
</ul>
<hr>
<p><a name="Step1"></a></p>
<h2 id="h_01JP06YW7A8XABNT89SN3F8YDF">Step 1: Set Up OptiSigns as a Connected App in Tableau Cloud</h2>
<p>To view Private reports in OptiSigns, it needs to be set up as a <strong>Connected App</strong> in Tableau Cloud. If you’re only interested in displaying Public reports, this step can be skipped - however, we <strong><em>highly recommend </em></strong>it, as setting up this integration will allow you to use it for any future reports you want to display from this account. If you are only interested in displaying Public reports, though, feel free to <a href="#Step3">skip to step 3</a>.</p>
<p>To begin, find your <strong>Settings </strong>tab within Tableau. Once there, click <strong>Connected Apps </strong>→ <strong>New Connected App</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/39250613919635" alt="new connected app tableau" width="624" height="396"></p>
<p>Select <strong>Direct Trust</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/39250613922451" alt="direct trust dropdown tableau" width="146" height="85"></p>
<p>You’ll open the Create Connected App window. Here, you can give your connected app a name (we recommend “OptiSigns” so you know it’s for us), restrict its access, and provide allowed domains. For the purposes of this example, we’ll apply it to “All projects” and “All domains.”</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/39250613923987" alt="create connected app window tableau" width="454" height="268"></p>
<p>Once created, it will appear in a list of Connected Apps. Select the app.</p>
<p>On this screen, you'll want to <strong>Enable </strong>the OptiSigns app by hitting the <strong>Three Dots</strong>. Then, you'll want to hit <strong>Generate New Secret</strong>:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/39672709375507" alt="Screenshot 2025-03-22 at 5.27.26 PM.jpg"></p>
<p>The blurred out values are your <strong>Secret ID, Secret Value, and Client ID</strong>. These values will be critical to setting up your integration with OptiSigns, so keep this tab open.</p>
<p>With this information and the app Enabled in Tableau, we can configure the integration in OptiSigns.</p>
<hr>
<p><a name="Step2"></a></p>
<h2 id="h_01JP06YW7AGXQCXHY3WF2AE5QJ">Step 2: Set Up Tableau Integration in OptiSigns</h2>
<p>Before starting this step, you should have:</p>
<ol>
<li>Your <strong>Secret ID, Secret Value, and Client ID </strong>from your Connected App in Tableau on hand</li>
<li>Your Connected App set to Enable</li>
</ol>
<p>When you’re ready to go, navigate to the <strong>Integrations </strong>tab within OptiSigns:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/39250660697107" alt="integrations tab optisigns" width="328" height="598"></p>
<p>Under the Tableau section of the Integrations page, select <strong>Add Connection</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/39597853563283" width="624" height="112"></p>
<p>The <strong>Add </strong>window will pop up:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/39250613933203" alt="add integrations window optisigns" width="624" height="432"><br>You’ll need to fill in 5 values:</p>
<ul>
<li>
<strong>Name - </strong>The name of the integration. Put whatever you want to help identify it.</li>
<li>
<strong>Email - </strong>The email associated with your Tableau account. This <strong><em>has to match</em></strong>.</li>
<li>
<strong>Client ID - </strong>The Client ID from <a href="#Step1">the last step</a>.</li>
<li>
<strong>Secret ID - </strong>The Secret ID from the last step.</li>
<li>
<strong>Secret Value - </strong>The Secret Value from the last step.</li>
</ul>
<p>Last, make sure the <strong>Active </strong>box is checked. When unchecked, this saves the integration but does not activate it.</p>
<p>Once these values are filled in, hit <strong>Add</strong>. We are now ready to create a Tableau Asset.</p>
<hr>
<p><a name="Step3"></a></p>
<h2 id="h_01JP06YW7AQAXN7P14FVYH5YE2">Step 3: Create a Tableau Asset and Assign it to a Screen</h2>
<p>Now that we’ve got the Tableau integration set up, it’s time to create a Tableau asset. This asset determines how your report will show up on your screens.</p>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td class="wysiwyg-text-align-center" style="width: 100%;"><strong>NOTE</strong></td>
</tr>
<tr>
<td style="width: 100%;">See <a href="#Note2"><strong>Note 2</strong></a> if your workbook contains Broad Views.</td>
</tr>
</tbody>
</table>
<p>First, find the report you’d like to display. Hit <strong>Share:</strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/39364492002579"></p>
<p>On the Share View window, hit <strong>Copy Link</strong>:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/39250613936275" alt="share view copy link tableau" width="382" height="244"></p>
<p>Now go back to the OptiSigns portal and hit <strong>Files/Assets </strong>→ <strong>Apps:</strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/39250613937555" alt="optisigns files/assets tab app" width="414" height="387"></p>
<p>Now find the <strong>Tableau </strong>app.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/39250660711955" alt="tableau app optisigns" width="448" height="247"></p>
<p>Clicking the app will open this window:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/39597827693203" width="500" height="265"></p>
<ul>
<li>
<strong>Name - </strong>The name of your Asset. This is used entirely in OptiSigns and can be anything you like.</li>
<li>
<strong>Tableau Shared Report URL - </strong>This is where you’ll input the Share URL you copied earlier.</li>
<li>
<strong>Update Interval -</strong> Denotes how often the app will sync, measured in seconds.</li>
<li>
<strong>Authenticate with Connected App Integration - </strong>Tick this box if you want to use Private reports. Since we set this up in <a href="#Step1">Steps 1</a> and <a href="#Step2">2</a>, we recommend ticking this box. If you skipped those steps and only want to use Public reports, no need to check the box.</li>
</ul>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td class="wysiwyg-text-align-center" style="width: 100%;"><strong>NOTE</strong></td>
</tr>
<tr>
<td style="width: 100%;">Tableau Cloud only allows 600 Update Interval requests per user/hour. See <a href="#Note3"><strong>Note 3</strong></a> for more information and solutions on how to handle this.</td>
</tr>
</tbody>
</table>
<p>Now it's time to authenticate your Shared Report URL with an appropriate Connected App Integration you set up earlier:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/39597827694099" width="624" height="441"></p>
<ul>
<li>
<strong>Connected App Integration - </strong>Select the integration <a href="#Step2">you set up in Step 2</a> in this box.</li>
</ul>
<p>Once you input the <strong>Tableau Shared Report URL</strong> and have selected your Integration, hit <strong>Save</strong> and your report should appear as a Preview:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/39597827695763"></p>
<p>Once you have tailored it to your liking, you can <strong>Close</strong> it. This will create a Tableau asset that can be added to a Playlist or directly assigned to a screen:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/39597853567251"></p>
<p>In order to display different tabs of a report, select the tab you'd like to view on Tableau site, then hit <strong>Share</strong>, same way as before:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/39250660703635" alt="tableau report share" width="624" height="296"></p>
<p>You'll then create a new Asset with that Share link as the <strong>Site URL</strong>:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/39597827698067"></p>
<p>To display all the tabs in a report on a screen, these Assets can be placed in a <a href="https://support.optisigns.com/hc/en-us/articles/28295104605843-How-to-Create-Use-Playlists" target="_blank" rel="noopener noreferrer">Playlist</a> to show the complete report.</p>
<p><a name="Notes"></a></p>
<h2 id="h_01JPX5487YXVSHD0APYBDCTZCW">Additional Notes</h2>
<h4 id="h_01JPX5GNQHENEK45KGFX30RXBA">Note 1</h4>
<p>Content display may vary based on device type and screen resolution.</p>
<p><a name="Note2"></a></p>
<h4 id="h_01JPX5GXEJ52XG5QCWZVGK4MVA">Note 2</h4>
<p><strong>If your workbook contains broad views:</strong></p>
<ul>
<li style="list-style-type: none;">
<ul>
<li style="list-style-type: none;">
<ul>
<li>Create Custom Views on the Tableau site and use the Custom View's URL as the Shared Report URL.<img src="https://support.optisigns.com/hc/article_attachments/39597853568787">
</li>
<li>Set the View Size to either <strong data-start="173" data-end="186">Fit Width</strong>, <strong data-start="188" data-end="202">Fit Height</strong>, or <strong data-start="207" data-end="222">Entire View</strong>:<br><img src="https://support.optisigns.com/hc/article_attachments/39597827704979">
</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><a name="Note3"></a></p>
<h4 id="h_01JPX5G2MK2XGPTN7XF455KYAQ">Note 3:</h4>
<p><a href="https://help.tableau.com/current/online/en-us/to_site_capacity.htm" target="_blank" rel="noopener noreferrer">Tableau currently limits</a> its maximum number of refresh requests to 600 per hour/user. This means you'll want to be careful on how you set the "Update Interval," especially if you have numerous devices wanting to display Tableau reports.</p>
<p>We have several recommendations on how to handle this with multiple devices:</p>
<ol>
<li>Set the Update Interval to match the number of devices. For example, if you have 50 devices, you can have a maximum Update Interval of 5 minutes (300 s) for a single report. With more devices this Update Interval will need to be longer, with less, it can be shorter.</li>
<li>For using Reports in a Playlist, the Report will update each time it is played. You'll need to set the proper duration, factoring in the number of reports and the number of devices. For example, if you have 10 reports on a single playlist across 5 devices, you can have a Playlist duration of 5 minutes (300 s).</li>
<li>To scale beyond these limitations, you'll need to create more connected apps under different Tableau Cloud users. Each Tableau Cloud user will have 600 requests an hour.</li>
</ol>
<h3 id="h_01JP06YW7A7FNFXM37N438AWMK"><span style="color: #434343;">That’s all!</span></h3>
<p>OptiSigns is the leader in <a href="https://www.optisigns.com/" target="_blank" rel="noopener noreferrer">digital signage software</a>. If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_blank" rel="noopener noreferrer">support@optisigns.com</a>.</p>