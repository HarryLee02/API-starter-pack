<h3 id="h_01JC3Q66ZBWTXQ7SFRWT799DEE"><span style="color: #434343;">In this article, we will explain how to install a root certificate on your devices to set up an internal website for use with OptiSigns.</span></h3>
<ul>
<li><a href="#ProPlayer">Installing a Root Certificate on an OptiSigns Gen 3 Pro Player</a></li>
<li><a href="#Ubuntu">Installing a Root Certificate on a Linux/Ubuntu Device</a></li>
<li>
<a href="#Windows">Installing a Root Certificate on a Windows Device</a>
<ul>
<li><a href="#MMC">Open the Microsoft Management Console (MMC)</a></li>
<li><a href="#Snap-In">Add the Certificates Snap-in</a></li>
<li><a href="#Import">Import the Certificate</a></li>
<li><a href="#Verify">Verify the Installation</a></li>
<li><a href="#Command1">Command Line Installation</a></li>
</ul>
</li>
<li>
<a href="#MacOS">Installing a Root Certificate on a MacOS Device</a><br>
<ul>
<li><a href="#Install">Install Certificate</a></li>
<li><a href="#Command2">Command Line Installation</a></li>
</ul>
</li>
<li><a href="#Chrome">Installing a Root Certificate on Chrome-Based Web Browsers</a></li>
<li>
<a href="#InternalWebsite">Setting Up an Internal Website for Use on OptiSigns Using the Website App</a>
<ul>
<li><a href="#WebScripting">Using Web Scripting to Bypass Logins</a></li>
</ul>
</li>
</ul>
<p>OptiSigns digital signage software is an extremely valuable tool for internal communication, capable of displaying internal memos, communications, and announcements across numerous locations and offices. Messaging can be tailored to specific audiences, scheduled, and automatically synced to data sources.</p>
<p>With all these capabilities, it stands to reason that some want to incorporate OptiSigns into their intranet, or internal website. These can be displayed on your screens using the OptiSigns Website app, or Advanced Website app in some cases.</p>
<p>However, in order to do this, you’ll need a trusted, self-signed root certificate installed on the platform you choose to run it on. Here, we’ll show you how to get that installed.</p>
<p>Please note that you’ll need to obtain a trusted certificate yourself. This will need to be some sort of key, usually denoted by a <strong>.pem </strong>file extension.</p>
<p>In this article, we will walk you through two main steps:</p>
<ol>
<li>Installing a root certificate on your device of choice (OptiSigns Pro Player, Ubuntu, Windows, MacOS, or Chrome browser)</li>
<li>Configuring a Website app to display your internal website</li>
</ol>
<div>
<table style="width: 100%; height: 66px;">
<colgroup> <col> </colgroup>
<tbody>
<tr style="height: 22px;">
<td style="text-align: center; height: 22px;"><strong>NOTE</strong></td>
</tr>
<tr style="height: 44px;">
<td style="height: 44px;">Before you start, make sure you’re connected to the same network as the server you’re trying to access.</td>
</tr>
</tbody>
</table>
</div>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td style="width: 100%;"><strong>Please note that Android devices are not supported at this time.</strong></td>
</tr>
</tbody>
</table>
<hr>
<p><a name="ProPlayer"></a></p>
<h2 id="h_01JC3Q66ZC8H18VZSMRN5H1MVV">Installing a Root Certificate on an OptiSigns Gen3 Pro Player</h2>
<p>In order to get your root certificate onto an OptiSigns Pro Digital Signage Player, you’ll need to manually add it. Find where your certificate is stored, then download it to a USB or MicroSD card. Plug the card into the Pro Player.</p>
<div>
<table style="width: 100%;">
<colgroup> <col> </colgroup>
<tbody>
<tr>
<td style="text-align: center;"><strong>IMPORTANT</strong></td>
</tr>
<tr>
<td>For installation on a Gen 3 Pro Player, your certificate must have a <strong>.crt </strong>extension. However, it is important that this certificate is signed and contains your public key. These are usually generated as <strong>.pem </strong>files. You’ll need to rename your certificate (.pem) file and change its extension to <strong>.crt </strong>for your internal website to properly display.</td>
</tr>
</tbody>
</table>
</div>
<p>Now, open your OptiSigns player menu. Go to <strong>About → Advanced Settings</strong>.</p>
<p><strong><img src="https://support.optisigns.com/hc/article_attachments/35184705322515" width="463" height="309"></strong></p>
<p>Here, you’ll see a field called <strong>Certificate File</strong>. </p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35184705339539" width="177" height="383"></p>
<p>Simply locate your certificate on your USB or MicroSD card and select it. The certificate will automatically be downloaded to the appropriate location. This will allow your OptiSigns player to display your internal website.</p>
<hr>
<p><a name="Ubuntu"></a></p>
<h2 id="h_01JC3Q66ZC3RYYM1QK0BD1E0XR">Installing a Root Certificate on OptiSigns Gen 2 Pro Players and Linux/Ubuntu Devices</h2>
<p>To install a root certificate on a Linux or Ubuntu device, you’ll need to make heavy use of the <strong>Terminal.</strong></p>
<p>To begin, take your trusted, signed certificate (.pem file) and place it in the <span style="color: #188038;">/usr/share/ca-certificates </span>folder.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35184720058515" width="532" height="307"></p>
<div>
<table style="width: 100%;">
<colgroup> <col> </colgroup>
<tbody>
<tr>
<td style="text-align: center;"><strong>NOTE</strong></td>
</tr>
<tr>
<td>You will need to rename your <strong>.pem </strong>file to make it a <strong>.crt </strong>file, or else this will not work.</td>
</tr>
</tbody>
</table>
</div>
<p>After the certificate has been moved and renamed, you’ll need to refresh the installed certificates and hashes. Open your <strong>Terminal </strong>and type in this command:</p>
<pre>sudo update-ca-certificates</pre>
<p>Once this command is executed, it should say that it has installed 1 (or more) new certificate.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35184720067475" width="511" height="331"></p>
<p>This means the certificate has been added to the operating system and signed certificates will be trusted.</p>
<p>Now, you’ll want to install the certificate in the Chromium store using this command:</p>
<pre><span style="color: #1d1c1d; background-color: #f8f8f8;">certutil -A -n "ROOT-CA" -t "TCu,Cu,Tu" -i /usr/share/ca-certificates/[name-of-cert].crt -d sql:/home/[user]/.pki/nssdb</span></pre>
<p><span style="color: #1d1c1d; background-color: #f8f8f8;">The Linux-based OptiSigns app uses Chromium, so this will allow the certificate to pass through the OptiSigns app.</span></p>
<p><span style="color: #1d1c1d; background-color: #f8f8f8;">Now reboot your device.</span></p>
<p><span style="color: #1d1c1d; background-color: #f8f8f8;">Congratulations! You’ve successfully installed a root certificate on Ubuntu.</span></p>
<hr>
<p><a name="Windows"></a></p>
<h2 id="h_01JC3Q66ZC6BYP8TGCX5JG953E">Installing a Root Certificate on a Windows Device</h2>
<p>Broadly, there are four major steps to installing a root certificate locally on a Windows device:</p>
<ol>
<li>Open the Microsoft Management Console (MMC)</li>
<li>Add the Certificates Snap-In</li>
<li>Import the Certificate</li>
<li>Verify the Installation</li>
</ol>
<p>These same steps can be performed quickly using the Windows Terminal, if you’re so inclined.</p>
<p>Be cautious when installing root certificates, especially self-signed ones. Only install certificates from sources you trust completely.</p>
<div>
<table style="width: 100%;">
<colgroup> <col> </colgroup>
<tbody>
<tr>
<td style="text-align: center;"><strong>NOTE</strong></td>
</tr>
<tr>
<td>You need administrator privileges to install certificates in the Trusted Root Certification Authorities store.</td>
</tr>
</tbody>
</table>
</div>
<p><a name="MMC"></a></p>
<h3 id="h_01JC3Q66ZCSJ0KG76AZX2G82QH"><span style="color: #434343;">Open the Microsoft Management Console (MMC)</span></h3>
<p>The first step is opening the Microsoft Management Console (MMC), which is a framework for managing Windows components.</p>
<p>To do this, click <strong>Start, </strong>type <strong>mmc </strong>into the Search bar, then press <strong>Enter</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35184705345939" width="624" height="249"></p>
<p><a name="Snap-In"></a></p>
<h3 id="h_01JC3Q66ZCVSMYT4ES7WYWP75N"><span style="color: #434343;">Add the Certificates Snap-In</span></h3>
<p>With the MMC open, go to <strong>File → Add/Remove Snap-In</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35184705348371" width="259" height="249"></p>
<p>In the “Available snap-ins” list, select <strong>Certificates </strong>and click <strong>Add.</strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35184720078227" width="624" height="444"></p>
<p>Choose <strong>Computer account </strong>to manage certificates for the local computer. Click <strong>Next</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35184705352851" width="521" height="387"></p>
<p>Next, click <strong>Local computer </strong>and click <strong>Finish</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35184705355155" width="519" height="387"></p>
<p>Click <strong>OK </strong>to close the “Add or Remove Snap-ins” dialog.</p>
<p><a name="Import"></a></p>
<h3 id="h_01JC3Q66ZCNADTPN9XWNJ53KXV"><span style="color: #434343;">Import the Certificate</span></h3>
<p>Now <strong>Certificates (Local Computer)</strong> will appear as an option in your MMC. To continue, exp[and the <strong>Certificates (Local Computer) </strong>option within the right pane of the console. Then, expand <strong>Trusted Root Certification Authorities</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35184720086931" width="320" height="373"></p>
<p>Right-click on the <strong>Certificates </strong>folder and select <strong>All Tasks → Import</strong>.</p>
<p><strong><img src="https://support.optisigns.com/hc/article_attachments/35184720091795" width="491" height="149"></strong></p>
<p>This will open the Certificate Import Wizard. Click <strong>Next </strong>to get started.</p>
<p>Now, click <strong>Browse. </strong>Locate your self-signed certificate and select it. This should be a .pem file. You may need to expand the file name options to <strong>All Files</strong> to see it.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35184705362323" width="358" height="365"></p>
<p>Select the file and click <strong>Open → Next.</strong></p>
<p>Select <strong>Place all certificates in the following store. </strong>Ensure that <strong>Trusted Root Certification Authorities </strong>is selected, then click <strong>Next.</strong></p>
<p><strong><img src="https://support.optisigns.com/hc/article_attachments/35184705364115" width="389" height="377"></strong></p>
<p>Now you’ll be asked to confirm whether you want to complete the import. As long as you trust the certificate, agree to it by hitting <strong>Finish</strong>.</p>
<p><strong><img src="https://support.optisigns.com/hc/article_attachments/35184705368339" width="372" height="360"></strong></p>
<p><a name="Verify"></a></p>
<h3 id="h_01JC3Q66ZCY47MT1RB065G9QG3"><span style="color: #434343;">Verify the Installation</span></h3>
<p>Close the MMC.</p>
<p>Open a web browser and try accessing the local<span style="color: #188038;"> host domain</span>. If the certificate is installed correctly, you should no longer see the security warning. However, because it's a self-signed root certificate, you might still see a warning indicating that the website's identity cannot be verified.</p>
<p>If you encounter any issues, double-check the file paths, file names, and the output of the Certificate Import Wizard for any error messages.</p>
<p><a name="Command1"></a></p>
<h3 id="h_01JC3Q66ZCE0NX4EB3GV0TPZNE"><span style="color: #434343;">Command Line Installation</span></h3>
<p>You can also use the <strong>Terminal</strong> to directly install the certificate. Simply open up the Terminal app with Administrator privileges after searching for it on your Start bar, and input the following command:</p>
<pre><span style="color: #1d1c1d; background-color: #ffffff;">certutil –addstore –f "Root" “</span><span style="color: #1d1c1d; background-color: #f8f8f8;">C:\path\to\your_certificate_file”</span></pre>
<p><span style="color: #1d1c1d; background-color: #f8f8f8;">This will automatically install the certificate to the Trusted Root Certificates folder and you should be able to access the host domain in the same way as above.</span></p>
<hr>
<p><a name="MacOS"></a></p>
<h2 id="h_01JC3Q66ZCPC4CG9P8E07X1QBY">Installing a Root Certificate on a MacOS Device</h2>
<p>To prepare for the installation, make sure your device is connected to the same network of host servers you plan to use. Also, make sure your certificate is in a folder (the Download folder will work) on the device installing the certificates.</p>
<p><a name="Install"></a></p>
<h3 id="h_01JC3Q66ZC0PW4BMZPJX7D6D70"><span style="color: #434343;">Install Certificate</span></h3>
<p>To begin, open <strong>Keychain Access</strong>. This is normally located in the “Other” folder in the launchpad.</p>
<p class="wysiwyg-indent2"><img src="https://support.optisigns.com/hc/article_attachments/35184720101907" width="323" height="187"></p>
<p>Select the System tab within the menu on the left. If you see a padlock icon next to the System folder, right click to unlock and enter the system password. </p>
<p class="wysiwyg-indent2"><img src="https://support.optisigns.com/hc/article_attachments/35184720103571" width="380" height="260"></p>
<p class="wysiwyg-indent1"><img src="https://support.optisigns.com/hc/article_attachments/35184720107027" width="509" height="175"></p>
<p>Open the folder where your certificate is stored. Drag and drop the certificate into the system folder in Keychain Access. If a red x is displayed next to the certificate like below, keep following along. Otherwise, you’re done.</p>
<p class="wysiwyg-indent1"><img src="https://support.optisigns.com/hc/article_attachments/35184705380883" width="489" height="154"></p>
<p>Right click the certificate and select “<span style="color: #ff9900;">get info</span>”</p>
<p class="wysiwyg-indent2"><img src="https://support.optisigns.com/hc/article_attachments/35184705382291" width="493" height="247"></p>
<p>Select “<span style="color: #ff9900;">Trust</span>”.</p>
<p class="wysiwyg-indent1"><span style="color: #ff9900;"><img src="https://support.optisigns.com/hc/article_attachments/35184720114579" width="338" height="285"></span></p>
<p>Select “<span style="color: #ff9900;">Always Trust</span>”. This means your computer will always trust this certificate to keep your connection secure.</p>
<p class="wysiwyg-indent2"><img src="https://support.optisigns.com/hc/article_attachments/35184705386771" width="353" height="302"></p>
<p>Exit and you will be prompted with entering password. Enter the system password.</p>
<p>Your certificate is now installed. You will now be able to access the local website. </p>
<p><a name="Command2"></a></p>
<h3 id="h_01JC3Q66ZCRQN9KAJEQ1NNS462"><span style="color: #434343;">Command Line Installation</span></h3>
<p>On MacOS, you can also use the Terminal to directly install the Certificate. Simply type in these commands:</p>
<p><strong>Use the following command to add a certificate:</strong></p>
<pre><span style="color: #333333; background-color: #f5f5f5;">sudo</span><span style="color: #bbbbbb; background-color: #f5f5f5;"> </span><span style="color: #333333; background-color: #f5f5f5;">security</span><span style="color: #bbbbbb; background-color: #f5f5f5;"> </span><span style="color: #333333; background-color: #f5f5f5;">add-trusted-cert</span><span style="color: #bbbbbb; background-color: #f5f5f5;"> </span><span style="color: #333333; background-color: #f5f5f5;">-d</span><span style="color: #bbbbbb; background-color: #f5f5f5;"> </span><span style="color: #333333; background-color: #f5f5f5;">-r</span><span style="color: #bbbbbb; background-color: #f5f5f5;"> </span><span style="color: #333333; background-color: #f5f5f5;">trustRoot</span><span style="color: #bbbbbb; background-color: #f5f5f5;"> </span><span style="color: #333333; background-color: #f5f5f5;">-k</span><span style="color: #bbbbbb; background-color: #f5f5f5;"> </span><span style="color: #333333; background-color: #f5f5f5;">/Library/Keychains/System.keychain</span><span style="color: #bbbbbb; background-color: #f5f5f5;"> </span><span style="color: #333333; background-color: #f5f5f5;">“</span><span style="color: #ff9900; background-color: #f5f5f5;">new-root-certificate</span><span style="color: #333333; background-color: #f5f5f5;">”</span></pre>
<p><strong>Use the following command to remove a certificate:</strong></p>
<pre><span style="color: #333333; background-color: #f5f5f5;">sudo</span><span style="color: #bbbbbb; background-color: #f5f5f5;"> </span><span style="color: #333333; background-color: #f5f5f5;">security</span><span style="color: #bbbbbb; background-color: #f5f5f5;"> </span><span style="color: #333333; background-color: #f5f5f5;">delete-certificate</span><span style="color: #bbbbbb; background-color: #f5f5f5;"> </span><span style="color: #333333; background-color: #f5f5f5;">-c</span><span style="color: #bbbbbb; background-color: #f5f5f5;"> </span><span style="color: #4070a0; background-color: #f5f5f5;">"</span><span style="color: #ff9900; background-color: #f5f5f5;">name of existing certificate</span><span style="color: #4070a0; background-color: #f5f5f5;">"</span></pre>
<hr>
<p><a name="Chrome"></a></p>
<h2 id="h_01JC3Q66ZCYRF4CFDKZC8PN8N7">Installing a Root Certificate on Chrome-Based Web Browsers</h2>
<p>Depending on the operating system, Chrome will use the system-wide certificates (such as the ones installed above) or its own certificates. If you are having trouble getting a system-wide certificate to work for your internal website, you may wish to try directly installing a root certificate to Chrome (or any Chromium browser) directly.</p>
<p>To begin, open the <strong>Settings </strong>tab in the Chrome browser.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35184720118803" width="306" height="632"></p>
<p>Next, click <strong>Privacy and security</strong> <strong>→ Security → Manage Certificates</strong></p>
<p><strong><img src="https://support.optisigns.com/hc/article_attachments/35184705392531" width="624" height="505"></strong></p>
<p>This will open the Certificates manager. You’ll need to add your internal website certificate as an authority. Here, click the <strong>Trusted Root Certification Authorities </strong>tab, then click <strong>Import</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35184720125715" width="423" height="385"></p>
<p>This will open the Certificate Import Wizard. Click <strong>Browse </strong>and locate the certificate necessary for your internal website. Then, click <strong>Next</strong>.</p>
<p><strong><img src="https://support.optisigns.com/hc/article_attachments/35184720127635" width="406" height="418"></strong></p>
<p>On the next screen, <strong>Place all certificates in the following store</strong> and make sure it’s “Trusted Root Certification Authorities”. Then hit <strong>Next</strong>.</p>
<p><strong><img src="https://support.optisigns.com/hc/article_attachments/35184705364115" width="389" height="377"></strong></p>
<p>Now you’ll be asked to confirm whether you want to complete the import. As long as you trust the certificate, agree to it by hitting <strong>Finish</strong>.</p>
<p><strong><img src="https://support.optisigns.com/hc/article_attachments/35184705368339" width="372" height="360"></strong></p>
<p>Congratulations, you’ve installed your root certificate on your Chrome browser.</p>
<hr>
<p><a name="InternalWebsite"></a></p>
<h2 id="h_01JC3Q66ZC757P6B31KN1Q2MFG">Setting an Internal Website Up for Use on OptiSigns Using the Website App</h2>
<p>The OptiSigns Website app allows you to display an internal website on your screens once a valid private certificate (.pem file) has been installed on your device.</p>
<p>To set it up, navigate to <strong>Files/Assets </strong>in your OptiSigns portal. Find the <strong>Website</strong> app.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35184705404947" width="447" height="323"></p>
<p>Enter the <strong>URL </strong>of your webpage here. The Name field is irrelevant to the app’s function and will only make the asset easier to find in OptiSigns.</p>
<div>
<table style="width: 100%;">
<colgroup> <col> </colgroup>
<tbody>
<tr>
<td style="text-align: center;"><strong>NOTE</strong></td>
</tr>
<tr>
<td>If your internal website is large and complex, you can also display it using the <strong>Advanced Website </strong>app. If you’re having trouble displaying it on the basic Website app, create an Advanced Website asset and try again.</td>
</tr>
</tbody>
</table>
</div>
<p>Once the Website asset is created, it can be assigned to a screen.</p>
<p><a name="WebScripting"></a></p>
<h3 id="h_01JC3Q66ZCDQMJN5ZNYVHKTHYQ"><span style="color: #434343;">Using Web Scripting to Bypass Logins</span></h3>
<p>Many internal websites require logins to work. In this case, the Website app will not be sufficient to access them on the OptiSigns app. In this case, we recommend our Web Scripting app.</p>
<p>Follow our complete <a href="https://support.optisigns.com/hc/en-us/articles/1500012522362-How-to-use-the-Web-Scripting-App"><span class="wysiwyg-underline" style="color: #1155cc;">guide to using the Web Scripting app</span></a> to set that up.</p>
<h3 id="h_01JC3Q66ZCNMNB5JCR0A8D4X54"><span style="color: #434343;">That’s all!</span></h3>
<p>OptiSigns is the leader in <a href="https://www.optisigns.com/"><span class="wysiwyg-underline" style="color: #1155cc;">digital signage software</span></a>. If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com"><span class="wysiwyg-underline" style="color: #1155cc;">support@optisigns.com</span></a>.</p>