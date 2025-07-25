<h3 id="h_01JH3P7R5TTEBSXDRFVQBH6SR9">In this article, we'll cover how to get OptiSigns running on devices running Linux.</h3>
<ul>
<li><a href="#Download">Download the OptiSigns AppImage</a></li>
<li><a href="#AnyLinux">Installing OptiSigns on Linux Distributions</a></li>
<li>
<a href="#24.04">Additional Instructions for Ubuntu 24.04 or Later</a><br>
<ul>
<li><a href="#libfuse2">Install libfuse2 Library to Support AppImage</a></li>
<li><a href="#AutoStart">Enabling AutoStart</a></li>
<li><a href="#Acceleration">Enabling Video Hardware Acceleration Using MPV Player</a></li>
</ul>
</li>
</ul>
<p>The OptiSigns Player app can be installed on any Linux machine and used as a player for your digital signs.</p>
<p>OptiSigns app is packaged as AppImage and will run on all major Linux Distribution: Ubuntu, Debian, CentOS, Red Hat, Arch Linux, etc.</p>
<hr>
<p><a name="Download"></a></p>
<h2 id="h_01JH3PDPXMMRNKR6ZSJYTPXZFC">Download the OptiSigns AppImage</h2>
<p>To install OptiSigns on Linux, you'll need:</p>
<ul>
<li>The AppImage for Linux PCs: <a href="https://links.optisigns.com/linux-32" target="_blank" rel="noopener noreferrer"><strong>32 bit (x86)</strong></a> | <strong><a href="https://links.optisigns.com/linux-64" target="_blank" rel="noopener noreferrer">64 bit (x64)</a></strong>
</li>
<li>For ARM Processors: <a href="https://links.optisigns.com/rpi" target="_blank" rel="noopener noreferrer"><strong>32 bit</strong></a> | <a href="https://links.optisigns.com/arm64" target="_blank" rel="noopener noreferrer"><strong>64 bit</strong></a>
</li>
</ul>
<hr>
<p><a name="AnyLinux"></a></p>
<h2 id="h_01JH412HZPPQAZY50DKPGWZJN3">Installing OptiSigns on any Linux Machine</h2>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2p1aK _2R0Lu _2Dym_">Once you've got the latest AppImage downloaded on your system, locate it wherever it's been downloaded.</p>
<div class="q2uC4">
<div class="_2CvYQ Slk8p _1K2V0 _1K2V0 _1hD8w">
<div class="_1Lhwj _2SZw6 image-container" data-hook="imageViewer">
<div class="xdJBZ"><img src="https://support.optisigns.com/hc/article_attachments/37230635291283" alt="optisigns appimage linux"></div>
<div class="xdJBZ">Right click on the AppImage and select <strong>Properties</strong>.</div>
<div class="xdJBZ"><img src="https://support.optisigns.com/hc/article_attachments/37230646236179" alt="appimage properties"></div>
<div class="xdJBZ"></div>
</div>
</div>
</div>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2p1aK _2R0Lu _2Dym_">In the Properties box, ensure the Permissions are set to <strong>Read &amp; Write</strong> and the "Executable as Program" slider is <strong>On</strong>.</p>
<p class="undefined"><img src="https://support.optisigns.com/hc/article_attachments/37230646238995" alt="optisigns appimage properties menu"></p>
<p class="undefined">We're not done. Before we can launch the application, we'll need to configure the proper libraries.</p>
<div class="xdJBZ">Now return to where your AppImage is stored and double click it. If you are running certain distributions that does not come with libfuse2, you will need <a href="#24.04">an additional step</a>.</div>
<div class="xdJBZ">You'll be asked to confirm Install, hit <strong>Yes</strong>.</div>
<div class="xdJBZ"><img src="https://support.optisigns.com/hc/article_attachments/37230646240915" alt="install linux appimage window"></div>
<div class="xdJBZ">
<div class="xdJBZ">The app will run in full screen mode and generate a pairing code for you to pair with the <a class="_2qJYG blog-link-hashtag-color _3sz0l" style="background-color: #ffffff;" href="http://app.optisigns.com/" target="_top" rel="noopener"><u class="sDZYg">app.optisigns.com</u></a> portal. If you move the mouse around, you will see the top 3 buttons to <strong>resize</strong>, <strong>open</strong> <strong>side bar menu,</strong> or <strong>close</strong> the app.</div>
<div class="xdJBZ">
<div class="q2uC4">
<div class="_2CvYQ Slk8p _1K2V0 _1K2V0 _1hD8w">
<div class="_1Lhwj _2SZw6 image-container" data-hook="imageViewer">
<div class="xdJBZ"><img class="_1Fjtc _2lDdg" src="https://static.wixstatic.com/media/e48f7f_3ee0de008d8b4f038c0de10250e80749~mv2.png/v1/fill/w_925,h_522,al_c,q_90,usm_0.66_1.00_0.01/e48f7f_3ee0de008d8b4f038c0de10250e80749~mv2.webp" alt="optisigns player pair code" data-pin-url="https://www.optisigns.com/post/using-raspberry-pi-as-digital-signage-player-with-optisigns" data-pin-media="https://static.wixstatic.com/media/e48f7f_3ee0de008d8b4f038c0de10250e80749~mv2.png/v1/fit/w_1397,h_788,al_c,q_80/file.png"></div>
</div>
</div>
</div>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2p1aK _2R0Lu _2Dym_">On the side menu, you can set Orientation, etc. The app will have the AutoStart and Fullscreen on Startup features checked as default. However, more setup is needed if you'd like the app to AutoStart.</p>
<div class="q2uC4">
<div class="_2CvYQ Slk8p _1K2V0 _1K2V0 _1hD8w">
<div class="_1Lhwj _2SZw6 image-container" data-hook="imageViewer">
<div class="xdJBZ"><img class="_1Fjtc _2lDdg" src="https://static.wixstatic.com/media/e48f7f_2fc697a5f1224304b2a6b23835a38355~mv2.png/v1/fill/w_925,h_518,al_c,q_90,usm_0.66_1.00_0.01/e48f7f_2fc697a5f1224304b2a6b23835a38355~mv2.webp" alt="optisigns player side menu" data-pin-url="https://www.optisigns.com/post/using-raspberry-pi-as-digital-signage-player-with-optisigns" data-pin-media="https://static.wixstatic.com/media/e48f7f_2fc697a5f1224304b2a6b23835a38355~mv2.png/v1/fit/w_1402,h_785,al_c,q_80/file.png"></div>
<hr>
<a name="24.04"></a>
<h2 id="h_01JH6F9BZ00S6CQS70C927TJAC" class="xdJBZ">Installing OptiSigns on Ubuntu v. 24.04 or Later</h2>
<p>Ubuntu v. 24.04 introduced some changes which will require some additional steps to get OptiSigns working properly.</p>
<p>First, follow <a href="https://support.optisigns.com/hc/en-us/articles/37162616928659#24.04">all the instructions above</a>. Next, you'll need to download the libfuse2 driver.</p>
<a name="libfuse2"></a>
<h3 id="h_01JH6N6ZT0V4T24MRNDV1KGP1C">Install libfuse2 Library to Support AppImage</h3>
<p class="undefined">To do this, open your <strong>Terminal </strong>and type:</p>
<pre class="undefined">sudo apt install libfuse2</pre>
<p><img src="https://support.optisigns.com/hc/article_attachments/37230646245011" alt="linux terminal libfuse2 install command"></p>
<p>The necessary libraries will automatically install, and now the OptiSigns AppImage can be launched.</p>
<p>Now, there are a few optional things you can do to further optimize OptiSigns on Ubuntu 24.04 or later, including:</p>
<ul>
<li>Enabling AutoStart</li>
<li>Enabling Video Hardware Acceleration via MPV Player</li>
</ul>
<p>These are completely optional, but helpful for your experience.</p>
<a name="AutoStart"></a>
<h3 id="h_01JH5T2TQ5PBDDBDVSMMG0ZPQ8" class="xdJBZ">Enabling AutoStart</h3>
<p>To enable AutoStart, we will need to alter the startup configuration on Ubuntu. To do this, we'll be setting up a shell script to run independently. This can be easily accomplished in around two minutes via Startup Applications Preferences.</p>
<p>Open up <strong>Startup Application Preferences</strong> and you should see something like this:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37230635312147" alt="linux startup programs"></p>
<p>The issue here is that the OptiSigns Digital Signage will not work after repeated startups. To get it working, hit <strong>Add.</strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37230635315091" alt="linux startup add program"></p>
<p>Name the file whatever you please and input any Comment you want. The <strong>Command: </strong>line is what's important here: put the same path as the basic OptiSigns autostart program, but add:</p>
<pre>--no-sandbox</pre>
<p>To the end of the command.</p>
<p>Once this is done, your player will continually autostart with each boot. You can delete the old OptiSigns startup script if you wish.</p>
<a name="Acceleration"></a>
<h3 id="h_01JH6JCTJS4634GGXBGHCCQ0JR">Enabling Video Hardware Acceleration via MPV Player</h3>
<p>In certain situations, Linux running Ubuntu 24.04 or later can struggle to play multiple or very high quality videos using the OptiSigns player.</p>
<p>In these situations, we recommend a very simple set of commands that should fix the issue.</p>
<p>First, if you're <strong>using an Intel processor, </strong>you'll need to download the proper drivers. Type this into the Terminal:<span style="color: #1d1c1d; font-family: Slack-Lato, Slack-Fractions, appleLogo, sans-serif; font-size: 15px; font-style: normal; font-variant-ligatures: common-ligatures; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: #f8f8f8; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;"></span></p>
<pre>sudo apt install intel-media-va-driver-non-free</pre>
<p>Next, you'll need to install MPV Player with this command:</p>
<pre>sudo apt install mpv</pre>
<p>Last, you'll want to hide the taskbar and top bar in the player. You'll need to input this command in order to get started:</p>
<pre>sudo apt install gnome-shell-extension-manager</pre>
<p>From here, head to <strong>Settings. </strong>Go to <strong>Ubuntu Desktop</strong>, and make sure <strong>Auto-hide the Dock</strong> is switched to ON.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37230646253459" alt="linux settings auto hide dock" width="478" height="310"></p>
<p>Next, open up the Extension Manager. Here, click <strong>Browse</strong>, then search for the "Hide Top Bar" extension. Click <strong>Install</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37230893391763" alt="linux extension manager hide top bar" width="529" height="401"></p>
<p>Now your video hardware acceleration should be enabled.</p>
<h3 id="h_01JH6JSJME1R603B11FE7ZXHKS"><strong>That's all!</strong></h3>
</div>
</div>
</div>
</div>
</div>
<div class="q2uC4">
<div class="_2CvYQ Slk8p _1K2V0 _1K2V0 _1hD8w">
<div class="_1Lhwj _2SZw6 image-container" data-hook="imageViewer">
<div class="xdJBZ">
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2p1aK _2R0Lu _2Dym_">You now can go to our portal at: <a class="_2qJYG blog-link-hashtag-color _3sz0l" href="https://app.optisigns.com/" target="_blank" rel="noopener noreferrer">https://app.optisigns.com/ </a>to pair the screen and start assigning content to it. For detail steps to get your screens started, please follow these guides:</p>
<ul>
<li class="undefined"><a href="https://support.optisigns.com/hc/en-us/articles/360016374813" target="_blank" rel="noopener noreferrer">Set up &amp; add a screen</a></li>
<li class="undefined"><a href="https://support.optisigns.com/hc/en-us/articles/360016247974">How to Upload &amp; Manage Your Files/ Assets</a></li>
<li class="undefined"><a href="https://support.optisigns.com/hc/en-us/articles/28295104605843">How to Create &amp; Use Playlists</a></li>
<li class="undefined"><a href="https://support.optisigns.com/hc/en-us/articles/360016981853">Create and Using Schedules with OptiSigns</a></li>
</ul>
<p>If you have feedback on how to make the how-to guides better, please let us know at: <a class="link-viewer_link__2qJYG blog-link-hashtag-color y_1_u" href="mailto:support@optisigns.com" target="_top" rel="noreferrer">support@optisigns.com</a></p>
</div>
<div class=""> </div>
</div>
</div>
</div>