<p>If your Pro Player looks like the image below, read on. If it does not, read on <a href="https://support.optisigns.com/hc/en-us/articles/4408658251027-How-to-use-Remote-Command-Execution-Windows-Linux" target="_blank" rel="noopener noreferrer"><strong>Remote Commands for the OptiSigns Pro Player (Gen 3)</strong></a>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/38310905084947" alt="Pro Player.png" width="322" height="250"></p>
<h2 id="h_01JKEH11THWF3A8PC7G0KAWXCN">OptiSigns Pro Player Gen 2 Commands</h2>
<p>You can install/update OptiSigns player on your OptiSigns Pro Player with 1 command line script:</p>
<pre> ~/bin/manual_update.sh </pre>
<p>This script will download latest version of OptiSigns AppImage and run it.</p>
<p>You can use our Remote Access feature to access the OptiSigns Pro Player, go to this article &amp; copy the command line and run on the Pi to update. It will save time vs. manually clicking &amp; downloading methods.</p>
<p> </p>
<p>Other command line scripts:</p>
<ul>
<li> If your TV has color saturation issues, run this command to fix it:<br>
<pre>wget -O- <a class="c-link" style="font-family: monospace, monospace; font-size: 13px; white-space: pre;" href="https://download.optisignsapp.com/pro-player/change-color-profile.sh" target="_blank" rel="noopener noreferrer" data-stringify-link="https://download.optisignsapp.com/pro-player/change-color-profile.sh" data-sk="tooltip_parent">https://download.optisignsapp.com/pro-player/change-color-profile.sh</a><span style="background-color: #e9ebed; font-family: monospace, monospace; font-size: 13px; white-space: pre;"> | bash </span></pre>
</li>
<li>Overwrite the automatic security updates timing
<pre>bash~/bin/override_upgrade_schedule.sh 23:30</pre>
</li>
<li>To lock the USB port, if you want to lock the device to prevent tampering fully.
<pre>~/bin/optisigns-lockusb.sh</pre>
</li>
<li>To unlock the USB port.
<pre>~/bin/optisigns-unlockusb.sh</pre>
</li>
</ul>
<p>If you have any additional questions or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self">support@optisigns.com</a></p>