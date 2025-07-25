<h3 id="h_01JDATXHK65VXDQBR4HRH4BGHP">Jira is a popular project management tool that helps teams plan, track, release, and support work. Let's go through how to set this app integration up!</h3>
<p><strong>What you'll need:</strong></p>
<ul>
<li>Jira project or dashboard</li>
<li>Keyboard and mouse</li>
</ul>
<hr>
<p class="wysiwyg-text-align-left">In your Jira account, navigate to the page of the project or private dashboard that you'd like to display. Copy the direct URL.</p>
<p class="wysiwyg-text-align-left"><img src="https://support.optisigns.com/hc/article_attachments/35838410787219" alt="Jira dashboard with the URL pointed at"></p>
<p>Next, log in to <a href="https://app.optisigns.com/app/screenManagement" target="_blank" rel="noopener noreferrer">OptiSigns portal</a> and navigate to the files/assets page. Click Apps and search for Jira. </p>
<p class="wysiwyg-text-align-left"><img src="https://support.optisigns.com/hc/article_attachments/35838410792595" alt="Jira app within OptiSigns"></p>
<p>Here, you'll input certain information to create the asset:</p>
<p class="wysiwyg-text-align-center"><img src="https://support.optisigns.com/hc/article_attachments/35838425274899" alt="Jira app settings when setting it up in OptiSigns"></p>
<ul>
<li>
<strong>Name:</strong> Any name you'd like to give the asset for internal organizational purposes only.</li>
<li>
<strong>Type:</strong> Either URL or Embed code.</li>
<li>
<strong>URL/Embed Code:</strong> The direct link or code of the project or dashboard that you'd like to display.</li>
<li>
<strong>Update Interval:</strong> The duration of time between updates. (Default: 600 seconds).</li>
</ul>
<p>For "Sign In" settings, you will have to provide you log in so OptiSigns can easily log in for you. When your app is pushed to the screen, OptiSigns will use this information to automatically login to your account to display the URL/Embed code given:</p>
<ul>
<li>
<strong>Master Password:</strong> By default, OptiSigns will encrypt the whole script with OptiSigns private key to protect your script, especially username, password in the script. You can add another protection layer by entering a Master Password. If you enter Master Password here, at each device, you will need to enter that Master Password one time in OptiSigns app so it can decrypt the content. </li>
<li>
<strong>Username/Email:</strong> The email or username for the account you're using.</li>
<li>
<strong>Password:</strong> The password for the account you're using.</li>
</ul>
<p>Finally, click "<strong>Save</strong>".</p>
<h3 id="h_01JDQ4RJTSWH65EKDR8KC9SHB1">Verification Code</h3>
<p>When you push your Jira asset to your screen for the first time, Jira will send a verification code to your email. You will need to input this code into the asset pushed to your screen.</p>
<p>For this, you will need a <strong>keyboard and mouse </strong>connected to your device to input this. Afterward, Jira will recognize your device and not ask you to do this again.</p>
<p><a href="https://community.atlassian.com/t5/Jira-questions/Stop-asking-me-for-email-verification/qaq-p/1646087" target="_blank" rel="noopener noreferrer">According to Jira</a>, this is for security purposes so Jira can register the device to your account. </p>
<hr>
<h2 id="h_01JDMP27G7CDJ2QFVGVBJGK3PE">Troubleshooting</h2>
<ul>
<li>If your dashboard is public, it may display as empty. Making your dashboard private will allow OptiSigns to properly run the login script. </li>
</ul>