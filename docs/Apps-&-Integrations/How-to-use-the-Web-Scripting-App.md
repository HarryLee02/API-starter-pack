<h3 id="h_01HY12S92BSCPAAPAME3M4HVMM">Web Scripting is an advanced feature for OptiSigns' Pro Plus subscribers or higher, enabling users to automate website navigation and form entries without any coding. This guide will walk you through recording your script, creating Web Scripting assets in OptiSigns, and using them securely on your screens.</h3>
<p id="h_01HY12X432GG0N16SPD4MZP7SW"><strong>In this article</strong></p>
<ol>
<li><a href="#What">What is Web Scripting</a></li>
<li><a href="#Record">Record Your Script</a></li>
<li><a href="#Create">Create Web Scripting Asset in OptiSigns</a></li>
<li><a href="#Using">Using It on Your Screens</a></li>
</ol>
<p><a name="What"></a></p>
<h2 id="h_01HY1310CR6XADXFDZVEP1YG3R">What is Web Scripting</h2>
<p>Web Scripting is a feature that allows users to automate navigation and form entry on websites without any coding. This tool records user actions, such as entering usernames and passwords, navigating to specific pages, handling pop-ups, running your own JavaScript and more on a website, and then encrypts the recorded script for secure execution on designated devices.</p>
<p>OptiSigns encrypt all the scripts and your password entered with our own private keys.</p>
<ul>
<li>This will ensure your data/password is safe as soon as it left your browsers and only get decrypted at device level before the fields are entered.</li>
</ul>
<p>We also provide Zero Knowledge encryption method so that you can protect your script with your own Master Password. <em>You can read more at the end of this article.</em></p>
<p>If your dashboard requires login with the 2FA, OptiSigns supports the 2FA in the Web Scripting app. You can read more <a href="https://support.optisigns.com/hc/en-us/articles/19145077187859" target="_self">here</a>.</p>
<p id="h_01HQ273MDTWJKKGD77SFHGWC1T"><strong>Let's jump in and get started!</strong></p>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td class="wysiwyg-text-align-center" style="width: 100%;"><strong>NOTE</strong></td>
</tr>
<tr>
<td style="width: 100%;">Web Scripting is not supported on Samsung SSSP or LG WebOS smart TVs.</td>
</tr>
</tbody>
</table>
<h2 id="h_01HQ273MDTNT4CH42T2K6ES6MK">
<a name="Record"></a> <strong>Record Your Script</strong>
</h2>
<p class="wysiwyg-text-align-left"><strong><iframe src="//www.youtube-nocookie.com/embed/v8fObpJWGX0" width="560" height="315" frameborder="0" allowfullscreen=""></iframe></strong></p>
<p>In this article, we will show you how to use a tool called Burp Suite Navigation Recorder. You can use other tools if that can generate similar scripts that works too. We recommend Burp Suite because it's a reputable tool used by many companies, including the Fortune 500.</p>
<p><strong>1. You need to install Burp Suite Navigation Recorder.</strong></p>
<p>Open <strong>Chrome Browser</strong>.</p>
<p>Go to Chrome Web Store: <a href="https://chrome.google.com/webstore/category/extensions">https://chrome.google.com/webstore/category/extensions</a></p>
<p>Search for: "<strong>Burp Suite Navigation Recorder</strong>".</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/1500019933121" alt="mceclip0.png"></p>
<p>Click on it.</p>
<p>Then click <strong>Add to Chrome.</strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/1500019933141" alt="mceclip1.png"></p>
<p>Burp Suite Navigation Recorder is installed</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/1500019660122" alt="mceclip2.png" width="478" height="292"></p>
<p>Click on the <strong>Navigation Recorder Icon.</strong></p>
<p>Then click <strong>Open Settings</strong> to finish set up.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/1500019660142" alt="mceclip3.png" width="420" height="383"></p>
<p>Scroll down and click <strong>"Allow in Incognito".</strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/1500019660162" alt="mceclip4.png"></p>
<p>Close this tab.</p>
<p>Now, if you click on the Navigation Recorder icon again, you will have option to Start Recording.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/1500019933161" alt="mceclip5.png" width="506" height="462"></p>
<p><strong>2. Record your Script</strong></p>
<p>From the Navigation Recorder extension pop out like in above screenshot, click <strong>Start Recording.</strong></p>
<p>It will open an <strong>Chrome Incognito window</strong>.<br>You can put in the URL of the website or page you want to start with.<br>Then fill out the forms. (such as, entering your username, password and click Login)</p>
<table style="border-collapse: collapse; width: 88.2857%;" border="1">
<tbody>
<tr>
<td style="width: 100%;">
<h3 id="h_01HY13NVVJEB6B6RPQ7BMFPFJH"><strong>Important Notes to Follow to Reduce Issues Later!</strong></h3>
</td>
</tr>
<tr>
<td style="width: 100%;">
<strong>Always start with the destination URL</strong> (The URL of the page you want to display). Let the website handle the redirection once you fill out the login information.</td>
</tr>
<tr>
<td style="width: 100%;">
<p><strong>Always click the Login button,</strong> instead of Enter.</p>
</td>
</tr>
<tr>
<td style="width: 100%;">
<p><strong>Correctly enter your fields in 1 attempt!</strong> Type slow and carefully. Don't use backspaces or arrows keys to modify. If you mess up, please restart this step from the beginning.</p>
</td>
</tr>
</tbody>
</table>
<p> </p>
<p><img src="https://support.optisigns.com/hc/article_attachments/1500019660182" alt="mceclip6.png"></p>
<p>You can click around, navigate to certain page, position on page etc.</p>
<p>Once you are done,  click on the <strong>Navigation Recorder Extension icon</strong> and click <strong>Stop Recording.</strong></p>
<p>This will close the Incognito window that you are working on.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/1500019933181" alt="mceclip7.png"></p>
<p> </p>
<p>Go back to Chrome, click <strong>Navigation Recorder icon.</strong><br>Click "<strong>Copy to Clipboard</strong>". This will copy your script to clipboard.<br>Now you are ready to put in use in OptiSigns.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/1500019660322" alt="mceclip8.png"></p>
<p><a name="Create"></a></p>
<h2 id="h_01HQ273MDT1ZSGVJ5WYJQTQA1T"><strong>Create Web Scripting Asset in OptiSigns</strong></h2>
<p>Log in to OptiSigns <a href="https://app.optisigns.com/">https://app.optisigns.com/</a></p>
<p>Click <strong>File/Assets</strong></p>
<p>Click <strong>Apps</strong> and select <strong>Web Scripting.</strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/1500019660382" alt="mceclip10.png"></p>
<p>Enter the information for your Web Scripting asset:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4404440196883" alt="mceclip0.png"></p>
<ul class="rich-content-viewer_unorderedListContainer__2PG9L PM4OL">
<li class="rich-content-viewer_unorderedList__1BJwx rich-content-viewer_elementSpacing__208Ie _3_7DB AvMd_ _310Mz rich-content-viewer_left__2p1aK _158eo _3_7DB">
<strong><u>Name</u>:</strong> Name of your asset your asset list. It will <u><strong>not</strong></u> be displayed on your screens.</li>
<li>
<strong><span class="wysiwyg-underline">Master Password:</span> </strong>By default, OptiSigns will encrypt the whole script with OptiSigns private key to protect your script, especially username, password in the script. You can add another protection layer by entering a Master Password. If you enter Master Password here, at each device, you will need to enter that Master Password one time in OptiSigns app so it can decrypt the content. </li>
<li>
<strong><u>Recorded Script:</u></strong> Paste the script recorded by the Navigation Recorder here. You can take notice to the script, it's actually not very complicated, you can make some minor changes if you need to.</li>
</ul>
<p><strong>Here's how the encryption flow works:</strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/1500019937601" alt="mceclip12.png"></p>
<p>If you want to add additional security by utilizing a Master Password and our Zero Knowledge Encryption framework you will have to enter your Master Password when:</p>
<ul>
<li>Creating/editing assets</li>
<li>One time at each devices, so it will know how to decrypt</li>
</ul>
<p>Your script is encrypted at your browser, and transfer securely using HTTPS/SSL during transits and stored on our servers.<br>It then sends securely to devices, and decrypted at device level right before executing on the target website.</p>
<p><a name="Using"></a></p>
<h2 id="h_01HQ273MDT28HAY95A884X903R"><strong>Using It on Your Screens</strong></h2>
<p>Once created, the Web Scripting asset can be used in by itself or in Playlists, Schedules, or SplitScreen zones just like any other assets.</p>
<p>If you don't use Master Password, device will use OptiSigns private key to decrypt and execute, so no additional action is needed on the devices.</p>
<p>If you choose to use Master Password and our Zero Knowledge Encryption framework, you will have to enter your Master Password at each device</p>
<ul>
<li>This only needs to be done once on each device and can be used to decrypt all Scripting Assets. (Of course, you have to use the same Master Password to encrypt them).</li>
</ul>
<p> </p>
<h2 id="h_01HQ273MDVKKXVR20DXP86NP2B"><strong>That's all!</strong></h2>
<p>Congratulation, you have created Web Scripting assets, now you can automatically log in to gated websites, navigate to pages as needed.</p>
<p>If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self" rel="undefined">support@optisigns.com</a> </p>