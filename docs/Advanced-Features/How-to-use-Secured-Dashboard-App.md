<p>Displaying KPIs and reports on the screen is a common use case for enterprise customers, however, companies are using different reporting systems, which makes this a difficult task to accomplish. OptiSigns has delivered a <a href="https://support.optisigns.com/hc/en-us/articles/1500012522362" target="_self">Web Scripting App</a> for customers to access their password-protected reporting systems without coding, it also supports Multi-Factor Authentication, for details please follow this <a href="https://support.optisigns.com/hc/en-us/articles/19145077187859" target="_self">article</a>.</p>
<p>Web Scripting App executes the scripts locally on the device, it is the recommended solution for customers to access their reports. However, there are still cases in which customers need another way to execute and display the reports. Below are a few examples. A Secured Dashboard is recommended in these situations. </p>
<ul>
<li>Customers use the same account with MFA to authenticate on multiple devices. Since MFA is using a one-time passcode, it will error if multiple device authentications are started at the same time.</li>
<li>Customers have a mixed device fleet, like Windows and Android are used together. Reports may render differently on Windows and Android, which may cause inconsistency in the report presentation.</li>
<li>Customers have reports that take a long time to execute/load, and looking for ways to avoid showing the loading status on the screen.  </li>
</ul>
<p>Secured Dashboard App will take the same scripts you recorded with the Web Scripting App, put it to execute on a dedicated instance, and return a screenshot of the reports. It can help address all the situations mentioned above and more.</p>
<p> </p>
<h2 id="h_01HQ095J1JD8Y32DM84SPJF9F5" class="rich-content-viewer_headerTwo__3f-vr rich-content-viewer_elementSpacing__208Ie blog-post-title-font _3aQMT _2J4pr css-x4x4qs rich-content-viewer_left__2p1aK _158eo _3_7DB"><strong>Let's jump in and get started:</strong></h2>
<p class="rich-content-viewer_headerTwo__3f-vr rich-content-viewer_elementSpacing__208Ie blog-post-title-font _3aQMT _2J4pr css-x4x4qs rich-content-viewer_left__2p1aK _158eo _3_7DB"><strong>1. Get the scripts ready</strong><br>Secured Dashboard uses the same scripts you recorded when you use the Web Scripting App. You can follow the document below and use Burp Suite Navigation Recorder to prepare the scripts and test them on the Web Scripting App.<br><a href="https://support.optisigns.com/hc/en-us/articles/1500012522362-How-to-use-Web-Scripting-App" rel="noopener noreferrer">How to use Web Scripting App – OptiSigns</a><br>If you are using MFA, you can follow this document, to get the MFA set up with the token and secret.</p>
<p class="rich-content-viewer_headerTwo__3f-vr rich-content-viewer_elementSpacing__208Ie blog-post-title-font _3aQMT _2J4pr css-x4x4qs rich-content-viewer_left__2p1aK _158eo _3_7DB"><a href="https://support.optisigns.com/hc/en-us/articles/19145077187859" target="_self">How to use Web Scripting App with 2FA</a><br>Once the script is tested with Web Scripting App, you can copy it and create the Secured Dashboard App with the same info.</p>
<p class="rich-content-viewer_headerTwo__3f-vr rich-content-viewer_elementSpacing__208Ie blog-post-title-font _3aQMT _2J4pr css-x4x4qs rich-content-viewer_left__2p1aK _158eo _3_7DB wysiwyg-text-align-center"><img src="https://support.optisigns.com/hc/article_attachments/19593475063955"></p>
<p> </p>
<p><strong>2. Configure the Secured Dashboard execution</strong><br>There are a few settings that allow you to control how the scripts are executed. Secured Dashboard will execute the scripts on a dedicated instance, and then take a screenshot of the report according to your settings.</p>
<ul class="rich-content-viewer_unorderedListContainer__2PG9L PM4OL">
<li>
<u>Resolution</u>: The default setting is 1080p - FHD(1920x1080) in landscape mode. You can choose other resolutions, even custom resolutions. Please note if you would like to display in portrait mode, you will need to choose custom resolutions and set the resolutions accordingly, e.g. 1080x1920.</li>
<li>
<u>Full Page</u>: If you select full page, it will take a screenshot of the entire webpage, even if the webpage is scrollable.</li>
<li>
<u>Clip</u>: This allows you to take screenshots of certain sections of the webpage. You can set the starting point of the screenshot from the top left, and the width and height of the screenshot.<br><img src="https://support.optisigns.com/hc/article_attachments/19595347412627">
</li>
<li>
<u>Delay</u>: This allows you to set when the screenshot is taken. The default is 30 seconds, meaning the screenshot will start the 30s after the scripts are executed. If your report data takes a long time to load, you can set a proper value here to pass the loading.</li>
</ul>
<p> </p>
<p>After completing all the settings, you can assign it to the screens, the screenshots will update at the set interval. </p>
<p><strong>Note:</strong> If your reporting systems have firewall rules or using CAPTCHA to block bots, you can contact us to get the IP address that you can use for whitelisting</p>
<h2 id="h_01HQ095J1K4T03DS4J60A8C66P" class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB"><strong>That's all!</strong></h2>
<p>If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self">support@optisigns.com</a></p>