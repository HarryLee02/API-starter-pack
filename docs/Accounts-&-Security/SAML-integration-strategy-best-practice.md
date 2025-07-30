<p>There are many ways to implement SAML to manage users and access OptiSigns with your IDP.</p>
<p>Here are some high-level best practices with OptiSigns that may help you to plan your integration and reduce overhead, and manual work later.</p>
<p> </p>
<p>This article only focuses on the strategy &amp; approach, for detailed step-by-step configuration, you can refer to <a href="https://support.optisigns.com/hc/en-us/articles/4404590815635" target="_self">this guide</a>.</p>
<p> </p>
<h4 id="h_01HQ071K10F3FT8C9B569T1S6S"><strong>Create a backup Admin account during set up:</strong></h4>
<p>During set up, we recommend leaving Enable Username &amp; Password login, and creating an Admin account with username/password to log back in and config, in case you accidentally lock yourself out by missing assignments of roles or groups.</p>
<p>You can disable this account later once your implementation is completed.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4407128153235" alt="mceclip0.png" width="314" height="127"></p>
<p>In this case, you are planning not to use email as the unique identifier for the user, and use a username or employee ID instead. We recommend having this on, so the account owner and admin account will be able to manage the account without interruption, e.g. forgetting the password, or an issue with identifying the provider. </p>
<p> </p>
<h4 id="h_01HQ071K11FD3T93ZKW59HSXDB"><strong>There are 2 Strategies for using SAML:</strong></h4>
<p><strong>1) As an Authentication &amp; Authorization Service </strong>to enforce identity verification like above, but also enforce user, team, and role mapping in OptiSigns, With this approach you will map all users to groups in your IDP, and map the IDP groups to OptiSigns teams/roles. When there's a change in IDP like a user is added or moved group, it will automatically reflect in OptiSigns. <strong>We recommend this approach</strong>.</p>
<p>To implement this, check "Enable User Override", with this enabled, every time a user logs in using SAML, OptiSigns will check to see if their group assignment has changed, and enforce that accordingly, also if their name has changed, updated, it will also update OptiSigns.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4407135779603" alt="mceclip1.png" width="377" height="224"></p>
<p>Map all your appropriate groups to roles &amp; team in OptiSigns.</p>
<p>For example we have 3 groups:</p>
<ul>
<li>Marketing West Coast - users responsible for managing screens, content for West region</li>
<li>Marketing East Coast - user responsible for manage screens, content for East region</li>
<li>IT Support - Admin that can support both region and do other admin tasks</li>
</ul>
<p>The mapping should be like below.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4407128634643" alt="mceclip3.png"></p>
<p>With this set up, if a user belong to Marketing West Coast, later moved to Marketing East Coast, you just need to update your IDP move him/her from Marketing West Coast to Marketing East Coast, next time the user log in, he/she now belong to and can only see "Marketing West Coast" team content in OptiSigns.</p>
<p> </p>
<p><strong>2) As Authentication Service Only</strong> to enforce your MFA, Password policy, and remove user will no longer have access to OptiSigns. You will still can assigns, manage these users to Teams, Roles in OptiSigns. This approach is quick to set up and flexible as you can quickly move users around in OptiSigns, but when users moved around in your IDP, you will have to remember to move them around in OptiSigns as well, if that's a requirement.</p>
<p>To implement this, uncheck "Enable User Override"</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4407136124435" alt="mceclip4.png" width="338" height="204"></p>
<p>This way, in the example above. When a user move from Marketing West Coast to Marketing East Coast.</p>
<p>You will need to go to OptiSigns and move the user's team assignment, if that's required.</p>
<p>Also if when the user update, change their name, you will have to update OptiSigns as well to keep it in sync.</p>
<p> </p>
<h4 id="h_01HQ071K11M4WVEWY4KHQ29JFK"><strong>Enable User Creation:</strong></h4>
<p>We recommend to keep this option checked. When this option is enabled, if users authenticated and SAML setting map the user to a team, role that can use OptiSigns, the user will be created automatically.</p>
<p>If disabled, you will have to create each user first in OptiSigns before they can log in with SAML SSO.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4407136156819" alt="mceclip5.png" width="389" height="247"></p>
<p>In the example above, if there are 20 users belong to Marketing West Coast group in your IDP, and Marketing West Coast is mapped to the Marketing West Coast team in OptiSigns.</p>
<p>If user A belong to Marketing West Coast group logs in, he/she will be created in OptiSigns and can start working right away to with West Coast Team screens and content.</p>
<p>The other 19 users are not created in OptiSigns until they attempt to log in.</p>
<p>You can also map the "Unmapped users/groups" to "No Team (Disable)", this way if a user belong to some other group in your IDP like say "Sales West Coast" try to log in, they will get an error and the user is not created in OptiSigns.</p>
<p>This way you can keep the system clean and only necessary users that using the app are replicated.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4407136240659" alt="mceclip6.png"></p>
<p> </p>
<p>If you have any questions or need help with SAML integration please feel free to reach out to us at <a href="mailto:support@optisigns.com">support@optisigns.com</a></p>
<p> </p>