<h4 id="h_01HPZPRK63TC3GV8QZD1DZ6A0Y" class="modal-title">Nowadays, RTSP Camera Streaming is popular. You can display your RTSP Stream on your Digital Screen via OptiSigns.<br><img src="https://support.optisigns.com/hc/article_attachments/8098888117779" alt="Support_article_-2.png">
</h4>
<p>This article will guide you through how to create and use the RTSP Stream app on Windows or Raspberry Pi. Note: For this feature, you must run OptiSigns player version 5.3.2 or newer on your devices. You can download the latest version of the app at <a href="http://www.optisigns.com/download" target="_blank" rel="noopener noreferrer">https://www.optisigns.com/download</a></p>
<p>If you want to use the Fire Stick or Android Stick to display the RTSP Stream app. The setup will be different. You can click <a href="https://support.optisigns.com/hc/en-us/articles/8098889840531" target="_self">here</a>.</p>
<p>Windows and Raspberry Pi don't support the RTSP HTML5 directly. Before you create the RTSP Stream app, you will need to transcode RTSP to HTTP. Then you can implement RTSP live streaming on the Windows and Raspberry Pi devices. The easy way of achieving RTSP HTML5 playback on Windows and Raspberry Pi is to embed VLC into the HTML5 webpage and adopt it as an HTML5 RTSP player.</p>
<h3 id="h_01HPZPRK648ZSZ61JPMJD1XAFQ" class="rich-content-viewer_headerTwo__3f-vr rich-content-viewer_elementSpacing__208Ie blog-post-title-font _3aQMT _2J4pr css-x4x4qs rich-content-viewer_left__2p1aK _158eo _3_7DB"><strong>Let's jump in and get started:</strong></h3>
<h4 id="h_01HPZPRK64KR24P1VEJN4QS88V" class="rich-content-viewer_headerTwo__3f-vr rich-content-viewer_elementSpacing__208Ie blog-post-title-font _3aQMT _2J4pr css-x4x4qs rich-content-viewer_left__2p1aK _158eo _3_7DB"><strong>1. How to use it on Windows and Raspberry Pi devices.</strong></h4>
<p>Before setting up, you will need to prepare:</p>
<ol>
<li>Need the VLC Media Player. You can download it <a href="https://www.videolan.org/vlc/index.html" target="_self">here</a>.</li>
<li>RTSP URL. (Here is an example: rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4)</li>
</ol>
<p>Then you can follow these steps to set it up.</p>
<p>Step 1. Launch VLC Media Player, go to the "<strong>Media</strong>" &gt; <strong>Open Network Stream</strong></p>
<p class="wysiwyg-text-align-center"><img src="https://support.optisigns.com/hc/article_attachments/8066835391379" alt="mceclip2.png" width="591" height="440"></p>
<p>Step 2. Go to the "<strong>Network</strong>", type in the RTSP URL to the "<strong>Network URL</strong>". We use this as a sample example. (rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4)</p>
<p class="wysiwyg-text-align-center"><img src="https://support.optisigns.com/hc/article_attachments/8066888364051" alt="mceclip4.png" width="601" height="388"></p>
<p>Step 3. Click the dropdown and select "<strong>Stream</strong>".</p>
<p class="wysiwyg-text-align-center"><img src="https://support.optisigns.com/hc/article_attachments/8066876184211" alt="mceclip6.png" width="600" height="462"></p>
<p>Step 4. Click "<strong>Next</strong>"</p>
<p class="wysiwyg-text-align-center"><img src="https://support.optisigns.com/hc/article_attachments/8066895761171" alt="mceclip7.png" width="601" height="392"></p>
<p class="wysiwyg-text-align-left">Step 5. Select "<strong>HTTP</strong>", and Click "<strong>Add</strong>"</p>
<p class="wysiwyg-text-align-center"><img src="https://support.optisigns.com/hc/article_attachments/8066948003603" alt="mceclip8.png" width="601" height="394"></p>
<p>Step 6. Type "<strong>9999</strong>" in the "<strong>Port</strong>" and "<strong>/stream.ogv</strong>" in "<strong>Path</strong>". The address of the output stream will be the IP address of "your native server/stream.ogv". Click "<strong>Next</strong>" to proceed.</p>
<p class="wysiwyg-text-align-center"><img src="https://support.optisigns.com/hc/article_attachments/8099130145555" alt="mceclip2.png" width="601" height="392"></p>
<p>Step 7. Select "<strong>Video-Theora+Vorbis (OGG)</strong>". Then click "<strong>Next</strong>"</p>
<p class="wysiwyg-text-align-center"><img src="https://support.optisigns.com/hc/article_attachments/8066996433683" alt="mceclip11.png" width="601" height="395"></p>
<p>Step 8. Check the output media codec at "Generated stream output string", make sure <strong>vcodec=theo </strong>and <strong>mux=ogg,</strong> otherwise manually modify. Then, click "<strong>Stream</strong>".</p>
<p class="wysiwyg-text-align-center"><img src="https://support.optisigns.com/hc/article_attachments/8067037167379" alt="mceclip12.png" width="600" height="389"></p>
<p>When it is successful, it will start the run. You can see the screenshot below.</p>
<p class="wysiwyg-text-align-center"><img src="https://support.optisigns.com/hc/article_attachments/8099117325203" alt="mceclip1.png" width="606" height="455"></p>
<h4 id="h_01HPZPRK64EJNDA5BJ302JATPX"><strong>2. Now it's time to create the RTSP stream app in OptiSigns Web Portal. </strong></h4>
<p>Note: Keep VLC running for constantly transcoding, and embedding RTSP stream HTML5 webpage.</p>
<p class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB">Go to Files/Assets, Click on "App", search for, and add the RTSP Stream app to your Account.</p>
<p class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB"><img src="https://support.optisigns.com/hc/article_attachments/8066535317907" alt="mceclip0.png"></p>
<p class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB">Enter your RTSP Stream App information:</p>
<h2 id="h_01HPZPRK64SM5TGZE4H9ZNAC2N" class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB wysiwyg-text-align-center"><img src="https://support.optisigns.com/hc/article_attachments/8099235015571" alt="mceclip3.png" width="600" height="376"></h2>
<ul>
<li class="rich-content-viewer_elementSpacing__208Ie">
<u>Name</u>: Name of your RTSP Stream app, this is the name of the app in your asset list. It will <u><strong>not</strong></u> be displayed on your screens.</li>
<li class="rich-content-viewer_elementSpacing__208Ie">
<span class="wysiwyg-underline">URL</span>: the URL link will be your local IP address with your setup. (http://[Your IP address]:[Port]/[path])</li>
</ul>
<p>Click Save to save your asset.</p>
<h2 id="h_01HPZPRK64RSTM6HMM6QENR1Q8" class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB">That's all!</h2>
<p>Congratulation! You have created your RTSP Stream App. Then you can assign it to your Windows or Raspberry Pi device.</p>
<p class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB">You can change the wall at any time by clicking on it in the Files/Assets tab.</p>
<p class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB">You can put the walls in a Playlist, Schedule too.</p>
<p class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB"> </p>
<p class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB">If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self" rel="undefined">support@optisigns.com</a></p>