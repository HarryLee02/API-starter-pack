<h4 id="h_01JCK6KCZ7GQSVM90CKYRKM6W3">Displaying Salesforce Dashboards on your digital screens is crucial to getting real-time data directly to who needs it. Let's go through how to set up your MFA-protected Salesforce Dashboard by using our Web Scripting app!</h4>
<p>Things You'll Need:</p>
<ul>
<li><a href="https://www.salesforce.com/" target="_blank" rel="noopener noreferrer">Salesforce Dashboard</a></li>
<li><a href="https://chromewebstore.google.com/detail/burp-suite-navigation-rec/anpapjclbjicacakeoggghfldppbkepg" target="_blank" rel="noopener noreferrer">Burp Suite Navigation Recorder</a></li>
<li>Authenticator App (ex., Google Authenticator)</li>
</ul>
<hr>
<h2 id="h_01JCK463M0DQMR9R2R5VVMS3PN">Setting Up MFA</h2>
<table style="border-collapse: collapse; width: 100%; height: 51px;" border="1">
<tbody>
<tr style="height: 51px;">
<td class="wysiwyg-text-align-center" style="width: 100%; height: 51px;">
<p><em>If you don't already have MFA set up for your Salesforce account, please visit their support article: <strong><span class="wysiwyg-color-blue110"><a href="https://help.salesforce.com/s/articleView?id=sf.security_overview_2fa.htm&amp;type=5" target="_blank" rel="noopener noreferrer"><span class="wysiwyg-color-green130">Multi-Factor Authentication for Salesforce Orgs.</span></a></span></strong></em></p>
</td>
</tr>
</tbody>
</table>
<p>Next, go to your account settings &gt; My Personal Information &gt; Advanced User Details</p>
<p>From there, click <strong>"Connect"</strong> on "<strong>App Registration: One-Time Password Authenticator</strong>"</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35528791304211" alt="Salesforce account settings and setting up authenticator app"></p>
<p>When Salesforce prompts you to connect an Authenticator App, <strong>DO NOT</strong> immediately scan the QR code.</p>
<p>Click "<strong>I Can't Scan the QR Code</strong>".</p>
<p class="wysiwyg-text-align-center"><img src="https://support.optisigns.com/hc/article_attachments/35528807336979" alt="Salesforce setting up authenticator app. Select 'I can't scan the QR code'"></p>
<p> </p>
<p><strong>Copy and paste the alphanumeric string</strong> displayed underneath "Key". <strong>Save this key</strong> somewhere secure, like the Notepad app. </p>
<ul>
<li>This is <em><strong>necessary</strong> </em>for the web scripting process later. </li>
</ul>
<p>Next, enter that setup key in your authenticator app, then enter the verification code into Salesforce, and connect!</p>
<p class="wysiwyg-text-align-center"><img src="https://support.optisigns.com/hc/article_attachments/35528807340691" alt="Save the setup key that Salesforce provides you."></p>
<p><strong>Your MFA is now set up!</strong></p>
<hr>
<h2 id="h_01JCK4ZKM2KCHPW4A9VVNSH6V8">Record &amp; Set Up Your Web Scripting App</h2>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td class="wysiwyg-text-align-center" style="width: 100%;"><em>You can refer to our<strong> <a href="https://support.optisigns.com/hc/en-us/articles/1500012522362" target="_blank" rel="noopener noreferrer"><span class="wysiwyg-color-green130">How to use the Web Scripting App article </span></a></strong>on how to download Burp Suite Navigation Recorder and record your script.</em></td>
</tr>
</tbody>
</table>
<p class="wysiwyg-text-align-left">During the recording process, <strong>write down the exact verification code</strong> you inputted to log in to your account.</p>
<ul>
<li>This is <strong><em>necessary</em> </strong>when setting up the Web Scripting app. </li>
</ul>
<p>Once your script is recorded, Burp Suite should automatically copy it to your clipboard. You can also copy it to your clipboard by opening Burp Suite in the extension manager:</p>
<p class="wysiwyg-text-align-center"><img src="https://support.optisigns.com/hc/article_attachments/35528791311507" alt="Click 'Copy to clipboard' on Burp Suite Navigation extension to copy the script again."></p>
<p>Log in to your OptiSigns account and open the Files/Assets page to create your asset. Click on <strong>"Apps"</strong> You need to:</p>
<ol>
<li>Paste your script into the "<strong>Recorded Script</strong>" box</li>
<li>Paste the alphanumeric setup key you saved from Salesforce into "<strong>Secret 2FA</strong>"</li>
<li>Input the <em>exact</em> verification code you used during the login process while recording into the "<strong>Recorded 2FA Code</strong>" box.</li>
</ol>
<p class="wysiwyg-text-align-center"><img src="https://support.optisigns.com/hc/article_attachments/35528807348627" alt="Web scripting in OptiSigns and pasting the script, setup key, and 2fa code in their respective boxes."></p>
<p>Click <strong>Save!</strong></p>
<hr>
<p>Now you can <a href="https://support.optisigns.com/hc/en-us/articles/18988049363859" target="_blank" rel="noopener noreferrer">push this app to your screen, </a><a href="https://support.optisigns.com/hc/en-us/articles/360026559573">add it to a split screen app</a>, and more!</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35377393852691" alt="A salesforce dashboard displayed on a split screen app to show the dashboard, weather, and important news on your TV."></p>
<p>If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at support@optisigns.com</p>