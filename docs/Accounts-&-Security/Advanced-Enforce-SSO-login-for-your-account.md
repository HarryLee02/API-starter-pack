<h3 id="h_01JJD0EAPZKF1VRP670X9DRS54">In this article, we'll explain how to enforce SSO logins for your OptiSigns account.</h3>
<ul>
<li><a href="#BasicSSO">Setting Up Basic SSO Enforcement (Microsoft, Facebook, Google)</a></li>
<li><a href="#SAML">Setting Up SAML SSO Enforcement (MS Entra ID, Okta, OneLogin, Google Workspace)</a></li>
</ul>
<p>By default, OptiSigns allows the use of Google, Facebook, or Microsoft accounts to access the OptiSigns portal:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37792885011987" alt="optisigns sso options" width="323" height="363"></p>
<p>However, some organizations have requirements to enforce SSO login for two-factor authentication and password protection purposes. OptiSigns supports this through Microsoft Entra ID and Google GSuite, as well as various SAML options requiring custom branding.</p>
<hr>
<p><a name="BasicSSO"></a></p>
<h2 id="h_01JJD0FG671WECG1BZM30QD29G">Setting Up Basic SSO Enforcement</h2>
<p>To set up basic SSO enforcement, go to the <strong>Preferences </strong>page in your OptiSigns portal:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37792885015699" alt="optisigns preferences tab" width="186" height="383"></p>
<p>You'll find the <strong>Enforce Account SSO </strong>option under the "General" section, right at the top of the page.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37792931285523" alt="optisigns enforce sso option"></p>
<p>Clicking on this will display several drop down options:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37792931288339" alt="optisigns enforce sso dropdown options"></p>
<p>Selecting either option will require any users logging on to OptiSigns to do so with their Google or Microsoft account. If a user tries to log in in any other way, they'll receive this error:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/1500001233801" alt="optisigns failed login error example" width="304" height="401"></p>
<p>For more information, see our guide on <strong><a href="https://support.optisigns.com/hc/en-us/articles/360046356113-Advanced-Security-Managing-User-Roles#AddingorInviting" target="_blank" rel="noopener noreferrer">User Management</a></strong>.</p>
<p><strong>Notes:</strong> You will have to use the official <a href="https://app.optisigns.com/">https://app.optisigns.com/</a> to log in to enforce SSO. You cannot use a custom domain with Enforce SSO, as the custom domain URL does not have an SSO login.</p>
<hr>
<p><a name="SAML"></a></p>
<h2 id="h_01JJD0MHAMZS9BTKKG7M44R941">Setting Up SAML SSO Enforcement (MS Entra ID, Okta, OneLogin, Google Workspace)</h2>
<div>
<table style="width: 100%;">
<tbody>
<tr>
<td>
<strong>NOTE: </strong> This feature is available to <strong>Pro Plus</strong>, <strong>Engage</strong>, and <strong>Enterprise </strong>plan users.</td>
</tr>
</tbody>
</table>
</div>
<p>Setting up SAML SSO enforcement requires setting up a subdomain, then configuring your settings on your client of choice.</p>
<p>We have numerous articles covering this process, as well as general best practices:</p>
<ul>
<li><a href="https://support.optisigns.com/hc/en-us/articles/4407128433299-SAML-integration-strategy-best-practice" target="_blank" rel="noopener noreferrer"><strong>SAML Integration Strategy and Best Practices</strong></a></li>
<li><a href="https://support.optisigns.com/hc/en-us/articles/4407252213395-How-to-Set-Up-SAML-2-0-with-OptiSigns-and-MS-Entra-ID-formerly-Azure-AD" target="_blank" rel="noopener noreferrer"><strong>Microsoft Entra ID SAML 2.0 SSO Setup</strong></a></li>
<li><a href="https://support.optisigns.com/hc/en-us/articles/4404590815635-How-to-set-up-SAML-2-0-with-OptiSigns-and-Okta" target="_blank" rel="noopener noreferrer"><strong>Okta SAML 2.0 SSO Setup</strong></a></li>
<li><a href="https://support.optisigns.com/hc/en-us/articles/4407386819731-How-to-set-up-SAML-2-0-with-OptiSigns-and-OneLogin" target="_blank" rel="noopener noreferrer"><strong>OneLogin SAML 2.0 SSO Setup</strong></a></li>
<li><a href="https://support.optisigns.com/hc/en-us/articles/4407493404307-How-to-set-up-SAML-2-0-with-OptiSigns-and-Google-Workspace" target="_blank" rel="noopener noreferrer"><strong>Google Workspace SAML 2.0 SSO Setup</strong></a></li>
</ul>
<p>Please follow one of these guides to set up SSO via SAML.</p>
<h3 id="h_01JJD0YS5096Q00PCXCDY1Y0WF"><strong>That's all!</strong></h3>
<p>OptiSigns is the leader in <a href="https://www.optisigns.com/" target="_blank" rel="noopener noreferrer">digital signage software</a>. If you have any additional questions or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com">support@optisigns.com</a>.</p>