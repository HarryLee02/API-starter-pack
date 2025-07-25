<p>OptiSigns AI Add-on is a background service running on your Linux, Raspberry Pi device to use a Camera to detect &amp; count people passing by.</p>
<p>If you have not tried to automatically activate this feature, please try it first by following <a href="https://support.optisigns.com/hc/en-us/articles/27690296225555" target="_blank" rel="noopener noreferrer">this guide</a>.</p>
<p>The add-on is a ~200MB app, so it will take several minutes to download and activate on your device, so please be patient after auto-activation before you try manual activation.</p>
<p>If auto-activation fails, then you can follow these steps to manually install &amp; activate AI detection add-on on your Linux or Raspberry Pi devices.</p>
<p> </p>
<p><strong>Before you start, please ensure that you have:</strong></p>
<ul>
<li>Your device has OptiSigns Digital Signage player version 4.2.10 or newer installed. You can download the latest version <a href="https://www.optisigns.com/download" target="_blank" rel="noopener noreferrer">here</a>.</li>
<li>There's a network connection to your device</li>
<li>You have enough authorization, and privileges to install apps, and background services on your device</li>
<li>optisigns-ai-detection runs on any Raspberry Pi OS, or any major Linux distro such as Ubuntu.</li>
</ul>
<h2 id="h_01HPZMCNESCYBV02HAAQ7WSFCY"><strong>How to manually install optisigns-ai-detection</strong></h2>
<p>Make sure you have a camera installed on your system.<br>Open Terminal.</p>
<p>On Raspberry Pi run:</p>
<pre>curl -s https://links.optisigns.com/ai-add-on-rpi-install -L | sh</pre>
<p>On Linux run:</p>
<pre>curl -s https://links.optisigns.com/ai-add-on-linux-install -L | sh</pre>
<p>This will download a script and run the installation.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/360099273994" alt="mceclip0.png"></p>
<p>After you see "Starting OptiSigns AI Detection Service ..." you are done!</p>
<p>You can go back to <a href="https://app.optisigns.com/app/screenManagement">app.optisigns.com </a>to use the AI feature now</p>
<h2 id="h_01HPZMCNESJD5AMBCGTZ9XTZH5"><strong>Further technical detail for optisigns-ai-detection</strong></h2>
<p>The binary executable is downloaded and installed to ~/bin/optisigns-ai-detection</p>
<p>It will be started as a background service and will be automatically started on system start-up.</p>
<p>This will ensure the AI detection add-on is independent of OptiSigns Digital Signage Player and still running in case the Player has an issue or you need to reinstall it.</p>
<p>You can manually execute the optisigns-ai-detection executable:</p>
<pre>&lt;path&gt;/optisigns-ai-detection [arg]<br>install : to install ai detection agent<br>remove : to remove/uninstall ai detection agent<br>start or restart : to start ai detection agent service<br>stop : to stop ai detection agent service<br>version or -V : to print ai detection agent version<br>help : to print this instructions<br>run : to run the ai detection agent in console or terminal or service<br>show or -s: show camera feed</pre>
<h2 id="h_01HPZMCNESA3C19N3KN4T3YN3R"><strong>How to remove optisigns-ai-detection:</strong></h2>
<p>Open Terminal and run:</p>
<pre>~/bin/optisigns-ai-detection remove</pre>
<p> </p>
<p>If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self" rel="undefined">support@optisigns.com</a></p>
<p> </p>