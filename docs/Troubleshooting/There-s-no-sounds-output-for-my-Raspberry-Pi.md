<p>Make sure you setting audio out to the right output.</p>
<p><strong>Solution 1:</strong></p>
<p>To change audio output, right click on the audio icon and select the output.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/360061945813" alt="mceclip1.png"></p>
<p>If you are using Raspberry Pi 4, as of 3/12/2020 there's some know issues output audio to both HDMI ports. Use the port next to the power input, it works.</p>
<p><strong>Solution 2:</strong></p>
<p>Open the <strong>Terminal,</strong> run command line, use this command to switch the audio output to HDMI:</p>
<pre><code>amixer cset numid=3 2</code></pre>
<p>If output is set to <code>2</code>, which is HDMI.  Output to <code>1</code> is analogue (headphone jack). Default setting is <code>0</code> is automatic.</p>
<p><strong>Solution 3:</strong></p>
<p>Open the <strong>Terminal,</strong> run command line.</p>
<pre>sudo raspi-config</pre>
<p><img src="https://support.optisigns.com/hc/article_attachments/8571021810579" alt="mceclip6.png" width="500" height="339"></p>
<p>Select <strong>System Options</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/8570979748499" alt="mceclip1.png"></p>
<p>Select <strong>Audio</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/8570950798611" alt="mceclip2.png"></p>
<p>Select <strong>0HDMI</strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/8570985894931" alt="mceclip3.png"></p>
<p>Then select <strong>Finish</strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/8570984227731" alt="mceclip4.png"></p>
<p>After that, run reboot in the command to reboot your Raspberry Pi</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/8570988279571" alt="mceclip5.png"></p>
<p> </p>
<p>If you have feedback on how to make the how-to guides better, please let us know at: <a class="link-viewer_link__2qJYG blog-link-hashtag-color y_1_u" href="mailto:support@optisigns.com" target="_top" rel="noreferrer">support@optisigns.com</a></p>
<p> </p>