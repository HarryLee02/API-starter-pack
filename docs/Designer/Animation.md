<h3 id="h_01JY4CW76E44XAXCH20S0VEPJW"><span style="color: #434343;">In this article, we’ll go over how to add Animations to any part of your design.</span></h3>
<ul>
<li>
<a href="https://support.optisigns.com/hc/en-us/articles/undefined#AddAnimations">How to Add Animations to Design Elements</a><ul>
<li><a href="#PageAnimations">Page Animations</a></li>
<li><a href="#ObjectAnimations">Object Animations</a></li>
</ul>
</li>
<li>
<a href="#CommonIssues">Common Issues with Animations</a><ul>
<li><a href="#PreloadingAssets">Preloading Assets to a Playlist</a></li>
<li><a href="#DevicePerformance">Device Performance</a></li>
</ul>
</li>
</ul>
<p>Animations are an effective way to display promotions, announcements, and messages. They draw the human eye with motion, causing people to naturally look toward its source. With Designer, it’s easy to add animations to your designs, bringing them more attention from visitors.</p>
<p>For an intro to using Designer, see our article on <a href="https://support.optisigns.com/hc/en-us/articles/42087942047379-Getting-Started-with-Designer" target="_blank" rel="noopener noreferrer"><strong>Getting Started with Designer</strong></a>.</p>
<hr><p><a name="AddAnimations"></a></p>
<h2 id="h_01JY4CW76T0WGBJ2PGY2YY6J8V">How to Add Animations to Design Elements</h2>
<p>Selecting the <strong>Animate </strong>button will allow you to add animations to your design elements.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42305104951699" width="624" height="45"></p>
<p>This button is also available per element.</p>
<p>Clicking it will open the <strong>Animate </strong>area on the Side Menu:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42305104952851" width="337" height="199"></p>
<p>In order to add an animation, you’ll need to select an element to animate. Then, decide whether to use a <strong>Page Animation </strong>or an <strong>Object Animation</strong>.</p>
<p>To demonstrate the differences between the two and how to best use them (together or separately), we’ll use a simple template design, like below:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42305104953619" width="624" height="352"></p>
<p><a name="PageAnimations"></a></p>
<h3 id="h_01JY4CW76Z5V7PZGDRECF5X04A"><span style="color: #434343;">Page Animations</span></h3>
<p><strong>Page Animations </strong>will animate in the order it is placed on the list. These also will animate only once, whenever the page loads.</p>
<p>For example, let’s say we want the water on our example template to fly in from the right - to give the appearance of splashing the water bottles.</p>
<p>First, select the element. Then, hit <strong>Animate → Add </strong>under the <strong>Page Animations </strong>section. This will bring up a whole mess of options:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42305100419987" width="339" height="535"></p>
<p><strong>Animation Types:</strong></p>
<ul>
<li><strong>Fade in</strong></li>
<li><strong>Fade out</strong></li>
<li><strong>Fly in from left</strong></li>
<li><strong>Fly in from right</strong></li>
<li><strong>Fly in from bottom</strong></li>
<li><strong>Fly in from top</strong></li>
<li><strong>Fly out to left</strong></li>
<li><strong>Fly out to right</strong></li>
<li><strong>Fly out to bottom</strong></li>
<li><strong>Fly out to top</strong></li>
<li>
<strong>Zoom in </strong>- Briefly zooms the element in</li>
<li>
<strong>Zoom out </strong>- Briefly zooms the element out</li>
<li>
<strong>Bounce X </strong>- Bounce the element horizontally</li>
<li>
<strong>Bounce Y </strong>- Bounce the element vertically</li>
<li><strong>Flash</strong></li>
<li>
<strong>Zoom </strong>- Alternates between zooming the element in and out</li>
<li><strong>Spin left</strong></li>
<li><strong>Spin right</strong></li>
</ul>
<p>While we could provide detailed descriptions of each of these, it’s more fun to play around with them and see how they fit your vision for yourself!</p>
<p><strong>Animation Timing:</strong></p>
<ul>
<li>
<strong>After previous </strong>- Sets the animation to trigger after the previous animation on the list.</li>
<li>
<strong>With previous </strong>- Sets the animation to trigger at the same time as the previous animation.</li>
<li>
<strong>From beginning </strong>- Sets the animation to trigger as soon as the asset loads.</li>
</ul>
<p><strong>Delay (sec) </strong>- How long of a delay between the asset loading/previous animation and the animation going off.</p>
<p><strong>Animation Speed </strong>- Changes how quickly the animation moves.</p>
<figure style="width: 100%;" class="wysiwyg-table"><table style="border-style: solid; border-width: 1px;"><tbody>
<tr><td style="border-style: solid; border-width: 1px;"><strong>NOTE</strong></td></tr>
<tr><td style="border-style: solid; border-width: 1px;">
<p>To properly utilize Animation Timing, you will need to coordinate your choice with the Delay option.</p>
<p>For example, say we have three page animations, <strong>A, B, and C</strong>.</p>
<ul>
<li>A will go first, right when the page loads. No delay is needed.</li>
<li>B is set to "After previous" in order to follow A. Setting a Delay of 1s will cause B to animate 1s <em><strong>after </strong></em>A animation ends.</li>
<li>C we want to fire at the same time as B. We select "With previous."<ul>
<li>With no delay, this will cause it to fire right as the B animation ends, causing it to look wrong.</li>
<li>To fix this, we will need to set a delay of 1s (assuming Animation Speed is also 1). This will cause C to fire 1s <em><strong>before </strong></em>the B animation ends, timing it properly.<br> </li>
</ul>
</li>
</ul>
</td></tr>
</tbody></table></figure>
<p>Once an animation is added, more can be created. The list of animations can be reordered via drag and drop:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42305104954643" width="337" height="323"></p>
<figure style="width: 100%;" class="wysiwyg-table"><table style="border-style: solid; border-width: 1px;"><tbody>
<tr><td style="border-style: solid; border-width: 1px;"><strong>NOTE</strong></td></tr>
<tr><td style="border-style: solid; border-width: 1px;">The order the Animations are dragged in does not override their timing to display. For example, if you have three animations and one is set to display "From Beginning" and you drag it to the bottom of the order, it will still display from the beginning despite being the last in order. Changing the order in the drag-and-drop will not change the Animation Timing setting.</td></tr>
</tbody></table></figure>
<p>To create the animation we want, we simply select the different water elements and have them <strong>Fly in from the right</strong>, set to <strong>From beginning </strong>so all the water comes in at once. We can test this by hitting <strong>Play</strong>:</p>
<figure class="wysiwyg-image"><img style="aspect-ratio: 2953/1465;" src="https://support.optisigns.com/hc/article_attachments/42305104955283" alt="firefox_sMTs0nNrIC.gif" width="2953" height="1465"></figure>
<p><a name="ObjectAnimations"></a></p>
<h3 id="h_01JY4CW77C2TABQKX3NVKR38MC"><span style="color: #434343;">Object Animations</span></h3>
<p><strong>Object Animations </strong>will animate simultaneously, regardless of the order they are placed in. These can also be set up to animate indefinitely (or as long as the asset is shown on the screen).</p>
<p>For example, let’s say we want our screen to stay up for quite some time (over a minute, say). For that, we’ll want to include some additional animation to make sure it doesn’t get stagnant, and to continue to draw people’s attention.</p>
<p>To do this, we’ll draw attention to the Hydration text element by creating an Object Animation.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42305104955795" width="331" height="437"></p>
<p>The Object Animations tab is similar to the Page Animations tab, with a few key differences:</p>
<p><strong>Animation Timing</strong></p>
<ul>
<li>
<strong>Delay </strong>- refers to the delay <strong>between</strong> each animation. This includes at the beginning, and on every subsequent animation</li>
<li>
<strong>End Delay </strong>- Refers to the delay <strong>inside </strong>each animation.</li>
</ul>
<p><strong>Loop</strong></p>
<ul>
<li>
<strong>Indefinitely </strong>- Continually loop the animation until the asset is changed.</li>
<li>
<strong>One Time </strong>- Play the animation upon load in one time.</li>
<li>
<strong>Iterations </strong>- Allows you to specify how many times you’d like the animation to repeat.</li>
</ul>
<figure style="width: 100%;" class="wysiwyg-table"><table style="border-style: solid; border-width: 1px;"><tbody>
<tr><td style="border-style: solid; border-width: 1px;"><strong>NOTE for Legacy Designer 1.0 Users</strong></td></tr>
<tr><td style="border-style: solid; border-width: 1px;">With the recent Designer 2.0 update, we've depreciated multiple object animations on a single element. If you have 2-3 object animations in a 1.0 design, it can still be edited in 2.0. If deleted, however, it will have to be added back in 1.0. Once Designer 1.0 is depreciated, you will only be able to edit or delete these animations.</td></tr>
</tbody></table></figure>
<p>Let’s say we want the Hydration text to bounce from side to side, but not too quickly as to be distracting or annoying.</p>
<p>We’ll set the <strong>Delay </strong>to <strong>3 seconds </strong>and then set the <strong>End Delay </strong>to <strong>3 seconds </strong>as well. This will cause the bounce to hang for that amount of time. Last, we’ll set the Loop to <strong>Indefinitely</strong>:</p>
<figure class="wysiwyg-image"><img style="aspect-ratio: 1613/789;" src="https://support.optisigns.com/hc/article_attachments/42305100424211" alt="firefox_yEpdMaig3q.gif" width="1613" height="789"></figure>
<p>Now, when we put all our animations together, we get a nice quick set of animations at the beginning thanks to our <strong>Page Animations</strong>, followed by a nice loop after thanks to our <strong>Object Animation</strong>. This can be tested with <strong>Play All </strong>or <strong>Preview</strong>:</p>
<figure class="wysiwyg-image"><img style="aspect-ratio: 1617/799;" src="https://support.optisigns.com/hc/article_attachments/42305100425363" alt="firefox_jSVIvqBZbf.gif" width="1617" height="799"></figure>
<figure style="width: 100%;" class="wysiwyg-table"><table style="border-style: solid; border-width: 1px;"><tbody>
<tr><td style="border-style: solid; border-width: 1px;"><strong>NOTE</strong></td></tr>
<tr><td style="border-style: solid; border-width: 1px;">
<p>The formula for each Object Animation iteration is as follows:</p>
<p>Delay + Animation Duration + End Delay = 1 Iteration.</p>
</td></tr>
</tbody></table></figure>
<p> </p>
<hr><p><a name="CommonIssues"></a></p>
<h2 id="h_01JY4CW77KXJ6F9JTEGS3DPMES">Common Issues with Animations</h2>
<p>Now, let’s go over a few common issues you may run into while trying to display your animations on a screen.</p>
<p><a name="PreloadingAssets"></a></p>
<h3 id="h_01JY4CW77KW3ZRHFSH9B22J095"><span style="color: #434343;">Preloading Assets in Playlist</span></h3>
<p>This feature allows a more seamless appearance by loading assets prior to showing onscreen. This lessens the likelihood of your signage hanging for a second or two as the assets are loaded.</p>
<p>OptiSigns will preload your assets 6-8 seconds prior to the asset displaying on the screen. This has the unfortunate effect of potentially skipping your animation, which will display immediately upon loading. To fix this, you can either:</p>
<ul>
<li>
<em><strong>(Recommended</strong>) </em>Add a 1-3 second delay on your animations to ensure they appear onscreen when this preloading is selected:</li>
<li>Disable Preload Assets in Playlist. However, this will show a blank screen in-between transitions.</li>
</ul>
<p><a name="DevicePerformance"></a></p>
<h3 id="h_01JY4CW77NMCQB54F2P51Q94W3"><span style="color: #434343;">Device Performance</span></h3>
<p>Running too many animations at once will affect your device’s performance and create a less-than-ideal digital signage experience.</p>
<p>In general, the degree to which this is felt will depend on your device’s performance capabilities. A Roku device, typical smart TV, Amazon FireStick, or other device not purpose built for digital signage is likely to suffer from worse issues. If using one of these devices, we recommend no more than <strong>1 or 2 animations per created asset</strong>.</p>
<p>By contrast, Windows and Linux devices or OptiSigns players can handle significantly higher loads. However, if you see stuttering while using one of these devices, we recommend limiting animations to <strong>3-4 animation per created asset</strong>.</p>
<h3 id="h_01JY4FP7AD7JFZKB3M9854NR3C"><span style="color: #434343;">That’s all!</span></h3>
<p>OptiSigns is the leader in <a href="https://www.optisigns.com/"><span class="wysiwyg-underline">digital signage software</span></a>. If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com"><span class="wysiwyg-underline">support@optisigns.com</span></a>.</p>
<p><br><br> </p>