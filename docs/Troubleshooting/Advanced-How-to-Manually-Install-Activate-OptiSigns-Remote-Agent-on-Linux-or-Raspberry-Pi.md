<h3 id="h_01JAE4KJCVH7J733CB2KRV24BY">In this article, we will show you how to complete a manual installation of the OptiSigns Remote Agent on a Linux or Raspberry Pi device.</h3>
<p>If you're running OptiSigns on a Windows, Linux or Raspberry Pi device, you can install optisigns-remote-agent add-on that will allow you to remotely control your device from the portal.</p>
<p>If you have not tried to automatically activate this feature, please try it first by following <a href="https://support.optisigns.com/hc/en-us/articles/360055486554" target="_self">this guide</a>.</p>
<p>If automatic activation fails, follow these steps to manually install &amp; activate the OptiSigns remote agent on your Linux or Raspberry Pi device.</p>
<p><strong>Before you start, please ensure that:</strong></p>
<ul>
<li>Your device has OptiSigns Digital Signage player installed. Download the latest version <a href="https://www.optisigns.com/download" target="_blank" rel="noopener noreferrer">here</a>.</li>
<li>Your device has an active network connection.</li>
<li>You have the authorization and privileges to install apps and background services on your device.</li>
</ul>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td class="wysiwyg-text-align-center" style="width: 100%;"><strong>NOTE</strong></td>
</tr>
<tr>
<td style="width: 100%;">The Remote Control feature is only available to subscribers with a <strong>Pro Plus </strong><strong>plan or above.</strong>
</td>
</tr>
</tbody>
</table>
<h2 id="h_01HQ0792CTF7VBJYZFC1RDJ3QH"><strong>How to manually install optisigns-remote-agent</strong></h2>
<p>Open Terminal.</p>
<p>On Raspberry Pi run:</p>
<pre>curl -s https://release.optisigns.com/optisigns-remote-agent-setup-rpi.sh -L | sh</pre>
<p>On Linux run:</p>
<pre>curl -s https://release.optisigns.com/optisigns-remote-agent-setup-linux.sh -L | sh</pre>
<p>This will download a script and run installation.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/360095986553" alt="mceclip0.png"></p>
<p>After you see "Starting Remote Control Service ..." you are done!</p>
<p>You can go back to app.optisigns.com to use Remote Control feature now.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/18614175492243" width="546" height="963"></p>
<p> </p>
<h2 id="h_01HQ0792CWP28AR95V3DS2VYVG"><strong>More Technical Details for optisigns-remote-agent</strong></h2>
<p>The binary executable is downloaded and installed to ~/bin/optisigns-remote-agent</p>
<p>It will be started as a background service and will automatically boot on system start up.</p>
<p>This ensures the remote agent is independent from OptiSigns Digital Signage Player and still running in case the Player encounters an issue, or you need to reinstall it.</p>
<p>You can manually execute the optisigns-remote-agent executable:</p>
<pre>&lt;path&gt;/optisigns-remote-agent [arg]<br>install : to install remote agent<br>remove : to remove/uninstall remote agent<br>start or restart : to start remote agent service<br>stop : to stop remote agent service<br>version or -V : to print remote agent version<br>help : to print this instructions<br>run : to run the remote agent in console or terminal or service</pre>
<h2 id="h_01HQ0792CWW0GJC86X0Y38XNZQ"><strong>How to remove optisigns-remote-agent:</strong></h2>
<p>Open Terminal and run:</p>
<pre>~/bin/optisigns-remote-agent remove</pre>
<p> </p>
<h3 id="h_01JAE4MSMK8523KHFBAWB5XJWV">That's all!</h3>
<p>OptiSigns is a leader in <a href="https://www.optisigns.com/" target="_blank" rel="noopener noreferrer">digital signage software</a>. If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self" rel="undefined">support@optisigns.com</a></p>
<p> </p>