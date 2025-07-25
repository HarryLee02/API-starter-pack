<p>Amazon recently released their new Gen 2 Fire Sticks that come with many changes including to its hardware and OS. While OptiSigns will run great on these new devices, there is an issue where the auto-start feature will not function properly, likely due to the updated version of Fire OS.</p>
<p>In this guide, we will show you how you can properly enable OptiSigns to auto-start on these new Gen 2 Fire Sticks.</p>
<p>Before we begin, please be sure you have the following ready:</p>
<ul>
<li>A computer.</li>
<li>Stable internet connection.</li>
<li>Ensure that both your computer and your Fire Stick are on the same network.</li>
<li>Android SDK Platform Tools installed on your computer.<br><a href="https://developer.android.com/tools/releases/platform-tools"><span class="wysiwyg-underline" style="color: #1155cc;">https://developer.android.com/tools/releases/platform-tools</span><br></a>
</li>
</ul>
<h4 id="h_01HGEDD45K3Z6B2BZN1GNMGDKK"><strong>Step 1:</strong></h4>
<p>On your Fire Stick, navigate to the settings then select “My Fire TV” then click on “Developer Options” and ensure that ABD Debugging is enabled.</p>
<p><br><strong>Note, in order to enable the developer options, follow these steps:</strong></p>
<ol>
<li><span class="wysiwyg-color-black">Go to “Settings” from the home screen of your Fire Stick.<br><br></span></li>
<li><span class="wysiwyg-color-black">Select the “My Fire TV” or “Device” option.<br><br></span></li>
<li><span class="wysiwyg-color-black">Click on “About”.<br> </span></li>
<li><span class="wysiwyg-color-black">Click on the first option where it labels the model of your Fire TV stick, quickly 7 times. You will see a notification at the bottom saying, "No need, you are already a developer" when this is complete.<br><br></span></li>
<li><span class="wysiwyg-color-black">Press the back button once or go back to “Settings” &gt; “My Fire TV” and you will now see "Developer Options".</span></li>
</ol>
<p><img src="https://support.optisigns.com/hc/article_attachments/23274690253587" width="586" height="298"></p>
<p> </p>
<h4 id="h_01HGEDDFSSW5SNZ9D9B43TQZ4R"><strong>Step 2:</strong></h4>
<p>Exit out of developer options then select “About” then “Network”. You will see the Fire Stick’s network information. In this case, we will want to write down the IP address:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/23274680489747" width="624" height="351"></p>
<h4 id="h_01HGEDDQS0T4SPD6TR5WG9PDQS"><strong>Step 3:</strong></h4>
<p>On your computer, you will need to have the Android SDK Platform Tools installed. You can install this by clicking on the link earlier in this guide. Make sure to create a folder somewhere on your computer such as your desktop then extract the contents on the Android SDK Platform Tools into that folder:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/23274673766803" width="624" height="348"></p>
<h4 id="h_01HGEDE23V6VQQN6T3YSSCKVP4"><strong>Step 4:</strong></h4>
<p>On your desktop, open the command prompt. On Windows you can do this by typing “cmd” in the search bar on your taskbar. On Mac, it will be called the Terminal.<br><br>Once you have this opened, type “cd \”</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/23274665378451" width="624" height="328"></p>
<p>Then type “cd android”</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/23274680497299" width="624" height="331"></p>
<p>Then type “dir”:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/23274643497875" width="624" height="332"></p>
<p>Type “adb connect &lt;The Firestick IP Address from step 2&gt;”</p>
<p><strong>NOTE: If you receive a message where it mentions “failed to authenticate to &lt;ip address&gt;” you will need to allow access from your Firestick. Check “always allow from this computer” and press “OK”. Then back on the command prompt, type “adb disconnect” and hit enter.</strong></p>
<p><strong><img src="https://support.optisigns.com/hc/article_attachments/23274690270739" width="624" height="316"></strong></p>
<p>Type adb connect &lt;Firestick’s IP address&gt; once more. Once connected, it should look like this:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/23274660262547" width="624" height="128"></p>
<p>After you’ve successfully connected, enter this command then hit enter:</p>
<pre><strong>adb shell pm grant com.optisigns.player android.permission.SYSTEM_ALERT_WINDOW</strong></pre>
<p>This command will now be sent to your Firestick in order to allow OptiSigns to have its auto-start function enabled.</p>
<p>And that’s it! You’re all set!</p>
<p>If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self" rel="undefined">support@optisigns.com</a> </p>