<h4 id="h_01J04A3XQRDPKN6P9JM9MVYG51">Using our new OptiSync feature in Designer, you can add your Google Sheets to your DataSources and apply to your designs or our prebuilt Repeater Templates or Components. For a breakdown on OptiSync, please visit our guide <strong><a href="https://support.optisigns.com/hc/en-us/articles/29217646663187" target="_blank" rel="noopener noreferrer">here</a></strong>. </h4>
<table style="border-collapse: collapse; width: 64%;" border="1">
<tbody>
<tr>
<td style="width: 100%;">Note: OptiSync is only available on Pro Plus and above plans. </td>
</tr>
</tbody>
</table>
<h2 id="h_01HZ319XPTVVKRKSDQ9E7M3239">Adding Your Google Sheets as a DataSource</h2>
<p>There are two different methods to adding Google Sheets to your DataSources:</p>
<h4 id="h_01HZ324M9HF4AM3Y15VHX3M3BR"><strong>Method 1: Through Designer</strong></h4>
<ul>
<li>On the Files/Assets page, select <strong>Designer</strong> from the Apps</li>
<li>Select <strong>DataSource</strong> on the side menu, then <strong>Add DataSource</strong>
</li>
<li>Click <strong>Google Sheets</strong>
</li>
<li>Copy and Paste your Google Sheets URL into the provided text box, then <strong>Import Data</strong>
<ul>
<li>Note: You will be prompted to sign into your Google</li>
</ul>
</li>
<li>Once your Google Sheets is imported into a table in our portal, click <strong>Save</strong>
</li>
<li>
<strong>Name</strong> your DataSource something easily recognizable</li>
<li>Select your Synchronization and Update Interval</li>
<li>Click <strong>Done</strong>
</li>
</ul>
<p><strong style="font-size: 1.1em;">Method 2: Through Account Settings</strong></p>
<ul>
<li>In our portal, select your account name, then <strong>More</strong>, then <strong>DataSources</strong>
</li>
<li>Select <strong>Google Sheets </strong>from the list of options</li>
<li>Copy and Paste your Google Sheets URL into the provided text box, then <strong>Import Data</strong>
<ul>
<li>Note: You will be prompted to sign into your Google</li>
</ul>
</li>
<li>Once your Google Sheets is imported into a table in our portal, click <strong>Update</strong>
</li>
<li>
<strong>Name</strong> your DataSource something easily recognizable</li>
<li>Select your Synchronization and Update Interval</li>
<li>Click <strong>Done</strong>
</li>
<li>Your <strong>DataSource</strong> will now be listed within your Advanced Account Settings</li>
</ul>
<div style="position: relative; width: 100%; height: 0; padding-top: 56.2500%; padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden; border-radius: 8px; will-change: transform;"><iframe style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0; margin: 0;" src="https://www.canva.com/design/DAGGpKj60qc/ofo2QuiiW6le9mMlq1SEFw/view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
  </iframe></div>
<p id="h_01HZ324DQH2Y0M0FFB38W2ZN4D"><span class="wysiwyg-underline"><strong>Synchronization</strong></span></p>
<ul>
<li>
<strong>Only import once:</strong> This option imports the data only once when you add the DataSource. After the initial import, the data will not be updated automatically.</li>
<li>
<strong>Periodic direct access:</strong> This option regularly fetches the latest data directly from the device through your gateway, providing "live access" to the data and ensuring you have the most up-to-date information available directly from the device.
<ul>
<li><em>This is better for more consistent update intervals, but could cause performance issues. </em></li>
</ul>
</li>
<li>
<strong>Periodic background sync:</strong> This option periodically syncs data to your server in the background at regular intervals, reducing the need for direct queries to the device.</li>
</ul>
<table style="border-collapse: collapse; width: 100%; height: 44px;" border="1">
<tbody>
<tr style="height: 22px;">
<td class="wysiwyg-text-align-center" style="width: 100%; height: 22px;"><strong>IMPORTANT</strong></td>
</tr>
<tr style="height: 22px;">
<td style="width: 100%; height: 22px;">OptiSync does not support special characters (i.e. anything outside the scope of an English-language keyboard). This will cause the system data to read as blank, and it will not show.</td>
</tr>
</tbody>
</table>
<p id="h_01HZ326QQCFT4MW7RF3JC7HTQH"><span class="wysiwyg-underline"><strong>Update Interval</strong></span></p>
<p><em>The duration of time between updates if you chose "Periodic direct access" or "Periodic background sync"</em></p>
<ul>
<li>None<em> (Your Datasource will import with the newest data available, but will not continuously update afterward. You will have to force refresh data for new updates.) </em>
</li>
<li>30 minutes</li>
<li>1 hour</li>
<li>8 hours</li>
</ul>
<table style="border-collapse: collapse; width: 64.2857%;" border="1">
<tbody>
<tr>
<td style="width: 100%;">
<h4 id="h_01HZ57NKKH32JF2ZPHCK9BY3P4">If you'd like to learn more about OptiSync and how to use this DataSource for Data Mapping, please visit the following guide:</h4>
</td>
</tr>
<tr>
<td style="width: 100%;"><strong><a href="https://support.optisigns.com/hc/en-us/articles/29217646663187" target="_blank" rel="noopener noreferrer">How to Set Up Dynamic Data Mapping with OptiSync</a></strong></td>
</tr>
</tbody>
</table>
<h2 id="h_01HZ56WM18EGT7Y5E4A4ZQ4796">That's it!</h2>
<p id="h_01HZ56Z6PCSVBME8P27C2GX7Q6">Now you've successfully added your Excel spreadsheet as a DataSource to be used for data mapping with OptiSync!</p>