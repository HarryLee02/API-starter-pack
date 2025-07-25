<p>With Pro Plus and Enterprise plan, you can configure SAML 2.0 with OptiSigns via Google Workspace. The Google Workspace will be acting as the IDP (Identify Provider), and OptiSigns will be working as the SP(Service Provider).</p>
<h3 id="h_01HBE9QRECM6N29AHPZ2BB120Q"><strong>Set up OptiSigns &amp; Google Workspace:</strong></h3>
<p><strong>First you need to do some set up in OptiSigns:</strong></p>
<p>If you don't have a sub domain yet, you can set up one by going to:<br><a href="https://app.optisigns.com/app/s/branding-settings">https://app.optisigns.com/app/s/branding-settings</a></p>
<p>Fill in subdomain field and click Activate. After that you can use this sub domain for "<br>You can also map your own domain like digitalsigns.yourcompany.com by following this <a href="https://support.optisigns.com/hc/en-us/articles/1500000480302" target="_self">article</a>.</p>
<p>This will be the URL that you can share with your users so they can log in to use the app, once integration has set up. In our example we will use <a href="https://advanced.optisigns.net/">https://advanced.optisigns.net/</a></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/21287201525907" alt="mceclip13.png"></p>
<p>Next, go to the SAML Single Sign On setting page:</p>
<p><a href="https://app.optisigns.com/app/s/saml-settings">https://app.optisigns.com/app/s/saml-settings</a></p>
<p>Click Enable SAML SSO.</p>
<p>The settings are:</p>
<ul>
<li>Enable Username &amp; Password login: Allow users to also log in with username/password. It’s recommended to disable it once the integration is all done. As Admin/Owner, it's recommended that you keep at least 1 account with a password log in, in case there are issues, you can always log back in from app.optisigns.com to reconfigure.</li>
<li>Enable User Creation: If users are authenticated, but do not exist in OptiSigns, they will be created in OptiSigns. You should enable this, because you likely already assign/approve users/groups to use OptiSigns, unless for some reason you want to be very strict and want to review roles of users before they can start using OptiSigns.</li>
<li>Enable User Override: Every time a user logs in, if their group assignment have changed on SAML, OptiSigns will update, override new profile settings.</li>
<li>Note the "Single Sign On URL" and "Audience URI (SP Entity ID) URL", you will need this to use in Google Workspace later.</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/21286640961939"></p>
<p> </p>
<p><strong>Next, add OptiSigns as an App in your Google Workspace admin portal:</strong></p>
<p>Log in to your Google Workspace portal as admin -&gt; Apps -&gt; Web and mobile apps</p>
<p>Click Add app -&gt; Add custom SAML app <img src="https://support.optisigns.com/hc/article_attachments/4407485683475" alt="mceclip0.png"></p>
<p>In the popup window, enter OptiSigns as the name of the app, you can upload the app icon here as well. Then click continue.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4407485688467" alt="mceclip1.png"></p>
<p>The next page will provide the IDP data. Get these 2 highlighted information then click continue, these need to be maintained in the OptiSigns SAML SSO settings later.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/21287044557843"></p>
<p>Next page will be the SP information, this is where you should provide the Single Sign On URL, and SP Entity ID you get from your OptiSigns SAML SSO setting.</p>
<p>SP Entity ID from OptiSigns SAML SSO setting should be put under Entity ID.</p>
<p>Single Sign On URL from OptiSigns SAML SSO setting should be put under ACS URL.</p>
<p>Also, set the Name ID format to Email.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/21286792807699"></p>
<p>The next page is where you maintain the attributes. This step will be explained later in this article. Click Finish, and the app is added to the Google Workspace.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/21286840258963"></p>
<p>After completing the app creation on Google Workspace. You can select the OptiSigns app under the "Web and mobile apps". Click on the OptiSigns app, and note the ID in the URL, that is the SPID that will be needed.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4407493347731" alt="mceclip7.png"></p>
<p>Go back to your OptiSigns account maintain above mentioned 3 fields, and save it.</p>
<p>You can get SSO URL, Entity ID, and Certificate from your Google Workspace.</p>
<ul>
<li>Put SSO URL from Google Workspace under SAML 2.0 Endpoint (HTTP).</li>
<li>Put Entity ID from Google Workspace under Identity Provider Issuer.</li>
<li>Put the content from the base64 encoded certificate under Public Certificate.</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/21287166076819"></p>
<p>Now your login portal &amp; integration are all setup.</p>
<p> </p>
<h4 id="h_01HBE9QRECXPGP09BKTPTN54Y7"><strong>Assign &amp; map users, and groups from Google Workspace to OptiSigns</strong></h4>
<p>It's not required, but recommended to create groups of users to be assigned, and map to OptiSigns Roles, and Teams so they will automatically have the right role &amp; group.</p>
<p><strong>IMPORTANT NOTE: If you don't configure this, all users will be assigned User Role &amp; Default Team (screenshot see below)</strong></p>
<p> </p>
<p>To configure how OptiSigns should map the user groups to OptiSigns Roles by going to: <a href="https://app.optisigns.com/app/s/saml-settings">https://app.optisigns.com/app/s/saml-settings</a></p>
<p>Scroll to Advanced Settings and create a mapping.<br>Group Name (can use department from Google Workspace), Role (role in OptiSigns) mapping. <br><img src="https://support.optisigns.com/hc/article_attachments/4407485832851" alt="mceclip8.png"></p>
<p>It's best practice to create a group specifically for OptiSigns with name prefix with optisigns- and map to OptiSigns like below:</p>
<ul>
<li>optisigns-admins (SAML group) -&gt; OptiSigns role: Admin</li>
<li>optisigns-users (SAML group) -&gt; OptiSigns role: Users</li>
<li>optisigns-custom-role (SAML group) -&gt; OptiSigns custom role that you create</li>
</ul>
<p><strong>How to handle Unmapped users/groups:</strong></p>
<p>You can map the "Unmapped users/group" to No Team (Disabled)</p>
<p>This way they will receive an error when trying to log in and will have to reach out to Admins to get correct teams, and roles assigned. This can be used as a safe guard, in case some users accidentally got assigned OptiSigns app but not the right groups.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/21287201539475" alt="mceclip3.png"></p>
<p>Note that if you map a SAML group to a Team and then delete the team, it will result in new user being mapped to No Team and will have to contact you to be assigned to a team to use the app.</p>
<p> </p>
<p>Next, it is time to talk about the attributes mapping. This is the last step when creating the app in Google Workspace.</p>
<p>Currently, OptiSigns support attributes mapping of first name, last name and group. You can define the attribute name in Google Workspace and set it to the same default attributes name used on OptiSigns.</p>
<p>These mappings will pass information to OptiSigns on what's user's Name and Groups.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4407485726611" alt="mceclip5.png"></p>
<p> </p>
<p>The "App attributes" are corresponding to OptiSigns</p>
<p><a href="https://app.optisigns.com/app/s/saml-settings" target="_self" rel="undefined">https://app.optisigns.com/app/s/saml-settings</a></p>
<p>OptiSigns accept firstName, lastName, and group by default. Instead of setting the attribute names to the default attribute name used on OptiSigns,  you can also change the attribute name on OptiSigns to match the attribute name you defined on Google Workspace as well.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4407485875347" alt="mceclip9.png"></p>
<h4 id="h_01JH5W64QF8FQMHHK66NHKXHT2"><strong><span style="color: #666666;">I've made it into my OptiSigns account, but don't seem to have all the side menu options I'm used to. What’s going on?</span></strong></h4>
<p>It's likely you've signed on through your Branded Portal, using a URL similar to this one:</p>
<pre>https://app.optisigns.com/signIn/&lt;accountId&gt;</pre>
<p>You'll first need to find your OptiSigns Account ID. To do this, simply find a paired screen, and hit <strong>Edit <span id="docs-internal-guid-af17cc22-7fff-76d0-f908-3ba6ea4fe31b">→</span> Advanced <span id="docs-internal-guid-af17cc22-7fff-76d0-f908-3ba6ea4fe31b">→</span> More</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/38962512579219" alt="edit screen advanced more"></p>
<p>Click <strong>Device Info:</strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/38962512582675" alt="info button edit screen"></p>
<p>Find the <strong>"accountId"</strong> number, then write it down somewhere. You'll be needing it soon.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/38962490259731"></p>
<p>Now copy the following URL, being sure to substitute your account ID where appropriate:</p>
<pre>https://app.optisigns.com/signIn/&lt;accountId&gt;</pre>
<p>Then put this URL in your Google Workspace under SSO URL.</p>
<h3 id="h_01HBE9QRECHWBR763YCYD2XN4E"><strong>That's it!</strong></h3>
<p>You have configured SAML 2.0 for OptiSigns with Google Workspace.</p>
<p>Now your users can log in using the subdomain that you configured (in this case it was <a href="https://advanced.optisigns.net/signIn">https://advanced.optisigns.net/signIn</a>).</p>
<p>You can share the URL with your users and they can log in with their SSO credentials.</p>
<p> </p>
<p>If you have any additional questions or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self">support@optisigns.com</a></p>
<p> </p>