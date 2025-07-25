<h3 id="h_01J6F8FZPQA08RZNPX8X1BFJT2"><span style="color: #434343;">In this article, we will walk you through the process of setting up a service principal for PowerBI in Microsoft Azure, and connecting it to OptiSigns.</span></h3>
<ul>
<li><a href="#Create">Creating an Entra App in Microsoft Azure</a></li>
<li>
<a href="#Enable">Enable PowerBI Service Admin Settings</a>
<ul>
<li><a href="#Add">Add the Service Principal to a Workspace</a></li>
</ul>
</li>
<li><a href="#Auth">Authenticating OptiSigns via Service Principal</a></li>
<li><a href="#Get">Getting PowerBI onto a Screen</a></li>
</ul>
<p>Using a PowerBI service principal with app registration is a preferred option for companies with strict information security rules that don't want to use individual user accounts for PowerBI integration. </p>
<p>This reduces headaches in situations when:</p>
<ul>
<li>There is a position or permission change of a user and authentication needs to be performed again by a different user.</li>
<li>A prolonged authentication token period cannot be set for individual users, and you will need to reauthorize and refresh the token every couple of months.</li>
</ul>
<p>Using a PowerBI service principal, the authentication tokens are associated with a registered app instead of a user. This allows you to set a longer validity time for the authentication token and avoids more frequent re-authorization. Using service principal with App registration for Power BI integration is supported well with OptiSigns.</p>
<div>
<table style="width: 100%;">
<colgroup> <col> </colgroup>
<tbody>
<tr>
<td>
<strong>NOTE: </strong>This feature is only available to customers on an <strong>Enterprise</strong> plan.</td>
</tr>
</tbody>
</table>
</div>
<hr>
<p><a name="Create"></a></p>
<h2 id="h_01J6F8FZPQ4EHTA99C5GG43PGS">Create an Entra App in Microsoft Azure</h2>
<p>An Entra app will be responsible for handling identity and access management for your service principal. In order to create one, you’ll need to login to Microsoft Azure with a viable Microsoft account.</p>
<p>Once at the Azure portal, search for <strong>“app registrations,” </strong>then select <strong>App Registrations </strong>from the list that appears:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32860610406547" alt="app registration instructions in microsoft azure" width="523" height="273"></p>
<p>Create a <strong>New Registration</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32860569069459" alt="how to create a new registration in microsoft azure" width="624" height="120"></p>
<p>On this screen, type a name for the app, then leave the other settings as default. These can be changed or altered at any time.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32860610418707" alt="instructions on registering an application in microsoft azure" width="551" height="392"></p>
<p>Once done, hit <strong>Register.</strong></p>
<hr>
<p><a name="Enable"></a></p>
<h2 id="h_01J6F8FZPQ5B41FRZ3CDFWQEKR">Enable PowerBI Service Admin Settings</h2>
<p>Follow this link to the <a href="https://app.powerbi.com/admin-portal/capacities?experience=power-bi"><span class="wysiwyg-underline" style="color: #1155cc;">PowerBI Admin Portal</span></a>.</p>
<p>Once there, click <strong>Tenant Settings</strong>. Then, scroll down to <strong>Developer Settings</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32860610420627" alt="finding developer settings in tenant settings within powerbi admin portal" width="624" height="481"></p>
<p>Enable the <strong>Embed Content in Apps Settings</strong>, as below:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32860610421779" alt="how to enable embed content in apps" width="611" height="365"></p>
<p>In this example, we’ve set this embed to apply permissions to the entire organization. However, you can restrict access to specific security groups based on your needs. These security settings can be changed as per your requirements.</p>
<p>Next, <strong>Enable Service principals can create workspaces, connections, and deployment pipelines </strong>and <strong>Enable Service Principals can call Fabric public APIs</strong>, as below:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42225175622675" alt="image (28)(1).png"></p>
<p>Like before, we’ve applied these to the entire organization. Just like the last step, you can restrict access to specific security groups based on your needs.</p>
<p><a name="Add"></a></p>
<h3 id="h_01J6F8FZPQGD414JAJHBTVV0Z8"><span style="color: #434343;">Add the Service Principal to a Workspace</span></h3>
<p>Now we need to assign service principal access to the workspaces you want to show in your PowerBI reports.</p>
<p>In the admin portal, click <strong>Workspaces</strong>. You’ll want to go to the workspace you want to assign service principal access to. Click the workspace, then hit <strong>Access</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32860610425107" alt="how to grant service principal access powerbi" width="624" height="265"></p>
<p>Add the service principal you created in the last step as a member of the workspace.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32860569093139" alt="how to add service principal as a member of powerbi workspace" width="535" height="285"></p>
<hr>
<p><a name="Auth"></a></p>
<h2 id="h_01J6F8FZPQAAYNP5Y4BTTKNWK3">Authenticating OptiSigns via Service Principal</h2>
<p>In order to authenticate your PowerBI on OptiSigns via service principal, you’ll need four pieces of information:</p>
<ol>
<li>Name of the service principal</li>
<li>Application (client) ID</li>
<li>Directory (tenant) ID</li>
<li>Application (client) secret</li>
</ol>
<p>Since we’ve already created an Entra app in Azure, we already have access to the first three pieces of information. These can be found under <strong>App Registrations </strong>back in Azure.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32860569095571" alt="where to find app registration information in microsoft azure" width="624" height="243"></p>
<p>In this example, the values have been blurred, but on your Azure portal, these should be visible.</p>
<p>The only piece of information you won’t have is the client secret. To get that, click <strong>Manage → Certificates &amp; Secrets → Client Secrets → New Client Secret</strong></p>
<p><strong><img src="https://support.optisigns.com/hc/article_attachments/32860569099411" alt="how to create new client secret in microsoft azure" width="624" height="307"></strong></p>
<p>Next, set the <strong>Description </strong>and <strong>Expiry</strong>, then click <strong>Add</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32860569100947" alt="how to add a client secret" width="352" height="532"></p>
<p>The <strong>Value </strong>present is the last piece of information you need.</p>
<p>Now, head into the OptiSigns app. Click your <strong>Profile name → More → Integrations.</strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32860610434451" alt="where to find integrations tab in optisigns" width="297" height="553"></p>
<p>A screen like the one below will appear. Click <strong>Add Azure Service Principal.</strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32860569109011" alt="how to add service principal in optisigns" width="624" height="193"></p>
<p>When the popup appears, collect the information mentioned above from Microsoft Azure and input it into OptiSigns. The values match up like this:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32860610442771" alt="inputting all the powerbi service principal information into optisigns" width="624" height="292"></p>
<p>Once all the information is input correctly, hit <strong>Save</strong>. Now your Service Principal is saved to the OptiSigns portal.</p>
<hr>
<p><a name="Get"></a></p>
<h2 id="h_01J6F8FZPQV420X324MGT49ZXK">Getting PowerBI onto a Screen</h2>
<p>Now we’ll need to configure your PowerBI asset in OptiSigns for use with your screens.</p>
<p>In the OptiSigns portal, go to <strong>Files/Assets → Apps → PowerBI</strong></p>
<p><strong><img src="https://support.optisigns.com/hc/article_attachments/32860569116691" alt="how to find powerbi app in optisigns" width="624" height="231"></strong></p>
<p>Check <strong>Use Service Principal </strong>and select the service principal you set up in the last step, or whichever service principal you want to use. </p>
<table style="width: 100%;">
<colgroup> <col> </colgroup>
<tbody>
<tr>
<td>
<strong>NOTE: </strong>Using a service principal, the Power BI Dashboard URL link needs to include the actual <strong>workspace (group)</strong> ID instead of me.</td>
</tr>
</tbody>
</table>
<p><strong><img src="https://support.optisigns.com/hc/article_attachments/32860610472339" alt="powerbi app information in optisigns" width="624" height="549"></strong></p>
<p>Finally, input the URL of whatever report you want to share. Name the app whatever you like, then hit <strong>Preview</strong> to view your report.</p>
<p><strong><img src="https://support.optisigns.com/hc/article_attachments/32860610476307" alt="preview of powerbi app running in optisigns" width="624" height="276"></strong></p>
<p>Hit <strong>Save</strong>, then this PowerBI app will exist as an asset. It can be pushed to any of your screens individually, scheduled, or added to a Playlist.</p>
<h3 id="h_01J6F8FZPQPDABTX05CCPW0PTF"><strong><span style="color: #666666;">That’s all!</span></strong></h3>
<p>If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com"><span class="wysiwyg-underline" style="color: #1155cc;">support@optisigns.com</span></a>.</p>