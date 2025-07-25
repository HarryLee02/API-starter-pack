<h3 id="h_01J7Y2QG6R8ADW4D5BRGYXFY2N"><span style="color: #434343;">With OptiSync, you can dynamically map data from sources such as Google Sheets, Microsoft Excel, APIs, and more to display updating event schedules on your screens. In this article, we will walk you through the steps.</span></h3>
<ul>
<li><a href="#Examples">Examples of Some Event Schedules OptiSync Can Make</a></li>
<li>
<a href="https://support.optisigns.com/hc/en-us/articles/undefined#Daily">Setting up a Daily Event Schedule with OptiSync</a>
<ul>
<li>
<a href="#Google">Option 1: Via Google Sheet/Excel</a>
<ul>
<li><a href="#Time">How to Set Up a Daily Event Schedule that Updates with the Passage of Time</a></li>
</ul>
</li>
<li><a href="#API">Option 2: Via API</a></li>
</ul>
</li>
<li><a href="#Weekly">Setting up a Weekly Event Schedule with OptiSync</a></li>
<li><a href="#Monthly">Setting up a Monthly Event Calendar with OptiSync</a></li>
</ul>
<p>Automatically updating your screens with event information is useful in many situations, including providing real-time updates across a wide area. </p>
<p>Providing updated daily, weekly, or monthly event schedules for conventions, trade shows, schools, local governments, public places, nonprofits, company internal events, and far more is OptiSync’s specialty.</p>
<p>In this guide, we’ll give very high level instructions on how to make several types of event schedules: daily, weekly, and monthly. This will not be an exhaustive guide on every possible way to format your spreadsheets for uploading into OptiSigns, or how to provide data for your API for uploading into OptiSigns. If you’d like a more comprehensive guide on how to input data into OptiSigns, see our <a href="https://support.optisigns.com/hc/en-us/articles/29217646663187-How-to-Set-Up-Dynamic-Data-Mapping-with-OptiSync"><span class="wysiwyg-underline" style="color: #1155cc;">Dynamic Data mapping guide</span></a>.</p>
<div>
<table style="width: 100%;">
<colgroup> <col> </colgroup>
<tbody>
<tr>
<td>
<strong>NOTE: </strong>OptiSync and dynamic data mapping are exclusive to <strong>Pro Plus</strong> plans and above.</td>
</tr>
</tbody>
</table>
</div>
<hr>
<p><a name="Examples"></a></p>
<h2 id="h_01J7Y2QG6S304AC0SNBNV6K3C8">Examples of Some Event Schedules Made with OptiSync</h2>
<h4 id="h_01J806N9K59WM2MRX5CT7T0NTN"><strong>Daily:</strong></h4>
<p><strong><img src="https://support.optisigns.com/hc/article_attachments/33492511435411" alt="example of a daily event schedule created using optisync"></strong></p>
<h4 id="h_01J806NCFNV7C37C8CCDWDBHH0"><strong>Weekly:</strong></h4>
<p><strong><img src="https://support.optisigns.com/hc/article_attachments/33468569053459" alt="example of a weekly event schedule created using optisync" width="624" height="344"></strong></p>
<h4 id="h_01J806NFA12FG3EZSC8EJ7CBWP">
<strong>Monthly:</strong><strong><br></strong><img src="https://support.optisigns.com/hc/article_attachments/33468600300819" alt="example of a weekly event schedule created using optisync">
</h4>
<h4 id="h_01J806NJJP57Z9JARE51H8KBD4"><strong>Split Screen:</strong></h4>
<p><strong><img src="https://support.optisigns.com/hc/article_attachments/33468759684755" alt="example of split screen event schedule created using optisync"></strong></p>
<hr>
<p><a name="Daily"></a></p>
<h2 id="h_01J7Y2QG6SGZWPRWVMQFHTX7QT">Setting up a Daily Event Schedule with OptiSync</h2>
<p>Daily event schedules are common for all kinds of businesses, which we won’t exhaustively list here.</p>
<p><a name="Google"></a></p>
<h3 id="h_01J7Y2QG6SKZQPT9PKPS6RMFD2"><span style="color: #434343;">Option 1: Via Google Sheet/Excel</span></h3>
<p>The simplest way to create a daily schedule is by organizing your event data similarly to the screenshot below:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/33468569065363" alt="example of google sheet layout with daily events" width="601" height="175"></p>
<p>The <strong>data is mapped from Row 2 onwards</strong>, and is <strong>grouped by Row.</strong> This means when the DataSource is added to OptiSigns, it will be clustered like this:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/33468600306195" alt="data clusters in optisigns, including Row 1, Event Name, Event Time, Event Description, and Event Over data points"></p>
<p>Since this is a daily schedule, we’re only worried about the time of the event, and we’ve also included a description. However, you can include all kinds of information should you feel it necessary.</p>
<p>Now, you’ll need to add your DataSource to OptiSigns.</p>
<p><strong>Please follow these guides to upload different kinds of DataSources:</strong></p>
<ul>
<li><a href="https://support.optisigns.com/hc/en-us/articles/29838866920211"><span class="wysiwyg-underline" style="color: #1155cc;">How to add Google Sheets as a DataSource for OptiSync</span></a></li>
<li><a href="https://support.optisigns.com/hc/en-us/articles/29863080711059"><span class="wysiwyg-underline" style="color: #1155cc;">How to add a Microsoft 365 Excel Spreadsheet as a DataSource for OptiSync</span></a></li>
</ul>
<p>Now that your DataSource is added, we can get started in Designer.</p>
<p>Daily events are best mapped as a <strong>Repeater</strong>. These allow you to set up a single design and have all your data appear within it</p>
<p>To set up a repeater, drag your first <strong>Row</strong> onto your design. You’ll receive the below prompt. Select <strong>Use in a Repeater</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/33468600312723" alt="optisigns menu choice with red arrow pointing at use in a repeater" width="422" height="200"></p>
<p>You’ll be able to format your data however you wish.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/33468600319891" alt="example of a daily event schedule using optisync for optisigns gym" width="624" height="348"></p>
<p><a name="Time"></a></p>
<h4 id="h_01J7Y2QG6S9P5REXCM5138N6EW"><span style="color: #666666;">How to Set Up a Daily Event Schedule that Updates with the Passage of Time</span></h4>
<p>With a Daily Event schedule, once an event happens, there’s no need to keep displaying the event. With OptiSync, you can configure your DataSource to ignore events which are now in the past.</p>
<p>To do this, we’ll need to set up an additional column in our spreadsheet. We’ll call it the <strong>Event Over? </strong>column.</p>
<p><strong><img src="https://support.optisigns.com/hc/article_attachments/33468600323987" alt="google sheets with an additional event over? column" width="624" height="139"></strong></p>
<p>In the “Event Over?” column, put this formula:</p>
<pre>=IF(<span style="color: #f7981d;">B2</span>&lt;=NOW(),"Yes","No")</pre>
<div>
<table style="width: 100%;">
<colgroup> <col> </colgroup>
<tbody>
<tr>
<td>
<strong>NOTE: </strong>This formula will only work if both the Date and Time are present in the Event Time cell. The “B2” part should match the actual event time, i.e. B3 for Zumba in the Example.</td>
</tr>
</tbody>
</table>
B2 is your reference value, which maps up with the event time. This formula will work regardless of whether or not the current date is referenced in the “Event Time” column.</div>
<p>Within the settings of your Google Sheet, please ensure Recalculation is on (e.g., On change and every hour/minute), otherwise the formula won't recalculate.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/33468569084819" alt="google sheets tutorial image with Calculation highlighted and red arrow pointing at On change and every minute option" width="464" height="281"></p>
<p>You can access this in your Google Sheet by selecting <strong>File</strong> <strong><span id="docs-internal-guid-d98d2b93-7fff-8ae6-412b-20d302c34632">→</span></strong> <strong>Settings</strong> <strong><span id="docs-internal-guid-d98d2b93-7fff-8ae6-412b-20d302c34632">→</span></strong> <strong>Calculation.</strong></p>
<p>All the “Event Over?” column does is check whether or not the event time has passed with a simple yes or no. When this screenshot was taken, it was between 1:00 and 3:30, so the first event to be shown should be “Rowing,” followed by “Surrender Yoga.”</p>
<p>To do this, we’ll make use of the <strong>DataSource</strong> <strong>Filter</strong>.</p>
<p>To get started, highlight the data you want to filter, then hit <strong>Settings. </strong>Then, hit the <strong>Filter</strong> option under your DataSource.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42920711657491" alt="firefox_69WJbcItk0.gif"></p>
<p>This screen will appear:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/33468600337171" alt="optisigns datasource filter" width="624" height="340"></p>
<p>What follows is, essentially, an <a href="https://support.microsoft.com/en-us/office/and-function-5f19b2e8-e1df-4408-897a-ce285a19e9d9"><span class="wysiwyg-underline" style="color: #1155cc;">AND statement</span></a> or an <a href="https://support.microsoft.com/en-us/office/and-function-5f19b2e8-e1df-4408-897a-ce285a19e9d9"><span class="wysiwyg-underline" style="color: #1155cc;">OR statement</span></a> you might use in Excel or Google Sheets. The easiest way to understand the Filter option is as an Excel or Google Sheet formula you input within OptiSigns.</p>
<p>You can add <strong>Rules</strong> or <strong>RuleSets</strong> to your filter to create as much complexity as you need:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/33468569116691" alt="optisigns datasource filter with additional rules and rulesets" width="624" height="339"></p>
<p>In order to set up a Rule, you’ll need to configure three values.</p>
<p>Selecting the first box gives you these options:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/33468569122707" alt="optisigns datasource filter first box options" width="199" height="205"></p>
<p>By default, these options equate to the <strong>headers of your columns in the spreadsheet you have mapped.</strong> This list will vary in length depending on how many headers you have. You can also input any value you wish by typing it in the box.</p>
<p>The second box is your <strong>Variable.</strong> OptiSigns provides these options:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/33468569128851" alt="optisigns datasource filter second box options" width="148" height="359"></p>
<p>The final option provides the following default values:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/33468569132819" alt="optisigns datasource filter third box options" width="393" height="183"></p>
<p>By default, these map to a screen or other device, allowing your filter to target only certain screens.</p>
<p>However, this value <strong>can be changed to anything you want.</strong> Simply type any value you wish.</p>
<p>For our purposes, we want to check to see if the “Event Over?” is equal to No:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/33468569142163" alt="example of optisync datasource filter with first value set to Event Over?, second value set to Equals, third value set to No" width="624" height="149"></p>
<p>That removes every row where the “Event Over?” value is Yes. Now, your Event Schedule will display this:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/33468569144851" alt="example of daily event schedule with filters applied" width="624" height="351"></p>
<p>There are dozens of possibilities using the OptiSync filter to show even more precise automated data on your screens.</p>
<hr>
<p><a name="API"></a></p>
<h3 id="h_01J7Y2QG6S50E204JPE9GWH9MZ"><span style="color: #434343;">Option 2: Via API</span></h3>
<p>In order to pull event data from an API, follow our guide on <a href="https://support.optisigns.com/hc/en-us/articles/22875592994195-How-to-Integrate-API-and-Publish-API-Data-via-OptiSync"><span class="wysiwyg-underline" style="color: #1155cc;">integrating API and publishing API data.</span></a></p>
<p>Data can be set up in Designer in the same manner as if you were using a spreadsheet.</p>
<hr>
<p><a name="Weekly"></a></p>
<h2 id="h_01J7Y2QG6SB1N19W9KXSSGCW9R">Setting up a Weekly Event Schedule with OptiSync</h2>
<p>Setting up a weekly event schedule is much the same as a daily schedule. There are numerous ways you can format your spreadsheet, but one of the easiest is like this:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/33468569155091" alt="google sheet weekly event schedule example" width="624" height="228"></p>
<p>Here, we’ve grouped all our events together with their location, date, and time. Depending on your needs, these may need to be input as individual rows, or individual pieces rather than as Repeaters.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42920711659923"></p>
<p>Complex weekly schedules like the one above will be easiest to input individually. Selecting the <strong>Row</strong> and dragging it onto your Design will open the following prompt. Hit <strong>Use on its own</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42920697677971"></p>
<p>Organizing your data this way will allow precise placement. We recommend this option when data can’t be easily repeated, as in this example where there are different numbers of events on different days.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/33468600389011" alt="weekly event schedule example design" width="624" height="352"></p>
<p>Your spreadsheet can be updated every week, and a simple refresh will update the design on OptiSigns.</p>
<hr>
<p><a name="Monthly"></a></p>
<h2 id="h_01J7Y2QG6STP4XTV4D6XKNG8ZW">Setting up a Monthly Event Schedule with OptiSync</h2>
<p>Monthly event calendars let you alert your customers or organization of upcoming events well in advance. Using Google Sheets as an example, the data can be organized in much the same way we did our weekly events. Simply add as many columns as you might want to place on your design. Remember, not every piece of data needs to be added to your final design, so you’re free to pick and choose as needed.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/33468600392851" alt="google sheets monthly event schedule example"></p>
<p>Importing this example data to OptiSigns will provide us with these clusters:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42920711662995"></p>
<hr>
<p><a name="Calendar"></a></p>
<h3 id="h_01J7Y2QG6SGDQND77E087WFX75"><span style="color: #434343;">Creating a Calendar-Style Monthly Event Schedule</span></h3>
<p>Calendar-style monthly event schedules, as the name suggests, present your event data in a calendar format. This is the best option if you want to see a great many events at a glance.</p>
<p>Should you choose the calendar-style format, space is a primary concern. You’ll have to pick and choose which pieces of data you want to display - long descriptions of an event, for example, would not be able to fit on a normal sized calendar. Fortunately, you do not have to discard any of your data, nor edit your spreadsheet. All you have to do is choose what individual pieces of data you want to place on your calendar.</p>
<p>For this example, we’ll only use the name of the Lunch and the Day of the Month on the menu. You could easily add a time repeater, as well.</p>
<p>Your data can be placed on a calendar design anywhere you like. Below, we’ve set up the entire calendar as a repeater and added the days of the week above.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/33468569193491" alt="calendar style event schedule example"></p>
<hr>
<p><a name="Split"></a></p>
<h2 id="h_01J7Y2QG6S39XHX3DP0N6KRYJ8">Setting Up a Split Screen Event Schedule</h2>
<p>Creating a split-screen for your event schedule is a fantastic way to maximize your screens, allowing both pertinent information and promotional material to be disseminated simultaneously. A split screen event schedule can make use of either Landscape or Portrait formatted designs of any type. You can use any of the above types of event schedules in a split screen.</p>
<p>For this example, we’re going to put together a number of techniques we’ve learned above, using this data example:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/33468600411411" alt="google sheets monthly event schedule example" width="624" height="209"></p>
<p>For this event schedule, we want to make use of all our data. So, we’ll need a repeater which shows the Event Name, Event Time, End Time (or Duration), Event Location, and Event Description, as well as organizing them by day of the week.</p>
<p>There are a few ways to do this. You can simply attach the Day of the Week to each Repeater value, giving us something like this:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/33468569204243" alt="optisync repeater example for daily event" width="624" height="136"></p>
<p>Or, you can create individual repeaters for each day of the week, allowing them to cycle.</p>
<p>Then, when you’re ready, you can attach it to your split screen app, creating a beautiful event schedule without getting in the way of anything else you'd like to display.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/33468786539667" alt="split screen weekly event schedule example"></p>
<p>For a step-by-step walkthrough on putting together a split screen, see our guide on <a href="https://support.optisigns.com/hc/en-us/articles/360026559573-How-to-Create-and-Use-the-Split-Screen-App"><span class="wysiwyg-underline" style="color: #1155cc;">how to create and use the Split Screen app</span></a>.</p>
<h3 id="h_01J7Y2QG6S7377WZHGX9KD689W"><span style="color: #434343;">That’s all!</span></h3>
<p>If you have any questions or issues that need support, please feel free to reach out to us at <a href="mailto:support@optisigns.com"><span class="wysiwyg-underline" style="color: #1155cc;">support@optisigns.com</span></a>.</p>