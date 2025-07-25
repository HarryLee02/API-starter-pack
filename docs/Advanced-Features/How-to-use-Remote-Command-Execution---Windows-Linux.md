<h3 id="h_01JE99X2MZTFW2Y51C7AF5ZE3P">In this article, we'll show you how to use the OptiSigns Portal to Execute Remote Commands on your Windows and Linux Devices.</h3>
<ul>
<li><a href="#Enable">Enable Remote Command Feature on Account</a></li>
<li><a href="#Howto">How to Execute Remote Commands</a></li>
<li><a href="#Controlling">Controlling Remote Command Received by the Device</a></li>
</ul>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td class="wysiwyg-text-align-center" style="width: 100%;"><strong>NOTE</strong></td>
</tr>
<tr>
<td style="width: 100%;">In order to use this feature, you will need a <strong>Pro Plus</strong> <strong>or above plan</strong>.</td>
</tr>
</tbody>
</table>
<p>The Execute Remote Commands feature allows you to remotely manage screens running on Windows/Linux/Raspberry Pi. It allows command to be pushed remotely to individual devices or groups of devices simultaneously.</p>
<hr>
<p><a name="Enable"></a></p>
<h2 id="h_01HQ09N7AFBX6WQ0RDDW6HTJ4T">Enable Remote Command Feature on Account<strong><br></strong>
</h2>
<p>Remote Command Execution is disabled by default. To use it, it will need to be turned on. To do this, navigated to <a href="https://app.optisigns.com/app/s/preference-settings" target="_blank" rel="noopener noreferrer">the Preferences section</a> in the OptiSigns portal.</p>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td style="width: 100%;">For security reasons, <strong>only the account owner</strong> can enable or disable Remote Command Execution.</td>
</tr>
</tbody>
</table>
<p><img src="https://support.optisigns.com/hc/article_attachments/36078208093075" alt="enable/disable remote command execution how-to"></p>
<hr>
<p><a name="Howto"></a></p>
<h2 id="h_01HQ09N7AF2RS31S45C9H50TE2">How to Execute Remote Commands<strong><br></strong>
</h2>
<p>To submit the command to manage the devices remotely, you will need to go to the remote command execution console. Click <strong>Screens</strong>, then the <strong>More Options (Three Dots)</strong></p>
<p>Screens -&gt; More Options Icon -&gt; Execute Remote Commands</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/36078232655763" alt="how to get to execute remote commands console"></p>
<p>The Execute Remote Commands console can be broken down into three sections:</p>
<ul>
<li>
<strong>Section 1</strong> - Where you specify the target of the commands.</li>
<li>
<strong>Section 2</strong> - The command you want to execute.</li>
<li>
<strong>Section 3</strong> - The execution result and history.</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/36078232658323" alt="three sections of execute remote commands"></p>
<p>For section 1, there are 2 types of targets you can choose from:</p>
<ul>
<li>
<strong>Screens</strong> - You can select the screen name here, it can be one screen or multiple screens.</li>
<li>
<strong>Tags</strong> - Utilizing tags, you can execute the command on a group of devices. In the below example, the command will be submitted to all devices tagged as Windows or Raspberry Pi.</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/4408658532371" alt="remote commands tags"></p>
<p>For section 2, you can enter the command you want to execute in the text box. The command needs to be OS-specific, depending on the OS your device is running on, you will need to build the scripts accordingly. Once you have your commands ready, just click the submit button. The command will be pushed to the devices for execution.</p>
<p>Other than the free-form scripts, there are some common commands built into the platform, to achieve these functions, you will just need to select it from the drop-down menu. Depending on the type of device OS, the command will be submitted accordingly.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/36078208103315" alt="common remote commands"></p>
<p>After a command is executed, it will appear in section 3: the command history.</p>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td class="wysiwyg-text-align-center" style="width: 100%;"><strong>NOTE</strong></td>
</tr>
<tr>
<td style="width: 100%;">The <strong>Refresh &amp; Relaunch</strong> command can be used on any device. The <strong>Reboot Device </strong>command cannot be used on certain Android devices.</td>
</tr>
</tbody>
</table>
<hr>
<p><a name="Controlling"></a></p>
<h2 id="h_01HQ09N7AFE0JJPK7E0DTP3M7J">Controlling Remote Commands Received by the Device<strong><br></strong>
</h2>
<p>In some cases, you may not want some of your devices to be controlled remotely for any reason. The ability to receive remote commands can be toggled on the device.</p>
<p>Go to the side menu on the OptiSigns player, click <strong>Advanced Options</strong>, and you'll find the toggle for <strong>Execute Remote Commands</strong>. Toggling this off will cause the device to reject remote commands.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/36078208107539" alt="device enable remote commands toggle" width="275" height="614"></p>
<h3 id="h_01JE9AS95AFCGW37R05X7YPF9Y" class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">That's all!</h3>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self">support@optisigns.com</a></p>