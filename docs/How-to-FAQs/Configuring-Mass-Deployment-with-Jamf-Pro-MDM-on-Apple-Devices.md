<p class="MsoNormal">Efficiently managing digital signage across multiple devices is crucial for businesses to ensure smooth operations and consistent updates. OptiSigns, in conjunction with a Mobile Device Management (MDM) system, offers a streamlined process for mass enrolling your devices. This guide will walk you through the steps to distribute and manage OptiSigns digital signage software using a Jamf MDM system on Apple devices.</p>
<hr>
<p class="undefined">In this article:</p>
<p class="undefined"><a href="#0">Requirements</a></p>
<p class="undefined"><a href="#1">Step 1: Load OptiSigns App Inside Jamf MDM</a></p>
<p class="undefined"><a href="#2">Step 2: OptiSigns App Enrollment with Jamf Pro MDM</a></p>
<p class="undefined"><a href="#3" target="_blank" rel="noopener noreferrer">Step 3: Deployment</a></p>
<p><a name="0"></a></p>
<h2 id="h_01J3NQJJCG7QSK6H5NMG396A3P" class="MsoNormal">Requirements</h2>
<p class="MsoNormal">To proceed with this guide, please ensure that you have:</p>
<p class="MsoNormal">1. Jamf Pro MDM account.</p>
<p class="MsoNormal">2. OptiSigns.com credentials.</p>
<p class="MsoNormal">3. Apple devices running iOS or tvOS.</p>
<p class="MsoNormal">4. Access to Apple Business Manager or Apple School Manager.</p>
<p><a name="1"></a></p>
<h2 id="h_01J3NQJ9SY7SH5WNV6BDS6Z98Y" class="undefined">Step 1: Load OptiSigns App Inside Jamf MDM</h2>
<p style="box-sizing: border-box;">Inside ABM (Apple Business Manager) volume purchase licenses of OptiSigns Digital Signage (It's free).</p>
<p style="box-sizing: border-box;">We assume that the ABM VPP account is linked to your Jamf Pro instance, otherwise, use this Jamf <a href="https://trainingcatalog.jamf.com/volume-purchasing/637880" target="_blank" rel="noopener noreferrer">Video Guide</a> to do so.</p>
<p style="box-sizing: border-box;"><span style="box-sizing: border-box;">After populating ABM apps into Jamf MDM, you should see OptiSigns Digital Signage app inside MDM Mobile Device Apps section, as shown below:</span></p>
<p style="box-sizing: border-box;"><span style="box-sizing: border-box; font-weight: bold;"><strong><img src="https://support.optisigns.com/hc/article_attachments/31703018962963" alt="chrome_QXt1erz8BI.png"></strong></span></p>
<p><a name="2"></a></p>
<h2 id="h_01J3NQP416VP5RJTNJRRG3BGEM">Step 2: OptiSigns App Enrollment with Jamf Pro MDM</h2>
<p>Before deploying the app to devices, you can preconfigure it to have your device automatically enrolled into your OptiSigns account.</p>
<ul>
<li>This is not required, but if you are managing a large number of devices, this will make the deployment much easier.</li>
</ul>
<p>To do this, navigate to the <strong>mobile device apps section</strong> in Jamf MDM → Click on the <strong>OptiSigns Digital Signage app → </strong>Select the<strong> App Configuration</strong> section → Complete the configuration as shown below:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/36280396747283" alt="chrome_xqP0Dfxy2g.png"></p>
<p>Let's go through each section of the configuration:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/36280396752915" alt="chrome_QVJc5ejA6j.png"></p>
<ol>
<li>
<strong>serialNo:</strong> Serial number of the device, you can map this to a variable from your MDM. </li>
<li>
<strong>accountId:</strong> This is your OptiSigns Account ID, you need to enter it manually.</li>
</ol>
<p>Account ID can be found inside the OptiSigns portal, by visiting the<strong> <a href="https://app.optisigns.com/app/screenManagement" target="_blank" rel="noopener noreferrer">Screens tab</a> </strong>→ Finding the screen you'd like→ Clicking <strong>Edit Screens</strong> → Click <strong>Advanced</strong> → Click <strong>More</strong> → Click on the "<strong>i</strong>" button </p>
<p><img src="https://support.optisigns.com/hc/article_attachments/31704324281107" alt="chrome_yBWo4GT2Dw.png"></p>
<p>This will open your <strong>Device Info</strong>:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/31704337896467" alt="chrome_81PqujFdUR.png"></p>
<p class="wysiwyg-indent3">3.<strong> screenName</strong> - This is the screen name that will appear on the OptiSigns portal, as shown in the screenshot below. Normally this is mapped to a variable from your MDM.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/31736820764819" alt="chrome_ffRQifJKS2.png"></p>
<p><a name="3"></a></p>
<h2 id="h_01J3NRXWRXNRTQ6JXTRYZ0189M">Step 3: Deployment</h2>
<p>After completing the app configuration, you need to define the scope in Jamf MDM. Follow the Jamf <a href="https://trainingcatalog.jamf.com/device-scope/552567" target="_blank" rel="noopener noreferrer">video guide</a>, and assign VPP within Managed Distribution:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/31704324293907" alt="chrome_QCOhneJupt.png"></p>
<p>Finally, you can check installation status in MDM:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/31704776061075" alt="chrome_nV2Lbl0MfF.png"></p>
<h3 id="h_01J40894CRK06AVBHWX34ST8C4">That's all! Congratulations!</h3>
<p>Now, you can enjoy OptiSigns Digital Signage across your Apple devices.</p>