<p>With Pro Plus and Enterprise plan, you can configure SAML 2.0 with OptiSigns via OneLogin.</p>
<p>OneLogin will be acting as the IDP (Identify Provider), and OptiSigns will be working as the SP(Service Provider).</p>
<p> </p>
<h3 id="h_01HQ07TWN78FJ1WDBRMQXYRKQ9"><strong>Set up OptiSigns &amp; OneLogin:</strong></h3>
<p><strong>First you need to do some set up in OptiSigns:</strong></p>
<p>If you don't have a sub domain yet, you can set up one by going to:<br><a href="https://app.optisigns.com/app/s/branding-settings">https://app.optisigns.com/app/s/branding-settings</a></p>
<p>Fill in subdomain field and click Activate. After that you can use this sub domain for "<br>You can also map your own domain like digitalsigns.yourcompany.com by following this <a href="https://support.optisigns.com/hc/en-us/articles/1500000480302" target="_self">article</a>.</p>
<p>This will be the URL that you can share with your users so they can log in to use the app, once integration has set up. In our example we will use <a href="https://advanced.optisigns.net/">https://advanced.optisigns.net/</a></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/19053401939731" alt="mceclip13.png"></p>
<p>Next go to SAML Single Sign On setting page:</p>
<p><a href="https://app.optisigns.com/app/s/saml-settings">https://app.optisigns.com/app/s/saml-settings</a></p>
<p>Click Enable SAML SSO.</p>
<p>The settings are:</p>
<ul>
<li>Enable Username &amp; Password login: <span style="font-weight: 400;">Allow users to also log in with username/password. It’s recommended to disable once integration is all done. As Admin/Owner, it's recommended that you keep at least 1 account with password log in, in case there's issues, you can always log back in from app.optisigns.com to reconfigure.</span>
</li>
<li>Enable User Creation: <span style="font-weight: 400;">If users are authenticated, but do not exist in OptiSigns, they will be created in OptiSigns. You should enable this, because you likely already assign/approve users/groups to use OptiSigns, unless for some reason you want to be very strict and want to review roles of users before they can start using OptiSigns</span>.</li>
<li>Enable User Override: <span style="font-weight: 400;">Every time a user logs in, if their group assignment have changed on SAML, OptiSigns will update, override new profile settings.</span>
</li>
<li>Note the "Single Sign On URL" and "Audience URI (SP Entity ID) URL", you will need this to use in OneLogin later.</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/19053301304083"></p>
<p> </p>
<p><strong>Next, add OptiSigns as an App in your OneLogin admin portal:</strong></p>
<p>Log in to your OneLogin portal as admin -&gt; Applications</p>
<p>Click Add app</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4407386965907" alt="mceclip0.png"></p>
<p>On the next page, search for "SAML" in the search box, and then select the "SAML Custom Connector (Advanced)".</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4407387031315" alt="mceclip1.png"></p>
<p>Enter "OptiSigns" in the display name, then click Save. You can also upload the OptiSigns logo here as well.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4407392839187" alt="mceclip2.png"></p>
<p>After saving, go to the configuration page. This is where you should provide the Single Sign On URL, and SP Entity ID you get from your OptiSigns SAML SSO setting.</p>
<ul>
<li>SP Entity ID from OptiSigns SAML SSO setting should be put under <strong>Audience (EntityID)</strong> and <strong>Login URL</strong>.</li>
<li>Single Sign On URL from OptiSigns SAML SSO setting should be put under <strong>Recipient</strong>, <strong>ACS URL validator,</strong> and <strong>ACS URL</strong>. </li>
<li>Change the <strong>SAML initiator</strong> to the <strong>Service Provider</strong>
</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/19053399114899"></p>
<p>Then go to the SSO page. Get these 3 highlighted information, these need to be maintained in the OptiSigns SAML SSO settings. After clicking View Details of the certificate, you can find the encoded content of the certificate, this will be needed in the next step.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/19053348948883"></p>
<p> </p>
<p>Go back to your OptiSigns account maintain above mentioned 3 fields, and save it.</p>
<p>Put the SAML 2.0 endpoint from OneLogin under the SAML 2.0 Endpoint.</p>
<p>Put the Issuer URL from OneLogin under Identity Provider Issuer.</p>
<p>Put the content from base64 encoded x509 certificate under Public Certificate.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/19053330062483"></p>
<p>Now your login portal &amp; integration are all setup.</p>
<p> </p>
<h4 id="h_01HQ07TWN8DZ4Z8VGTRD8V3XSY"><strong>Assign &amp; map users, and groups from OneLogin to OptiSigns</strong></h4>
<p>It's not required, but recommended to create groups of users to be assigned, and map to OptiSigns Roles, and Teams so they will automatically have the right role &amp; group.</p>
<p><strong>IMPORTANT NOTE: If you don't configure this, all users will be assigned User Role &amp; Default Team (screenshot see below)</strong></p>
<p> </p>
<p>To configure how OptiSigns should map the user groups to OptiSigns Roles by going to: <a href="https://app.optisigns.com/app/s/saml-settings">https://app.optisigns.com/app/s/saml-settings</a></p>
<p>Scroll to Advanced Settings and create a mapping.<br>Group Name (roles assigned to the user from OneLogin), Role (role in OptiSigns) mapping. <br><img src="https://support.optisigns.com/hc/article_attachments/4407387515155" alt="mceclip9.png"></p>
<p>It's best practice to create a group specifically for OptiSigns with name prefix with OptiSigns- and map to OptiSigns like below:</p>
<ul>
<li>optisigns-admins (SAML group) -&gt; OptiSigns role: Admin</li>
<li>optisigns-users (SAML group) -&gt; OptiSigns role: Users</li>
<li>optisigns-custom-role (SAML group) -&gt; OptiSigns custom role that you create</li>
</ul>
<p><strong>How to handle Unmapped users/groups:</strong></p>
<p>You can map the "Unmapped users/group" to No Team (Disabled)</p>
<p>This way they will receive an error when trying to log in and will have to reach out to Admins to get correct teams, and roles assigned. This can be used as a safeguard, in case some users accidentally get assigned OptiSigns app but not the right groups.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/19053410145299" alt="mceclip3.png"></p>
<p>Note that if you map a SAML group to a Team and then delete the team, it will result in the new user being mapped to No Team and will have to contact you to be assigned to a team to use the app.</p>
<p> </p>
<p>Next, go to your OneLogin portal. Go to the parameters page of the OptiSigns application. This is where you maintain the mapping of the attributes.</p>
<p>Create new custom parameters here by clicking the + icon. Currently, OptiSigns support attributes mapping of first name, last name, and group. You can set the customer parameter name to the same default attribute name used on OptiSigns, and then assign it to the corresponding values from OneLogin.</p>
<p>These mappings will pass information to OptiSigns on the user's Name and Group.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4407387440147" alt="mceclip7.png"></p>
<p> </p>
<p>The parameter names are corresponding to OptiSigns</p>
<p><a href="https://app.optisigns.com/app/s/saml-settings" target="_self" rel="undefined">https://app.optisigns.com/app/s/saml-settings</a></p>
<p>OptiSigns accept firstName, lastName, and group by default. Instead of setting the parameter names to the default attribute name used on OptiSigns,  you can also change the attribute name on OptiSigns to match the parameter names you defined on OneLogin as well.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/19053401940243" alt="mceclip2.png"></p>
<p> </p>
<p> </p>
<h3 id="h_01HQ07TWN8H88RKD636ATB1X4A"><strong>That's it!</strong></h3>
<p>You have configured SAML 2.0 for OptiSigns with OneLogin.</p>
<p>Now your users can log in using the subdomain that you configured (in this case it was <a href="https://advanced.optisigns.net/signIn">https://advanced.optisigns.net/signIn</a>).</p>
<p>You can share the URL with your users and they can log in with their SSO credentials.</p>
<p> </p>
<p>If you have any additional questions or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self">support@optisigns.com</a></p>
<p> </p>