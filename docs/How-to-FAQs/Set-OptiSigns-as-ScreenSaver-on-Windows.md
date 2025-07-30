<p>Sometimes, you would want to set OptiSigns to run if the PC is idle for some time.<br>This is a good use case for Kiosk and Public use computers.</p>
<p>In this guide, we will walk you through end to end process to set OptiSigns app as Screen Saver on Windows.</p>
<h3 id="h_01HPXZ755T0EJZ2MYECRN8FH68">How to Set OptiSigns as Screen Saver on Windows.</h3>
<p>First open OptiSigns side menu, click Advanced, and turn on "Screen Saver Mode".</p>
<p>When this mode is on, OptiSigns will be closed on any mouse move, click, or keyboard pressed.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4403429024787" alt="mceclip0.png"></p>
<p>Then use Window's task scheduler to run OptiSigns when the PC is idle.</p>
<p>Here's the steps, on Windows click Start, search for "Task Scheduler" &amp; open it.</p>
<p>Task Scheduler -&gt; Create Task -&gt; "Trigger" tab -&gt; New -&gt; "Begin the task:" -&gt; "On Idle"</p>
<p>Next, go to the "Actions" tab and set the action to whatever it is you want to run.</p>
<ul>
<li>Search for "<strong>Task Scheduler</strong>" &amp; open it</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/360091166373" alt="Task_Scheduel_1.png" width="620" height="508"></p>
<ul>
<li>
<strong>Create Task</strong> in your Task Scheduler</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/360091166393" alt="Task_Scheduel_2.png" width="620" height="445"></p>
<ul>
<li>Set <strong>Configure</strong> for your device</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/360091166413" alt="Task_Scheduel_3.png" width="620" height="445"></p>
<ul>
<li>Go to <strong>Triggers</strong> tap, and click "<strong>New ...</strong>"</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/360091166433" alt="Task_Scheduel_4.png" width="620" height="445"></p>
<ul>
<li>Set Begin the task: "<strong>On idle</strong>"</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/360091166453" alt="Task_Scheduel_5.png" width="620" height="445"></p>
<ul>
<li>Go to <strong>Actions</strong> tap, and click "<strong>New ...</strong>"</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/360091166473" alt="Task_Scheduel_6.png" width="620" height="445"></p>
<ul>
<li>Set Action: "<strong>Start a program</strong>", and "<strong>Browse</strong>" OptiSigns app's location.</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/360089015334" alt="Task_Scheduel_7.png" width="620" height="445"></p>
<ul>
<li>Go to <strong>Condition</strong> tap, and set the condition for your computer. </li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/360089015354" alt="Task_Scheduel_8.png" width="620" height="445"></p>
<ul>
<li>Go to <strong>Setting</strong> tap, and set "<strong>Run a new instance in parallel</strong>" (The Task Scheduler service will run the new instance of the task in parallel with the instance that is already running.)</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/360089015394" alt="Task_Scheduel_9.png" width="620" height="445"></p>
<ul>
<li>After that, you finish your task setting. You can click "<strong>Run</strong>" to start this task.</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/360089015494" alt="Task_Scheduel_10.png" width="620" height="445"></p>
<ul>
<li>Your status of task will show "<strong>Running</strong>". </li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/360091166533" alt="Task_Scheduel_11.png" width="621" height="445"></p>
<ul>
<li>Close OptisSigns app</li>
</ul>
<p>Once the computer is idle, your screen will run OptiSigns app. </p>
<p>You're ready to go.</p>
<p> </p>
<p><strong>IMPORTANT:</strong></p>
<p>Because OptiSigns is closed on any mouse move, click or key press when Screen Saver mode is turned on.</p>
<p>If you want to control OptiSigns again, press Ctrl + Alt + A or Ctrl + Alt + S, this will turn off Screen Saver mode, and you can interact with OptiSigns.</p>
<p> </p>
<p>If you have feedback on how to make the how-to guides better, please let us know at: <a class="link-viewer_link__2qJYG blog-link-hashtag-color y_1_u" href="mailto:support@optisigns.com" target="_top" rel="noreferrer">support@optisigns.com</a></p>
<p> </p>