<p>With OptiSigns, you can show the Live TV from your cable TV services (such as Xfinity, DirectTV) on your screens. There are 2 ways you can do it with OptiSigns.</p>
<ul>
<li>If you are using a windows player and just need to show it on a single screen, you can follow the HDMI Video Input approach and use the Live TV app to achieve it. You can refer to <a href="https://support.optisigns.com/hc/en-us/articles/1500002042241" target="_self" rel="undefined">this article</a> for more details.</li>
<li>If you would like to broadcast to more than one screen and use any media players, you can follow this document and use the video streaming app to achieve it. </li>
</ul>
<p>Video streaming app is used to subscribe to the live streams transferred through HTTP, such as HLS, DASH. HTTP is widely used for the internet data transfer, it is supported well on almost all the platforms, such as Windows, Linux, Android, etc. To stream Live TV, you will need to get a HDMI Video Encoder to convert the Live TV to a HLS stream, such as this <a href="https://a.co/d/ezieSsp" target="_self">URayCoder HDMI Video Encoder</a>. Then the video streaming app can be used to show the Live TV on your screens, and you can use the same HLS stream on multiple screens as long as they are in the same network.  </p>
<p>In this document, we will walk through how to show the Live TV using the video streaming app. It consists of 3 steps at high level.</p>
<ol>
<li>Set up the HDMI Video Encoder.</li>
<li>Create the video streaming app</li>
<li>Put the Live TV on your Screen</li>
</ol>
<p>If you have an IPTV system in place which supports HLS already, you can skip step 1 and set up the video streaming app to put it on your screens directly. </p>
<p> </p>
<p><span class="wysiwyg-font-size-x-large"><strong>1. Set up the HDMI Video Encoder</strong></span></p>
<p>The HDMI Video Encoder has an admin console to manage the configuration and settings. Depending on the encoder you use, you will need to access it differently. Please follow the instructions of the HDMI Video Encoder to access the admin console. For the UrayCoder HDMI Video Encoder, the default IP address to access the admin console is 192.168.1.168</p>
<p>Once in the admin console, please go to the setting page to configure the video stream to be used. In this case, we will need to make sure the HLS stream is enabled, the rest of the streams can be disabled.  </p>
<p><img src="https://support.optisigns.com/hc/article_attachments/10158743969939" alt="mceclip1.png"></p>
<p>Click Apply after the change, then you will be able to see the URL to use for the HLS stream from the status page.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/10158882063635" alt="mceclip2.png"></p>
<p><span class="wysiwyg-font-size-x-large"><strong>2. Create the video streaming app</strong></span></p>
<p>Go to asset-&gt;app section to create a video stream app. Simply put the HLS stream URL of the HDMI video encoder in the video streaming app, then it will be available for use. You can refer to <a href="https://support.optisigns.com/hc/en-us/articles/8369526604435" target="_self">this article</a> for more information about the video streaming app. </p>
<p>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/10158846152467" alt="mceclip3.png"></p>
<p><span class="wysiwyg-font-size-x-large"><strong>3. Put the Live TV on your screens</strong></span></p>
<p>Now the video streaming app is available for use, you can assign it to any screens you want to show the Live TV. Please make sure that the screens need to be in the same network as the HDMI video encoder, so that the HLS stream is accessible by your screens. For more information on how to assign content to the screens, you can refer to <a href="https://support.optisigns.com/hc/en-us/articles/360016375153" target="_self">this article</a>.</p>
<p>You can also put it in the splitscreen app, then you will be able to have other information to show together with the Live TV. You can refer to <a href="https://support.optisigns.com/hc/en-us/articles/360026559573" target="_self">this article</a> for more details on how to setup multiple screen zones.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/10159027869971" alt="mceclip3.png"></p>
<p> </p>
<h3 id="h_01HPZMKYR5QF1QZSMGYSJC12G1" class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB"><strong>That's all! Congratulation!</strong></h3>
<p>If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self" rel="undefined">support@optisigns.com</a> </p>