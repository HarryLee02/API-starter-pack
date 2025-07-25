<p>Chrome boxes are common for large-scale digital signage deployment as there are industrial-grade chrome boxes such as <a href="https://amzn.to/33Zcu22" target="_self">AOpen Commercial Chromebox</a> or <a href="https://amzn.to/2FS8FDP" target="_self">ASUS Chromebit</a></p>
<p>Chrome devices are very stable, and provide excellent performance, they can also be managed by Google Chrome Device Management which will simplify your large-scale deployment, ensure enterprise security, and reduce device management overhead. You can learn more about Google's Chrome Device Management <a href="https://support.google.com/chrome/a/answer/1289314?hl=en#:~:text=Enforce%20policies%20and%20manage%20apps&amp;text=You%20can%20make%20Wi%2DFi,Manage%20policies%20for%20Chrome%20devices." target="_self">here</a>.</p>
<h2 id="h_01HQ0C84EV0498WGV83D0E2SP6">Set up OptiSigns Player on your device with Chrome Device Management</h2>
<p>1) Setting Up ChromeOS Digital Signage Players for Automatic Provisioning with OptisSgns.</p>
<p>2) Using OptiSigns' Web portal to assign content and manage your screens.</p>
<p>Note: For large deployments, you can also use auto-provisioning templates to skip step 2. For more information, please check <a href="https://support.optisigns.com/hc/en-us/articles/17353256033811" target="_self">here</a>.</p>
<p> </p>
<p>So let's dive in!</p>
<h2 id="h_01HQ0C84EV9T5XEKRXXTKR32HK">1) Setting Up Optisigns on ChromeOS Device as a Digital Signage Players</h2>
<p>First, you need to use Chrome Enterprise and Single App Kiosk Mode. This allows you to manage Chrome devices to boot directly into the OptiSigns application. You can remotely manage the devices, update security patches, update the OptiSigns application, and set up in Kiosk …etc.</p>
<h3 id="h_01HQ0C84EVC9DGBJ4PXP2V5ERE">1 Chrome Enrollment and Set up</h3>
<p><strong>1.1 You need to have Google Enterprise Single App Kiosk Licenses</strong></p>
<p>Chrome Enterprise is Google's management system, and it lets you manage multiple Chrome devices through a single interface. You check <a href="https://chromeenterprise.google/" target="_blank" rel="noopener noreferrer">here</a> for purchasing Chrome Enterprise licenses.</p>
<p><strong>1.2 Enroll your ChromeOS Digital Signage Players</strong></p>
<p><a href="https://support.google.com/chrome/a/answer/1360534?hl=en" target="_blank" rel="noopener noreferrer">Click here</a> for Google Enterprise instructions to enroll your devices.</p>
<h3 id="h_01HQ0C84EV4GFAK277T3XAJYRG">2 Add Optisigns app to your devices</h3>
<p>Once your Chrome Device is enrolled in Chrome Device Management, you can add OptiSigns to your Google Device via Device Management Portal</p>
<ul>
<li>Go to<a href="https://admin.google.com/" target="_blank" rel="noopener noreferrer"> Google Admin</a> and login to your Google account</li>
<li>Click “<strong>Devices</strong>”</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/360090882514" alt="1.png"></p>
<ul>
<li>Click “<strong>Chrome devices</strong>”</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/360093009813" alt="2.png"></p>
<ul>
<li>Click on the "<strong>Chrome</strong>" at the top left of the page</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/360090882774" alt="5.png"></p>
<ul>
<li>Go to“<strong>Apps &amp; Extensions</strong>”</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/360090882794" alt="6.png"></p>
<ul>
<li>Select your "<strong>Organizational Unit</strong>", "<strong>Kiosks</strong>" and then "<strong>Add Chrome app or extension by ID"</strong>
</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/360093044833" alt="6.1.1.png"></p>
<ul>
<li>Enter Optisigns ID: <strong>ankpffnbahhgegojammhgdnbmdbfnnfe</strong> in “Add chrome app or extension by ID"</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/360090918914" alt="14.png"></p>
<ul>
<li>Once the Optisign has been added, set the app to <strong>Auto-launch</strong>, and SAVE it</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/360093044893" alt="15.png"></p>
<ul>
<li>Go back to the Chrome Management page, select <strong>Device settings</strong>:</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/360093044913" alt="6.1.png"></p>
<ul>
<li>In the Device settings, go to the <strong>Sign-in settings section</strong>, and set the following:
<ul>
<li>Guest mode to “<strong>Disable guest mode</strong>”</li>
<li>Sign-in restriction to “<strong>Do not allow any user to sign in</strong>”</li>
<li>User data to “<strong>Do not erase local user data</strong>”</li>
</ul>
</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/360093045093" alt="ChromeOS_11.png" width="702" height="437"></p>
<ul>
<li>Go to <strong>Kiosk settings section</strong>, set the Managed guest session to “<strong>Do not allow managed guest sessions</strong>”</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/360090919174" alt="ChromeOS_12.png" width="702" height="437"></p>
<h2 id="h_01HQ0C84EWBADFCA4A1BJMG654">2) Pair the app with OptiSigns portal &amp; assign content.</h2>
<p>If you set up Kiosk mode correctly in previous step, OptiSign App will be launched automatically when device is started, and it will generate a pairing code like below.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/360093951413" alt="mceclip0.png"></p>
<p>You now can go to our portal at: <a href="https://app.optisigns.com/">https://app.optisigns.com/ </a>to pair the screen.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/360093005473" alt="4.png" width="700" height="413"></p>
<p>Once you logged in Click "Add screen" button</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/360093005953" alt="5.png" width="702" height="295"></p>
<p>In this pop-up, type in the Pair Code showing up on the OptiSigns App. Then Click Pair.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/360093006013" alt="6.png" width="702" height="517"></p>
<p>The OptiSigns App will change to:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/360090879354" alt="7.png" width="701" height="392"></p>
<p>Now you are ready to upload and assign content.</p>
<p><strong>1. Upload video/ image to your account:</strong></p>
<p>Log on to your account. Click Files/ Assets</p>
<p>Click Upload Files</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/360093045373" alt="8.png" width="702" height="448"></p>
<p>In this pop up, click to browse the file or drag and drop your files here.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/360090919354" alt="9.1.png"></p>
<p><strong>2. Create a Playlist:</strong></p>
<p>Go to Playlist Tab: Click Create Playlist A "New Playlist" will appear at the bottom on the screen. Click on it.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/360090919374" alt="10.png" width="702" height="466"></p>
<p>Click on the pencil button to change Playlist name.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/360093045493" alt="11.png" width="702" height="117"></p>
<p>Change it to something meaningful for you. In this case, we will name it "Lobby TV Playlist"</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/360093045513" alt="12.png" width="701" height="245"></p>
<p>Drag and drop Video/Images that you uploaded to the playlist.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/360090919474" alt="13.png" width="702" height="306"></p>
<p>When you are done, it should look something like below.</p>
<p>You can click on the pencil button next to the item duration loke below to change the duration of the item on the playlist.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/360090919514" alt="14.png" width="703" height="312"></p>
<p><strong>3. Assign the playlist to your screen:</strong> </p>
<p>Go to the Screen tab.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/360090919534" alt="15.png" width="700" height="286"></p>
<p>Click the "Edit" button on the screen you want to change.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/360093045533" alt="16.png"></p>
<p>Click the Type drop-down list and select Playlist.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/360093045593" alt="17.png"></p>
<p>Click the Selected Playlist drop-down and select the playlist you've created. In this case we select "Lobby TV Playlist"</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/360090919594" alt="18.png" width="700" height="546"></p>
<p>Click Save.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/360090919654" alt="19.png"></p>
<p><strong>The Screen will be updated.</strong><br><br>If you want to change the playlist, add, remove Video/Image, change duration, etc.<br><br>You can go back to the Playlist tab and make the change to the playlist.<br><br>The device will update automatically.<br><br>You can also start using Apps like Google Slides or set up a Schedule for your content.</p>
<p> </p>
<p> </p>
<p>If you have feedback on how to make the how-to guides better, please let us know at: <a class="link-viewer_link__2qJYG blog-link-hashtag-color y_1_u" href="mailto:support@optisigns.com" target="_top" rel="noreferrer">support@optisigns.com</a></p>
<p> </p>