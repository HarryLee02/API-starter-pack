<h3 id="h_01J2VSTHS10Y5M8KPCM03J87S5">How to quickly get your IoT sensors up and running on any screens you wish.</h3>
<p>In this article:</p>
<ul>
<li><a href="#Serial">Set Up Serial Communication Channel</a></li>
<li><a href="#Lift">Set Up IoT Sensor via Lift and Learn</a></li>
<li>
<a href="#assign">Assign the IoT Sensor to a Screen</a>
<ul>
<li><a href="#1">Option 1: Through Lift and Learn</a></li>
<li><a href="#2">Option 2: Through Edit Screen Menu</a></li>
</ul>
</li>
<li><a href="#Advanced">Advanced Settings</a></li>
</ul>
<table style="border-collapse: collapse; width: 61.1429%;" border="1">
<tbody>
<tr>
<td class="wysiwyg-text-align-left" style="width: 100%;">
<strong>NOTE:</strong> This feature requires the <strong>Engage plan </strong>or higher.</td>
</tr>
</tbody>
</table>
<hr>
<p class="wysiwyg-text-align-left">The OptiSigns IoT Sensor Add-on allows you to use any IoT sensors that work with serial communication to interact with your screens. You'll be able to:</p>
<ol>
<li class="wysiwyg-text-align-left">Detect and monitor sensor data about the surroundings, such as motion, temperature and humidity, object liftup/placedown. </li>
<li class="wysiwyg-text-align-left">Responsively display different content based on the sensor event that was received by the player connected to the screen.</li>
<li class="wysiwyg-text-align-left">Send command to other IoT devices to control its behavior, e.g. turn on the atmosphere light, turn on/off the screen monitor.</li>
</ol>
<p>Our YouTube video shows how it supports the lift and learn use cases using a Nexmosphere brand sensor.</p>
<p class="wysiwyg-text-align-center"><iframe src="//www.youtube-nocookie.com/embed/5W__BqfYp7o" width="560" height="315" frameborder="0" allowfullscreen=""></iframe></p>
<p class="wysiwyg-text-align-center"><em>This feature supports Windows, Linux , MacOS, BrightSigns Player, and our pre-configured Android Stick.</em></p>
<hr>
<h2 id="h_01HA92FY64Y3Z1M0P4BMW2QEXR"><strong>Quick Start Guide for OptiSigns IoT Sensor Add-on</strong></h2>
<p>For the following example, we will use a temperature sensor with an <strong>Arduino</strong> board to demonstrate how it works. <strong><em>Your board may have slightly different connection options - we will note instances where this may be the case.</em></strong></p>
<p>The temperature sensor will send data in its own format to the OptiSigns player through serial communication. The temperature data can be displayed on the screen in realtime, and when the defined condition met, the screen content will change to show overheat status. </p>
<p><img src="https://support.optisigns.com/hc/article_attachments/13110301584531" alt="mceclip0.png"></p>
<p>Setting up the IoT sensor add-on will take three steps:</p>
<ol>
<li>Set up the serial communication channel.</li>
<li>Set up IoT sensor via Lift and Learn</li>
<li>Activate the IoT sensor on the screen and assign the IoT sensor addon app to it.</li>
</ol>
<p>From there you can modify the set up to fit your need.</p>
<hr>
<p><a name="Serial"></a></p>
<h2 id="h_01HA92FY64ZCQ90ZZQMVEHWH4X"><strong>1. Set Up Serial Communication Channel</strong></h2>
<p>In the top right corner, click on the account name.</p>
<p>Then, click <strong>Personal Profile → </strong>Look to the left hand column.</p>
<p>Expand <strong>"Advanced" →</strong> <strong>"External Communications (RS232)"</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32208926824211" alt="firefox_kDKZkQZT6x.png"></p>
<p> </p>
<p><em>You can also go the the page using this link: <strong><a href="https://app.optisigns.com/app/s/external-coms" target="_blank" rel="noopener noreferrer">https://app.optisigns.com/app/s/external-coms</a></strong></em></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/13110350933139" alt="mceclip1.png"></p>
<p> </p>
<p>Click <strong>"Add New"</strong> in the <strong>Connections</strong> tab to bring up the <strong>Create New Connection</strong> page, where you can define the parameters for the serial communication.<img src="https://support.optisigns.com/hc/article_attachments/32208926832787" alt="firefox_KBKtcrjYw5.png"></p>
<table style="border-collapse: collapse; width: 84.5714%;" border="1">
<tbody>
<tr>
<td class="wysiwyg-text-align-left" style="width: 100%;">
<strong>NOTE:</strong> Most of the required settings will depend on your device. Please see your device's documentation for specific information.</td>
</tr>
</tbody>
</table>
<p>We are only going to cover three main settings off this screen: <strong>Name, COM Port, </strong>and <strong>Baud Rate.</strong></p>
<ul>
<li>
<strong>Name: </strong>A quick name for your sensor. Enter whatever you'd like.</li>
<li>
<strong>COM port: </strong>Designates which serial port the serial communication channel will enter from.<br>Please note, different systems will organize the serial port differently.
<ul>
<li>
<strong>Windows:</strong> Normally represented as "COM#". This will depend on the port you've plugged the sensor into.</li>
<li>
<strong>Linux: </strong>Normally represented as something like "/dev/ttyUSB0" or "/dev/ttyACM0".</li>
<li>
<strong>Brightsigns: </strong>Normally represented as "1" or "2"</li>
<li>
<strong>OptiSigns Preconfigured Android Sticks: </strong>Usually is "USB0"</li>
</ul>
</li>
</ul>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td class="wysiwyg-text-align-center" style="width: 100%;"><strong>NOTE</strong></td>
</tr>
<tr>
<td style="width: 100%;">
<p>You can find your COM Port by navigating to the <strong>Trigger Event Viewer </strong>page on your screen and clicking on "Show":</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42985157368979"></p>
</td>
</tr>
</tbody>
</table>
<ul>
<li>
<strong>Baud Rate: </strong>This is a device specific number. For this example, we're using a Baud rate of 9600 for the communication with Arduino board. When using Nexmosphere sensors, the baud rate is always 115200.</li>
</ul>
<p>Also note, both Arduino board and Nexmosphere controller are using USB port, please make sure the media player you use comes with USB port.</p>
<p>The other options (Data Bits, Stop Bits, Parity, Flow Controls, Receive Line Ending (EOL), Receive Encoding) are highly advanced and <strong>are best left at default</strong> unless your device specifies otherwise.</p>
<p><strong>Save</strong> the connection once the configuration is complete and then it is ready for use.</p>
<table style="border-collapse: collapse; width: 92%;" border="1">
<tbody>
<tr>
<td class="wysiwyg-text-align-left" style="width: 100%;">
<strong>NOTE:</strong> If you wish to set up custom commands to send to your sensor now, see the <strong><em>Set Up Custom Sensor Commands</em></strong> section of this guide.</td>
</tr>
</tbody>
</table>
<p> </p>
<hr>
<p><a name="Lift"></a></p>
<h2 id="h_01HA92FY6494H4TB9VZ2H29Y5C"><strong>2. Set Up IoT sensor via Lift and Learn<br></strong></h2>
<p>The IoT sensor is configured through our <strong>"Lift and Learn" </strong>builder, found under the <strong>Engage</strong> tab.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32208926838675" alt="firefox_h7cyVMoyaT.png"></p>
<p> </p>
<p>Once you've selected Lift and Learn, click <strong>Build.</strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32208910745747" alt="ZgbrWWmul3.png"></p>
<p> </p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32208910750355" alt="S0kR2qEg9y.png" width="825" height="422"></p>
<table style="border-collapse: collapse; width: 92%;" border="1">
<tbody>
<tr>
<td class="wysiwyg-text-align-left" style="width: 100%;">
<strong>NOTE:</strong> In the case of custom commands, these are often device specific. Your user manual may have several basic commands. More commands can be determined through OptiSigns; however, the rest of the setup process will need to be completed first.</td>
</tr>
</tbody>
</table>
<ul>
<li>
<strong>Name: </strong>This is an internally facing name that will help you organize your IoT devices. Type whatever you wish.</li>
<li>
<strong>Change Content: </strong>Switch between "Immediately" and a "Delay" of your choice in milliseconds.</li>
<li>
<strong>Play for at least: </strong>When triggered, the app will play the content corresponding to the play rule for as many seconds as you select here. We recommend keeping this at 3 seconds to give a smoother experience, just in case the triggering events are met frequently.</li>
<li>
<strong>Rest for: </strong>When the triggering condition is not met, the device will resume playing the content assigned to it for this number of seconds. We recommend keeping this at 3 seconds to give a smoother experience, just in case the triggering events are met frequently.</li>
<li>
<strong>Play Rules: </strong>Set content you want to play when the corresponding trigger event fires.<br>
<ul>
<li>
<strong>Effective Time: </strong>Determines the time at which the IoT sensor is active. You can select times and days of the week, or a customized schedule.</li>
<li>
<strong>If Detected: </strong>Sets the command trigger for the rule. This can be one of two preset options, or a custom command. This is a command <em>received </em>from the sensor.<br>
<ul>
<li>
<strong>Tag picked up: </strong>If something is placed on the sensor and then picked up, this will trigger the rule. This gives a Default value specifically for Nexmosphere sensors. Please see the below section<em> </em>to get the exact command for your sensor.</li>
<li>
<strong>Tag put down: </strong>If something is put down on the sensor, this will trigger the rule. This gives a Default value made for Nexmosphere sensors. Please see the below section to get the exact command for your sensor.</li>
<li>
<strong>Full Command: </strong>A custom command can be input below.</li>
</ul>
</li>
<li>
<strong>"&lt;/&gt;": </strong>A Javascript-based function where you can apply the needed logic to process the incoming command and derive the needed result. In the below example, the Ardunio board will send the temperature data from the sensor in a string, the processing rule extracts the temperature value and determine when the "TOOHOT30" custom command triggers the event.</li>
</ul>
</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/13110786060691" alt="mceclip5.png"></p>
<ul>
<li style="list-style-type: none;">
<ul>
<li>
<strong>Play Content:</strong> Determines what content plays (or stops) when trigger conditions are met. Options are "Asset," "Playlist," or "Stop Playing."</li>
<li>
<strong>Commands:</strong> Allows you to send out commands to sensors instead of just receiving them. If you're using a typical IoT sensor, <strong>you most likely won't need to use this</strong>. These are typically used for other types of devices, such as atmospheric lighting or speakers. These commands are created in the "Commands" section of the "External Communications (RS232)" section from before. We will be returning to this later in the article.</li>
<li>
<strong>Action: </strong>Allows you to move a Rule's place in the list, or delete them.</li>
</ul>
</li>
<li>
<strong>Add Rule: </strong>Allows the creation of more rules, with no maximum. These can be deleted or organized via the Action setting.</li>
</ul>
<p>We <em><strong>strongly recommend</strong></em> obtaining a string command and inputting it into the <strong>Play Rules </strong>section. This will reduce or eliminate any potential issues.</p>
<p>To do this, boot up your screen and navigate to the OptiSigns main menu. Scroll down until you see <strong>Trigger Event Viewer</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42985157371027" alt="firefox_VujXdIW6kJ(1).jpg"></p>
<p>When your sensor is properly configured, you will be able to see it mapped to a COM port. This information can be  By placing pressure on the sensor, a <strong>string </strong>will appear on the right side of your screen. By typing this <strong>case-sensitive</strong> string into your <strong>If Detected</strong> area, your issues will likely resolve.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32208926880915" alt="firefox_ISUylb5Aq5.png"></p>
<p>This is the easiest way to get these command strings for non-Nexmosphere brand sensors. You can also find these command strings by looking at your manufacturer's website.</p>
<p><br>Once you've got everything set up to your liking, hit <strong>Assign</strong> to move to the next step.</p>
<hr>
<p><a name="assign"></a></p>
<h2 id="h_01HA92FY642FRQ6E95V3PZ03EA"><strong>3. Assign the IoT Sensor Add-on app to a Screen</strong></h2>
<p>There are two options for assigning your Sensor Add-On to a screen.</p>
<p><a name="1"></a></p>
<h3 id="h_01J2VMGA6F3BTN81DFH4XGXCFT">Option 1: Through Lift and Learn</h3>
<p><img src="https://support.optisigns.com/hc/article_attachments/32208926865683" alt="firefox_vDbwOLdUam.png"></p>
<p>Once you've created the parameters for your IoT sensor, you can assign it directly to one of your screens. There are two options:</p>
<ul>
<li>
<strong>Target -</strong> Select between Screens and Tags. Selecting one or the other will change the next option to either Screens or Tags, depending on which you select here.</li>
<li>
<strong>Screens / Tags </strong>- Select which screen or tag will be associated with the sensor. This determines where your content will appear.</li>
</ul>
<p><a name="2"></a></p>
<h3 id="h_01J2VMH3W7C9G1Y6CF8KG6D5WA">Option 2: Through the Edit Screen Menu</h3>
<p>You can also assign your completed Sensor app to a screen through the <a href="https://support.optisigns.com/hc/en-us/articles/360048914673-Edit-Screen-What-does-each-option-do">Edit Screen Menu.</a></p>
<p>To get there, go to Screen Management and click Edit the screen you want to add this Add-on to.</p>
<p>Click <strong>Advanced</strong> <strong>→</strong> <strong>More</strong> <strong>→</strong> <strong>Sensor Add-on → Activate </strong>to open up more options.</p>
<p> </p>
<p><img src="https://support.optisigns.com/hc/article_attachments/13110881710611" alt="mceclip7.png"></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/13110883397907" alt="mceclip6.png"></p>
<ul>
<li>
<strong>Sensor Add-on - </strong>This is the IoT Sensor Add-on we created earlier. You can cycle through your created apps here.</li>
<li>
<strong>Sensor COM Connection </strong>- This is the serial communication channel we created in the first step. Select it here!</li>
<li>
<strong>Sensor Commands Template - </strong>This sets an external command template. If you're using an IoT sensor, you <strong>should not need to use this device</strong>.</li>
<li>
<strong>External COM - </strong>This for when you need to send a command out. Most users will want to leave this unchecked.</li>
</ul>
<p>On the screen, you should also select the standard content that should be played on the screen in the normal, in this case we use the "Heat Sensor - Normal" asset that display the standard content and also data from temperature sensor in real time.</p>
<p>Once IoT Sensor Addon is activated, you can assign the IoT sensor Add-on app that was created earlier, in this case it is called "Sensor". And also select the sensor connection that was created in the first step, in this case it is "Arduino - Win". Since we are only receiving commands from sensors, we will leave the sensor commands template as "None"</p>
<p> </p>
<hr>
<p><a name="Advanced"></a></p>
<h2 id="h_01J2W7DX9EDWXAF6T4FV94TYYZ"><strong>Advanced Settings</strong></h2>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td class="wysiwyg-text-align-center" style="width: 100%;"><strong>Use Case</strong></td>
</tr>
<tr>
<td style="width: 100%;">In special cases when you need to send commands back to external devices, such as a light source or speaker, these options are for you. These options are not needed for those using ordinary IoT sensor devices.</td>
</tr>
</tbody>
</table>
<p>First, navigate to <strong>External Communications (RS232) → </strong><strong>Add New</strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32208910780051" alt="firefox_Ormk62EJMc.png"></p>
<p>This screen will come up:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32208910797715" alt="firefox_tdPfmJaP56.png"></p>
<p>Here you'll see four options:</p>
<ul>
<li>
<strong>Name -</strong> What you'll call this command. This comes out in the form of a Tag.</li>
<li>
<strong>Encoding </strong>- The type of coding being sent to your device. Choose between "ascii" and "hex."</li>
<li>
<strong>Value </strong>- The actual command string being input. These will vary depending on use case and device.</li>
<li>
<strong>Line Ending (EOL)</strong> - The code for your line ending. Options are "None," "CR," "LF," and "CR + LF." We recommend leaving it at "None."</li>
</ul>
<p>Once you've configured your Command, press <strong>Save</strong>.</p>
<p>Next, navigate back to <strong>Lift and Learn</strong> and click on your IoT app to edit it. Click the empty box under <strong>"Commands" </strong>and you should be able to select your tag:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32208926902675" alt="firefox_SASdQOLURh.png"></p>
<p>As long as everything is configured correctly, this will allow you to send commands to external devices.</p>
<p> </p>
<hr>
<p><strong><span class="wysiwyg-font-size-x-large">That's all! </span></strong></p>
<p>Now you have completed all the needed configurations to use the IoT sensors add-on, just connect the sensors and controller to your screen(media player), then you are ready to go. In this case, the screen will play the standard content like the one on the left with real time data from the temperature sensor, and when the temperature surpasses 30 degrees in Celsius, it will trigger the overheat content on the screen like the one on the right. </p>
<p><img src="https://support.optisigns.com/hc/article_attachments/13110301584531" alt="mceclip0.png"></p>
<p>If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self">support@optisigns.com</a></p>