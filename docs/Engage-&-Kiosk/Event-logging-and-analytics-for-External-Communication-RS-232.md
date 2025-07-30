<p>With OptiSigns you can enable track of the data communication between the digital signage player and external devices through external communication (RS232). The feature is available for customers on Enterprise plan. </p>
<p>Once it is enabled, it will keep tracking of the inbound/outbound event data that was sent between the digital signage player and external devices. For example, if you are using IoT sensors, the feature can track the serial command that was sent from your sensors, and you can analyze the data to monitor and further optimize your IoT sensors usage. Or you can track the RS232 commands(power on/off, mute/unmute etc) that was sent to your TVs and use it as a proof of your compliance. </p>
<h3 id="h_01HPZKZ1D1ND0KYQ6AR5A7CJ5S"><strong>Prerequisite:</strong></h3>
<p>To use this feature, you will need to confirm in advance that the connection between your digital signage player and external devices are working properly. </p>
<p>The external communication(RS-232) should be configured and tested. Depending on your use case, you can follow below listed documents.</p>
<ul>
<li>If you are using RS-232 commands to communicate with your TV, please check the<a href="https://support.optisigns.com/hc/en-us/articles/9061950942995-Using-RS-232-to-Schedule-TV-Power-On-Off-or-other-commands" target="_self"> advanced scheduling feature</a>. </li>
<li>If you are using IoT sensors, please check <a href="https://support.optisigns.com/hc/en-us/articles/13097501958291-OptiSigns-IoT-Sensor-Add-on-Quick-Start" target="_self">IoT sensor Add-on</a>.</li>
</ul>
<p>Note: To test and confirm your external communication(RS-232) connection and configuraiton are set up properly, you can use the "Trigger Event Viewer" from the side menu of OptiSigns player. It can show the events received from external devices/sensors, and also you can use it to test send commands out to external devices.<br><img src="https://support.optisigns.com/hc/article_attachments/17344618238099"></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/17344754633875"></p>
<h2 id="h_01HPZKZ1D1RM45WJRQ0SQEWXCJ"> </h2>
<h2 id="h_01HPZKZ1D1HDVX43YYN7ZR4CHE"><strong>Let's jump in and get started:</strong></h2>
<p><strong>1. Setup: Enable RS232 logging</strong></p>
<p>If you are on Enterprise plan and interested in this feature, please contact</p>
<p><a href="mailto:support@optisigns.com">support@optisigns.com</a></p>
<p>Once the feature is made available, you can go to settings, under Advanced-&gt;External Communications(RS232) you will see the setup(Analytics) page available. You can also use the link below.<br><a href="https://app.optisigns.com/app/s/external-coms" target="_self">https://app.optisigns.com/app/s/external-coms</a></p>
<p>Click "Analytics", you will be able to enable the RS232 logging here.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/17345659223187"></p>
<p>By default, event data will be logged in real-time.If internet is disconnected, data will be saved locally and will be synced to server automatically when the device come back online.</p>
<p>If for some reason, you don't want real-time data (i.e. to reduce network usage during day time, or if you do "drive-by" data collection once a while). You can unchecked Real-time option and select an upload interval of your choice.</p>
<p><strong>2. Enable data collection on IoT sensors add-on</strong></p>
<p>If you are using IoT sensors, you can set it up to collect the event data within the IoT Sensor Add-on. Simply tick the "Send Data" checkbox, it will start to track the event data. <strong><br><img src="https://support.optisigns.com/hc/article_attachments/17351908243987"><br></strong></p>
<p> </p>
<p><strong>3. Data collection with advanced scheduling</strong></p>
<p>If you are using advanced scheduling to control you TV or other devices supporting RS232, the event data collection is enabled by default if you choose the "RS232 Commands" type. You can configure and send multiple commands together, the commands will be sent to the target device one after anther with small latency. If the target devices are responding with confirmation, the response will be logged as well.</p>
<p>Please note, if you are sending multiple commands together, please check the target device specification, the target device may take longer time to execute the commands, in the case, please send the command separately on its own, otherwise the following commands may not be executed and you will not see response from the logging. </p>
<p><img src="https://support.optisigns.com/hc/article_attachments/17352284082323"></p>
<p><strong>4. Export Data: Schedule data export &amp; download data</strong></p>
<p>You can configure OptiSigns to regularly export your raw data.</p>
<p>Here you can control the frequency of the data export, time window of the data export, and the recipients of the data exports. Also, if you have your own AWS S3 buckets available, you can also configure your AWS S3 as the destination of the data export, it is easier for you to automate and connect it to your own analytics process.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/17345743164307"></p>
<p>Here's how a data export looks like:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/17343162545043"></p>
<p>You can also go to the report history tab and download the historical data export.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/17345817445779"></p>
<p> </p>
<h2 id="h_01HPZKZ1D1N3Z35JB1C7GNZG05"><strong>Summary:</strong></h2>
<p>The RS-232 logging and analytics will collect the event data and make it available to customers. The data is available in JSON format, you can automate the data export and build your own data pipeline to process the data for further analysis. </p>
<p> </p>
<p><strong><span class="wysiwyg-font-size-x-large">That's all!</span></strong></p>
<p> </p>
<p>If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self">support@optisigns.com</a></p>
<p> </p>
<p> </p>