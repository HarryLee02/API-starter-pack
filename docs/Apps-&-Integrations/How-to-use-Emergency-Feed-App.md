<p>Some Emergency Alert Systems or Emergency Mass Notification Systems do push out RSS feeds.</p>
<p>Using OptiSigns Emergency Feed app, you can have OptiSigns listen to an RSS feed, filter for certain types of messages, and target locations, and if there's matching content, it will take over screens to display emergency messages.</p>
<p>When the emergency is over, the feed returns blank, or no more matching content. OptiSigns will return to playing signage content as usual.</p>
<p> </p>
<p class="wysiwyg-text-align-center"><img src="https://signagecloud-prd.s3.amazonaws.com/editor/5f1595d6020cce00136d5164/f37643a3bef24cb59f514684aa518c3d_5f1595d6020cce00136d5164.jpg"></p>
<p> </p>
<h2 id="h_01HN20CVTEXXVHRP4Q9PFPTTP3" class="rich-content-viewer_headerTwo__3f-vr rich-content-viewer_elementSpacing__208Ie blog-post-title-font _3aQMT _2J4pr css-x4x4qs rich-content-viewer_left__2p1aK _158eo _3_7DB"><strong>Let's jump in and get started:</strong></h2>
<p class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB">First, you will need to have your screens set up and paired. For more information on how to do that, click <a class="link-viewer_link__2qJYG blog-link-hashtag-color y_1_u" href="https://www.optisigns.com/blog/how-to-set-up-digital-signs-with-optisigns-and-amazon-fire-tv" target="_blank" rel="noopener noreferrer">here</a>.</p>
<p class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB">Then log on to our portal: <a class="link-viewer_link__2qJYG blog-link-hashtag-color y_1_u" href="http://app.optisigns.com/" target="_top" rel="noreferrer">http://app.optisigns.com/</a></p>
<p class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB">Go to Files/Assets, Click on "App"</p>
<div class="rich-content-viewer_pluginContainerReadOnly__2CvYQ rich-content-viewer_alignCenter__Slk8p _3Q5gW rich-content-viewer_sizeContent__1hD8w">
<div class="image-viewer_imageContainer__1Lhwj _34hgV">
<div class="image-viewer_imageWrapper__xdJBZ wysiwyg-text-align-center"><img src="https://support.optisigns.com/hc/article_attachments/29815774668947"></div>
<div class="image-viewer_imageWrapper__xdJBZ"> </div>
<div class="image-viewer_imageWrapper__xdJBZ">Click Emergency Feed:</div>
<div class="image-viewer_imageWrapper__xdJBZ wysiwyg-text-align-center"><img src="https://support.optisigns.com/hc/article_attachments/29815767093395"></div>
<div class="image-viewer_imageWrapper__xdJBZ"> </div>
<div class="image-viewer_imageWrapper__xdJBZ">Set up your Emergency Feed app:</div>
<div class="image-viewer_imageWrapper__xdJBZ wysiwyg-text-align-center"><img src="https://support.optisigns.com/hc/article_attachments/29815776944787"></div>
<div class="image-viewer_imageWrapper__xdJBZ wysiwyg-text-align-left"> </div>
<div class="image-viewer_imageWrapper__xdJBZ wysiwyg-text-align-left">
<ul>
<li class="rich-content-viewer_elementSpacing__208Ie">
<strong><u>Name</u></strong>: Name of your assets, this will not be displayed on the screens.</li>
<li>
<strong><u>Target</u>:</strong> Select Screens or Tags.</li>
<li>
<u><strong>Screens/Tags</strong>:</u> Select which screens or group of screens (tags) you want to target for this emergency. (i.e. Fire in building/location 1)</li>
<li>
<strong><span class="wysiwyg-underline">RSS URL:</span></strong> the URL of your RSS feed</li>
</ul>
<p>Advanced settings:</p>
<p class="wysiwyg-text-align-center"><img src="https://support.optisigns.com/hc/article_attachments/29815769407763"></p>
<ul>
<li class="rich-content-viewer_elementSpacing__208Ie">
<span class="wysiwyg-underline"><strong>Using Text Font, Color, Background Color, Text Alignment, and Background Image</strong></span>, you can design the message as you desire (i.e. text shows up in the middle of the screen on top of your organization's branded image template)</li>
<li class="rich-content-viewer_elementSpacing__208Ie">
<strong><span class="wysiwyg-underline">Title Tag:</span></strong> Message title from the RSS XML feed, default is &lt;title&gt; - you can change if your feed is different</li>
<li>
<span class="wysiwyg-underline"><strong>Description Tag</strong>:</span> Message content from the RSS XML feed, default is &lt;description&gt; - you can change if your feed is different</li>
<li>
<strong><span class="wysiwyg-underline">Location (Screen Tags):</span> </strong>Some RSS can pass locations tag (i.e. emergency in a certain location only) default tag is &lt;location&gt; - you can change it if your feed is different</li>
<li>
<span style="box-sizing: border-box; text-decoration: underline;"><strong style="box-sizing: border-box;">Filter content containing:</strong></span><span> </span>you can filter content based on specific words in the title or description. I.E: "fire", so if any title or description contains the word "fire" (non-case insensitive), the app will trigger the screen takeover.</li>
<li>
<span style="box-sizing: border-box; text-decoration: underline;"><strong style="box-sizing: border-box;">Exclude title containing:</strong></span><span> </span>this filter will only apply to the title. You can hide all the old feeds by filtering with specific words in the title. I.E: “All Clear”, so after the emergency is gone, all the feeds before this title will be hidden, then the screen will revert to the original content or just display the new content after that.</li>
<li>
<strong><span class="wysiwyg-underline">Check RSS feed every:</span></strong> default is 10s</li>
</ul>
<p> </p>
</div>
<div class="image-viewer_imageWrapper__xdJBZ wysiwyg-text-align-left">
<div class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color">Click Save.</div>
<div class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color"> </div>
<div class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color">After Saving, the app will start listening to the RSS feed, if the condition matches based on your settings, all will take over the screens you targeted and display the emergency messages from the RSS feed.<br><br>
</div>
<p>If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self">support@optisigns.com</a></p>
</div>
<div class="image-viewer_imageWrapper__xdJBZ wysiwyg-text-align-left"> </div>
<div class="image-viewer_imageWrapper__xdJBZ wysiwyg-text-align-left"> </div>
</div>
</div>