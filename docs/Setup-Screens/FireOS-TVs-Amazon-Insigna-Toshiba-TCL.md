<div class="_zLbN" data-hook="post-title">
<div class="_zLbN" data-hook="post-title">
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td style="width: 100%;">
<h4 id="h_01J048YBQXZMT31KREN6SJXA9J">As of Feb 2024, FireStick and Fire TV are <strong>no longer recommended</strong> as digital signage player. This is due to <strong><a href="https://www.aftvnews.com/amazon-blocks-long-running-fire-tv-capability-breaking-popular-apps-with-no-warning-and-giving-developers-the-runaround/" target="_blank" rel="noopener noreferrer"><span class="wysiwyg-color-purple130">Amazon eliminating the ability to auto start app</span></a></strong> with FireStick &amp; Fire TVs starting FireOS 8.</h4>
</td>
</tr>
</tbody>
</table>
</div>
<div class="_zLbN" data-hook="post-title">There are workarounds with <a href="https://support.optisigns.com/hc/en-us/articles/23274673797139">ADB commands</a> or manually to start the app.</div>
<div class="_zLbN" data-hook="post-title">However, those workarounds are inconvenient, and we believe without an easy way to AutoStart apps, it is not a good solution for a Digital Signage player.</div>
</div>
<div class="_zLbN" data-hook="post-title"> </div>
<div class="_zLbN" data-hook="post-title">If you have older model of TVs with Amazon FireOS 7 or lower, you can continue with this article to get it set up.</div>
<h2 id="h_01HQF5CGES7ND3Z14HZ7XBG76T" class="rich-content-viewer_headerTwo__3f-vr rich-content-viewer_elementSpacing__208Ie blog-post-title-font _3aQMT _2J4pr css-x4x4qs rich-content-viewer_left__2p1aK _158eo _3_7DB"><strong>Here are the high level steps:</strong></h2>
<p class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB">1) Download OptiSigns Digital Signage from Amazon App Store</p>
<p class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB">2) Using OptiSigns' web portal to assign content and remotely manage your screens</p>
<p class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB">So let's dive in!</p>
<h3 id="h_01HQF5CGESVHFGWXP937D75DR6" class="rich-content-viewer_headerTwo__3f-vr rich-content-viewer_elementSpacing__208Ie blog-post-title-font _3aQMT _2J4pr css-x4x4qs rich-content-viewer_left__2p1aK _158eo _3_7DB"><strong>1) Download &amp; Set up OptiSigns Digital Signage from Amazon App Store</strong></h3>
<p class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB">Press the <strong>Search</strong> icon on the <strong>Find</strong> section of the Fire TV,</p>
<p class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB"><img src="https://support.optisigns.com/hc/article_attachments/26399157505811" alt="Fire_Stick-12.png"></p>
<p class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB">Type in "OptiSigns".<br>Fire TV Search can be tricky to use, and search as you type sometimes does not work properly.<br>After you typed "optisigns", be sure to press the menu down button until the "Optisigns" text is highlighted and then click on it.</p>
<div class="rich-content-viewer_pluginContainerReadOnly__2CvYQ rich-content-viewer_alignCenter__Slk8p _3Q5gW rich-content-viewer_sizeContent__1hD8w">
<div class="image-viewer_imageContainer__1Lhwj _34hgV">
<div class="image-viewer_imageWrapper__xdJBZ"><img src="https://support.optisigns.com/hc/article_attachments/26399157512211" alt="Fire_Stick-13.png"></div>
<div class="image-viewer_imageWrapper__xdJBZ">Click <strong>Download</strong> on the OptiSigns app icon</div>
</div>
</div>
<div class="rich-content-viewer_pluginContainerReadOnly__2CvYQ rich-content-viewer_alignCenter__Slk8p _3Q5gW rich-content-viewer_sizeContent__1hD8w">
<div class="image-viewer_imageContainer__1Lhwj _34hgV">
<div class="image-viewer_imageWrapper__xdJBZ"><img src="https://support.optisigns.com/hc/article_attachments/26399157514387" alt="Fire_Stick-14.png"></div>
</div>
</div>
<p>Once the app is installed, <strong>launch</strong> it.</p>
<p>The app will ask if you want to automatically start when device start up. It recommended to select <strong>yes</strong>, unless you want to launch the app yourself every time manually.</p>
<div class="rich-content-viewer_pluginContainerReadOnly__2CvYQ rich-content-viewer_alignCenter__Slk8p _3Q5gW">
<div class="HtmlComponent_htmlComponent__hnvPV _2sXl_">You then will see this pairing screen:</div>
</div>
<div class="rich-content-viewer_pluginContainerReadOnly__2CvYQ rich-content-viewer_alignCenter__Slk8p _3Q5gW rich-content-viewer_sizeContent__1hD8w">
<div class="image-viewer_imageContainer__1Lhwj _34hgV">
<div class="image-viewer_imageWrapper__xdJBZ"><img src="https://support.optisigns.com/hc/article_attachments/26399157527059" alt="mceclip1.png"></div>
</div>
</div>
<p class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB">Go to our website: <a class="link-viewer_link__2qJYG blog-link-hashtag-color y_1_u" href="https://app.optisigns.com/app/screenManagement" target="_self" rel="noreferrer">https://app.optisigns.com</a></p>
<p class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB">If you don't have an account already, create one, or you can also log in with Google or Facebook account.</p>
<div class="rich-content-viewer_pluginContainerReadOnly__2CvYQ rich-content-viewer_alignCenter__Slk8p _3Q5gW rich-content-viewer_sizeContent__1hD8w">
<div class="image-viewer_imageContainer__1Lhwj _34hgV">
<div class="">
<img src="https://support.optisigns.com/hc/article_attachments/26399172852627" alt="mceclip2.png">Once you logged in, click "<strong>Add screen"</strong> button</div>
<div class=""> </div>
</div>
</div>
<div class="rich-content-viewer_pluginContainerReadOnly__2CvYQ rich-content-viewer_alignCenter__Slk8p _3Q5gW rich-content-viewer_sizeContent__1hD8w">
<div class="image-viewer_imageContainer__1Lhwj _34hgV">
<div class="image-viewer_imageWrapper__xdJBZ"><img src="https://support.optisigns.com/hc/article_attachments/26399172854931" alt="mceclip3.png"></div>
<div class="">In this pop up, type in the Pair Code showing up on your Fire TV screen. Then, click <strong>Pair</strong>:</div>
<div class=""> </div>
<div class=""><img src="https://support.optisigns.com/hc/article_attachments/26399157541779" alt="mceclip4.png"></div>
</div>
</div>
<p class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB">The Fire TV screen will change to:</p>
<div class="rich-content-viewer_pluginContainerReadOnly__2CvYQ rich-content-viewer_alignCenter__Slk8p _3Q5gW rich-content-viewer_sizeContent__1hD8w">
<div class="image-viewer_imageContainer__1Lhwj _34hgV">
<div class="image-viewer_imageWrapper__xdJBZ"><img src="https://support.optisigns.com/hc/article_attachments/26399172862355" alt="mceclip5.png"></div>
</div>
</div>
<p class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB">Now you are ready to upload and assign content.</p>
<h3 id="h_01HQF5CGESWPAFDA07MF9JPTQZ" class="rich-content-viewer_headerTwo__3f-vr rich-content-viewer_elementSpacing__208Ie blog-post-title-font _3aQMT _2J4pr css-x4x4qs rich-content-viewer_left__2p1aK _158eo _3_7DB"><strong>2) Using OptiSigns's web portal to assign content and remotely manage your screens</strong></h3>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2p1aK _2R0Lu _2Dym_">Once you go to our portal at: <a class="_2qJYG blog-link-hashtag-color _3sz0l" href="https://app.optisigns.com/" target="_blank" rel="noopener noreferrer">https://app.optisigns.com/ </a>to pair the screen and start assigning content to it, you can follow these guides for more detailed steps:</p>
<ul>
<li class="undefined"><a href="https://support.optisigns.com/hc/en-us/articles/360016374813" target="_blank" rel="noopener noreferrer">Set up &amp; add a screen</a></li>
<li class="undefined"><a href="https://support.optisigns.com/hc/en-us/articles/360016247974">How to Upload &amp; Manage Your Files/ Assets</a></li>
<li class="undefined"><a href="https://support.optisigns.com/hc/en-us/articles/28295104605843">How to Create &amp; Use Playlists</a></li>
<li class="undefined"><a href="https://support.optisigns.com/hc/en-us/articles/360016981853">Create and Using Schedules with OptiSigns</a></li>
</ul>
<div class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color"> </div>
<p class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB">If you have feedback on how to make the how-to guides better, please let us know at: <a class="link-viewer_link__2qJYG blog-link-hashtag-color y_1_u" href="mailto:support@optisigns.com" target="_top" rel="noreferrer">support@optisigns.com</a></p>
<p class="rich-content-viewer_text__XzvDs rich-content-viewer_elementSpacing__208Ie _3_7DB blog-post-text-font blog-post-text-color rich-content-viewer_left__2p1aK _158eo _3_7DB"> </p>