<p>With Pro Plus and Enterprise plans, you can configure SAML 2.0 with OptiSigns via Okta.</p>
<p>Assuming you already using Okta for identity management. If you have not used Okta, it is the leading identity management platform, you can learn more <a href="https://www.okta.com/intro-to-okta/" target="_self">here</a>.</p>
<p> </p>
<h3 id="h_01HQ077MARH2D0ZZTK1JYBQ4SA"><strong>Set up OptiSigns &amp; Okta:</strong></h3>
<p><strong>First, you need to do some setup in OptiSigns:</strong></p>
<p>If you don't have a subdomain yet, you can set up one by going to:<br><a href="https://app.optisigns.com/app/s/branding-settings">https://app.optisigns.com/app/s/branding-settings</a></p>
<p>Fill in the subdomain field and click Activate. After that, you can use this subdomain for "<br>You can also map your domain like digitalsigns.yourcompany.com by following this <a href="https://support.optisigns.com/hc/en-us/articles/1500000480302" target="_self">article</a>.</p>
<p>This will be the URL that you can share with your users so they can log in to use the app, once integration has set up. In our example, we will use <a href="https://advanced.optisigns.net/">https://advanced.optisigns.net/</a></p>
<p><img src="https://api.hubspot.com/filemanager/api/v2/files/161592480004/signed-url-redirect?portalId=20629229"></p>
<p>Next, go to the SAML Single Sign On setting page:</p>
<p><a href="https://app.optisigns.com/app/s/saml-settings">https://app.optisigns.com/app/s/saml-settings</a></p>
<p>Click Enable SAML SSO.</p>
<p>The settings are:</p>
<ul>
<li>Enable Username &amp; Password login: <span style="font-weight: 400;">Allow users to also log in with username/password. It’s recommended to disable it once integration is all done. As Admin/Owner, it's recommended that you keep at least 1 account with a password log in, in case there's issues, you can always log back in from app.optisigns.com to reconfigure.</span>
</li>
<li>Enable User Creation: <span style="font-weight: 400;">If users are authenticated, but do not exist in OptiSigns, they will be created in OptiSigns. You should enable this, because you likely already assign/approve users/groups to use OptiSigns, unless for some reason you want to be very strict and want to review the roles of users before they can start using OptiSigns</span>.</li>
<li>Enable User Override: <span style="font-weight: 400;">Every time a user logs in, if their group assignment has changed on SAML, OptiSigns will update, and override new profile settings.</span>
</li>
<li>Note the "Single Sign On URL" and "Audience URI (SP Entity ID) URL", you will need this to use in Okta later.</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/28207766414227"></p>
<p> </p>
<p><strong>Next, add OptiSigns as an App to your Okta account:</strong></p>
<p>Log in to your Okta account as admin -&gt; Application</p>
<p>Or go to: <a href="https://optisigns-admin.okta.com/admin/apps/active">https://optisigns-admin.okta.com/admin/apps/active</a></p>
<p>Click Create App Integration</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4404598581779" alt="mceclip0.png"></p>
<p>Select SAML 2.0</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4404590829203" alt="mceclip1.png"></p>
<p>Enter App name: OptiSigns</p>
<p>If you want to upload a logo, you can use our logo <a href="https://download.optisignsapp.com/marketing/optisigns-logo.png" target="_blank" rel="noopener noreferrer">here</a>.</p>
<p>Click Next</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4404590844691" alt="mceclip2.png"></p>
<p>In "Single sign-in URL" and "Audience URI (SP Entity ID)", these are the URL that you have in <a href="https://app.optisigns.com/app/s/saml-settings">https://app.optisigns.com/app/s/saml-settings</a><br>Check "Use this for Recipient URL and Destination URLs"</p>
<p>Click Next.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4404608330003" alt="mceclip5.png"></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/28207766417811"></p>
<p>The last step is just informational for Okta to know how you are using the app.</p>
<p>Select "I'm an Okta customer adding an internal app" as OptiSigns is now an internal app in your organization.</p>
<p>Click Next.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4404615741075" alt="mceclip8.png"></p>
<p> </p>
<p>Then click "View Setup Instruction"</p>
<p><img src="https://api.hubspot.com/filemanager/api/v2/files/161591154242/signed-url-redirect?portalId=20629229"></p>
<p>Copy these 3 fields and paste into OptiSigns' SAML config page:</p>
<ul>
<li>Identity Provider Single Sign-On ULR -&gt; OptiSigns: SAML 2.0 Endpoint (HTTP)</li>
<li>Identity Provider Issuer -&gt; OptiSigns: Identity Provider Issuer</li>
<li>X.509 Certificate -&gt; OptiSigns: Public Certificate</li>
</ul>
<p><img src="https://support.optisigns.com/hc/article_attachments/4404615786259" alt="okta-config.png"></p>
<p> </p>
<p>Lastly, set the "Sign In Button label", this is the text of the button you want your users to see in their login portal. Use something descriptive like "Log in with Okta" "Sign in with SSO" or something your user is familiar with.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4404615885331" alt="okta-config-2.png"></p>
<p>Click Save</p>
<p>Now your login portal &amp; integration are all setup.</p>
<p>Next, you need to assign users, and groups that can use OptiSigns.</p>
<p> </p>
<h4 id="h_01HQ077MARZ8Z614Y50E9G1WZK"><strong>Assign &amp; map users, and groups from Okta to OptiSigns</strong></h4>
<p>It's not required, but recommended to create groups of users to be assigned, and map to OptiSigns Roles, and Teams so they will automatically have the right role &amp; group.</p>
<p><strong>IMPORTANT NOTE: If you don't configure this, all users will be assigned User Role &amp; Default Team (screenshot see below)</strong></p>
<p> </p>
<p>To configure how OptiSigns should map the user groups to OptiSigns Roles by going to: <a href="https://app.optisigns.com/app/s/saml-settings">https://app.optisigns.com/app/s/saml-settings</a></p>
<p>Scroll to Advanced Settings and create a mapping.<br>Group Name (group names in Okta), Role (role in OptiSigns) mapping. <br><img src="https://support.optisigns.com/hc/article_attachments/4404820186003" alt="mceclip1.png"></p>
<p>It's best practice to create a group name prefix with Optisigns- and map to OptiSigns like below:</p>
<ul>
<li>optisigns-admins (SAML group) -&gt; OptiSigns role: Admin</li>
<li>optisigns-users (SAML group) -&gt; OptiSigns role: Users</li>
<li>optisigns-custom-role (SAML group) -&gt; OptiSigns custom role that you create</li>
</ul>
<p><strong>How to handle Unmapped users/groups:</strong></p>
<p>You can map the "Unmapped users/group" to No Team (Disabled)</p>
<p>This way they will receive an error when trying to log in and will have to reach out to Admins to get the correct teams, and roles assigned. This can be used as a safeguard, in case some users accidentally got assigned OptiSigns app but not the right groups.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4404812977171" alt="mceclip3.png"></p>
<p>Note that if you map a SAML group to a Team and then delete the team, it will result in new user being mapped to No Team and will have to contact you to be assigned to a team to use the app.</p>
<p> </p>
<p>Next, go to your Okta Admin portal. Click Applications -&gt; OptiSigns.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4404615820691" alt="mceclip11.png"></p>
<p>Click Assign -&gt; People or Groups to use this app. You can also configure your user to request to use the app, but that's beyond the scope of this article.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4404615832339" alt="mceclip12.png"></p>
<p>You can set up group mapping by going to General -&gt; SAML settings</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4404762241811" alt="mceclip2.png"></p>
<p>Click Next:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4404767623827" alt="mceclip3.png"></p>
<p>Creating these mappings will pass information to OptiSigns on the user's Name and Groups.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4404762334611" alt="mceclip4.png"></p>
<p>The "Attribute Statement" and "Group Attribute Statement" are corresponding to OptiSigns <a href="https://app.optisigns.com/app/s/saml-settings" target="_self" rel="undefined">https://app.optisigns.com/app/s/saml-settings</a></p>
<p>OptiSigns accept firstName, lastName, and group by default, but if you change these in Okta, you will need to match it here as well.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4404812916115" alt="mceclip2.png"></p>
<p><strong>Additional Note:</strong></p>
<p>If you want your user to login to the OptiSigns portal via OKTA portal, Okta does not support the IDP that is initiated. It will use the Bookmark App on Okta, You can follow this article to set up the Bookmark app: <a href="https://support.okta.com/help/s/article/How-do-you-create-a-bookmark-app?language=en_US">https://support.okta.com/help/s/article/How-do-you-create-a-bookmark-app?language=en_US</a></p>
<h4 id="h_01JH5W64QF8FQMHHK66NHKXHT2"><strong><span style="color: #666666;">I've made it into my OptiSigns account, but don't seem to have all the side menu options I'm used to. What’s going on?</span></strong></h4>
<p>It's likely you've signed on through your Branded Portal, using a URL similar to this one:</p>
<pre>https://app.optisigns.com/signIn/&lt;accountId&gt;</pre>
<p>You'll first need to find your OptiSigns Account ID. To do this, simply find a paired screen, and hit <strong>Edit <span id="docs-internal-guid-af17cc22-7fff-76d0-f908-3ba6ea4fe31b">→</span> Advanced <span id="docs-internal-guid-af17cc22-7fff-76d0-f908-3ba6ea4fe31b">→</span> More</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/38962229904659" alt="edit screen advanced more"></p>
<p>Click <strong>Device Info:</strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/38962229906835" alt="info button edit screen"></p>
<p>Find the <strong>"accountId"</strong> number, then write it down somewhere. You'll be needing it soon.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/38962235455635"></p>
<p>Now copy the following URL, being sure to substitute your account ID where appropriate:</p>
<pre>https://app.optisigns.com/signIn/&lt;accountId&gt;</pre>
<p>Now you'll want to set this URL up as an Okta bookmark. You can follow this article to set up the Bookmark app: <a href="https://support.okta.com/help/s/article/How-do-you-create-a-bookmark-app?language=en_US">https://support.okta.com/help/s/article/How-do-you-create-a-bookmark-app?language=en_US</a></p>
<h3 id="h_01HQ077MARE4CXPATEGHTWJC2P"><strong>That's it!</strong></h3>
<p>You have configured SAML 2.0 for OptiSigns with Okta.</p>
<p>Now your users can log in using the subdomain that you configured (in this case it was <a href="https://advanced.optisigns.net/signIn">https://advanced.optisigns.net/signIn</a>).</p>
<p>You can share the URL with your users and they can log in with their SSO credentials.</p>
<p> </p>
<p>If you have any additional questions or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self">support@optisigns.com</a></p>
<p> </p>