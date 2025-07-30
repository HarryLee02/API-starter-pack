<h3 id="h_01JH5W64QFV28ZK99E0RN5WX8G"><span style="color: #434343;">In this article, we will provide a step-by-step guide to setting up SAML 2.0 with Microsoft Entra ID for use with OptiSigns.</span></h3>
<ul>
<li>
<a href="#Subdomain">Set Up OptiSigns Subdomain and SAML SSO Settings</a>
<ul>
<li><a href="#CustomSubdomain">Setting up a Custom Subdomain</a></li>
<li><a href="#SAMLssoSettings">Setting up SAML SSO Settings</a></li>
</ul>
</li>
<li><a href="#EntraIDPortal">Add OptiSigns as an App in Azure Portal</a></li>
<li>
<a href="#AssignMap">Assign and Map Users and Groups from Azure to OptiSigns (OPTIONAL)</a>
<ul>
<li><a href="#Unmapped">How to Handle Unmapped Users and Groups (OPTIONAL)</a></li>
<li>
<a href="#AttributesClaims">Managing Attributes &amp; Claims in Microsoft Azure (OPTIONAL)</a>
<ul>
<li><a href="#GroupClaims">Creating Group Claims (OPTIONAL)</a></li>
<li><a href="#UserClaims">Customizing Claims for Use with OptiSigns (OPTIONAL)</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#Office.com">Setting Up OptiSigns Login to Appear in Office.com (OPTIONAL)</a></li>
<li><a href="#FAQs">Frequently Asked Questions</a></li>
</ul>
<div>
<table style="width: 100%;">
<colgroup> <col> </colgroup>
<tbody>
<tr>
<td>
<strong>NOTE: </strong> This feature is available to <strong>Pro Plus</strong>, <strong>Engage</strong>, and <strong>Enterprise </strong>plan users.</td>
</tr>
</tbody>
</table>
</div>
<p>SAML (Security Assertion Markup Language) 2.0 allows a single authorization to access multiple systems. This can be configured to allow easy access to OptiSigns digital signage through your Microsoft Entra ID. Entra ID will act as the IDP (Identity Provider), with OptiSigns will work as the SP (Service Provider). Here is a quick video showing how to set up SAML 2.0 with Entra ID (when it was known as Azure AD):</p>
<p><iframe src="//www.youtube-nocookie.com/embed/EG55Th1oFNE" width="560" height="315" frameborder="0" allowfullscreen=""></iframe></p>
<hr>
<p><a name="Subdomain"></a></p>
<h2 id="h_01JH5W64QFHKSBWAFKND84GHD6">Set Up OptiSigns Subdomain and SAML SSO Settings</h2>
<p>To begin, you’ll need to perform some functions within the OptiSigns app, including:</p>
<ul>
<li>Creating a Custom Subdomain</li>
<li>Setting up SAML SSO Settings</li>
</ul>
<p>Now, let’s begin.</p>
<p><a name="CustomSubdomain"></a></p>
<h3 id="h_01JH5W64QFM1DKDTCSQQHXPNZG"><span style="color: #434343;">Setting up a Custom Subdomain</span></h3>
<p>First, ensure you have an OptiSigns subdomain. This can be obtained by going to the <a href="https://app.optisigns.com/app/s/branding-settings"><span class="wysiwyg-underline" style="color: #1155cc;">Branding Settings</span></a> page.</p>
<p>Fill in the subdomain field and click <strong>Activate</strong>. Now you can use this subdomain for a variety of functions, including SAML setup. You can also map your domain by following our article on <a href="https://support.optisigns.com/hc/en-us/articles/1500000480302-Advanced-Custom-Domain-mapping"><span class="wysiwyg-underline" style="color: #1155cc;">Custom Domain mapping</span></a>.</p>
<p>This subdomain will be the URL to share with your users so they can log in to use the app after integration has been set up.</p>
<p>For this example, we will use <a href="https://optisignsdemo-ad.optisigns.net/"><span class="wysiwyg-underline" style="color: #1155cc;">https://optisignsdemo-ad.optisigns.net/</span></a> as our URL.</p>
<p><a name="SAMLssoSettings"></a></p>
<h3 id="h_01JH5W64QFKGT30VM4MVZRF5KP"><span style="color: #434343;">Setting up SAML SSO Settings</span></h3>
<p>Go to the SAML Single Sign-On Setting Page:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186635027731" alt="go to saml single sign on page" width="253" height="438"></p>
<p>Now enable <strong>Enable SAML SSO</strong>. There should be a green checkmark next to the option. This will expand the options available to you.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186682762387" alt="saml sso settings checklist" width="597" height="263"></p>
<p>The other settings are:</p>
<ul>
<li>
<strong>Enable Username &amp; Password Login - </strong>Allow users to also log in with username/password. We recommend disabling this once integration is finished. As Admin/Owner, it’s recommended to keep at least 1 account with a password login in case there are issues. You can use this account to login directly to the app to reconfigure if necessary.</li>
<li>
<strong>Enable User Creation - </strong>If users are authenticated but do not exist in OptiSigns, they will be created in the OptiSigns app. We recommend enabling this unless you wish to be extremely strict and want to review the roles of users before they can start using OptiSigns.</li>
<li>
<strong>Enable User Override - </strong>Every time a user logs in, OptiSigns will check their group assignment. If it has changed on SAML, OptiSigns will update their permissions within the app.</li>
</ul>
<p>Next, note your <strong>Single Sign On URL </strong>and <strong>Audience URI (SP Entity ID) URL</strong>. You will need to use these later.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186635040403" width="624" height="103"></p>
<hr>
<p><a name="EntraIDPortal"></a></p>
<h2 id="h_01JH5W64QFFHS6CQ9RV937E0Q7">Add OptiSigns as an App in Microsoft Entra ID Portal</h2>
<p>Log in to your Microsoft Azure portal as an administrator, then navigate to <strong>Enterprise Applications</strong>.</p>
<p>Click <strong>New Application</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186682790803" alt="creating new enterprise application ms azure" width="624" height="309"></p>
<p>Select <strong>Create your application</strong>. This pops up a sidebar on the right. Inside, input “OptiSigns” as the name of the app, and choose <strong>Integrate any other application you don’t find in the gallery (Non-gallery)</strong>. Finally, hit <strong>Create</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186682801427" alt="create own application ms azure" width="624" height="281"></p>
<p>This will take a moment, but you’ll eventually be brought to an Overview screen.</p>
<p>Click <strong>Set up single sign on.</strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186682808851" alt="setting up single sign on ms azure" width="624" height="239"></p>
<p>Click <strong>SAML</strong>. This will begin the setup of SAML-based Sign-on.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186635065235" alt="saml ms azure" width="624" height="227"></p>
<p>Here, click <strong>Edit</strong> in the Basic SAML Configuration section. This is where you should provide the Single Sign On URL and SP Entity ID you got <a href="#SAMLssoSettings" target="_blank" rel="noopener noreferrer">in the last step</a>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186635074707" alt="basic saml configuration" width="624" height="260"></p>
<p>Place the Single Sign On URL under <strong>Reply URL </strong>and the SP Entity ID under <strong>Identifier</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186682845331" alt="identifier and reply URL saml config ms azure" width="624" height="385"></p>
<p>Next, note the next two sections: <strong>SAML Certificates </strong>and <strong>Set up OptiSigns</strong>. You’ll need to obtain three key pieces of information:</p>
<ol>
<li>Certificate (Base64)</li>
<li>Login URL</li>
<li>Microsoft Entra Identifier</li>
</ol>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186682850067" alt="three key pieces of information ms azure" width="624" height="417"></p>
<p>These will need to be maintained within the OptiSigns app, in the SAML SSO Settings page.</p>
<p>Now go back to your OptiSigns account and input these three pieces of information in the following places:</p>
<ol>
<li>
<strong>Login URL </strong>should go under <strong>SAML 2.0 Endpoint (HTTP)</strong>
</li>
<li>
<strong>Microsoft Entra Identifier </strong>should go under <strong>Identity Provider Issuer</strong>
</li>
<li>The content of the downloaded <strong>Certificate (Base64) </strong>should be pasted under <strong>Public Certificate</strong>.</li>
</ol>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186682855955" alt="setup SAML authentication optisigns" width="624" height="325"></p>
<p>With this, your login portal and integration are all set up. If this is all you need, you’re done. If you’d like to manage users, groups, and teams, keep reading.</p>
<hr>
<p><a name="AssignMap"></a></p>
<h2 id="h_01JH5W64QFKG356APZRQVA6GHT">Assign and Map Users and Groups from Azure to OptiSigns (OPTIONAL)</h2>
<p>We highly recommend creating groups of users to be assigned within Azure to be automatically mapped to OptiSigns with the correct role and group.</p>
<div>
<table style="width: 100%;">
<colgroup> <col> </colgroup>
<tbody>
<tr>
<td>
<strong>NOTE: </strong>Without configuring this, all users will be assigned User Role and Default Team. You will have to manually change their roles and teams within the OptiSigns app.</td>
</tr>
</tbody>
</table>
</div>
<p>Head back to the <a href="https://app.optisigns.com/app/s/saml-settings"><span class="wysiwyg-underline" style="color: #1155cc;">SAML settings page</span></a> within OptiSigns. Scroll to <strong>Advanced Settings </strong>and you should see this:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186635103379" alt="group mapping optisigns" width="624" height="179"></p>
<p>By default, unmapped users/groups become Users within the Default Team in OptiSigns. To link OptiSigns to Azure, either create a new mapping by clicking <strong>Add</strong> or edit one of the existing Group mappings.</p>
<p>The “Group Name” within OptiSigns corresponds to the “Group ID” within Azure. To find this information, go to your Azure Portal and select <strong>Groups</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186682869779" alt="groups tab ms azure" width="438" height="391"></p>
<p>Your Object ID can be found here for each group you’ve created.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186635118611" alt="groups with object id noted" width="624" height="271"></p>
<p>This Object ID should be input into the Group Name field within OptiSigns. However, we recommend creating a group specifically for OptiSigns with an OptiSigns- prefix and map these to OptiSigns like this:</p>
<ul>
<li>optisigns-admins (SAML group) → OptiSigns role: Admin</li>
<li>optisigns-users (SAML group) → OptiSigns role: Users</li>
<li>optisigns-custom-role (SAML group) → OptiSigns custom role that you create</li>
</ul>
<p>Once finished, it should resemble this:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186682886547" alt="filled out group mapping optisigns" width="624" height="228"></p>
<p>You can create as many groups and roles as you like.</p>
<p><a name="Unmapped"></a></p>
<h3 id="h_01JH5W64QFGF6J7GXVXBCKMX13"><span style="color: #434343;">How to Handle Unmapped Users and Groups</span></h3>
<p>You may wish to map the “Unmapped users/groups” section to <strong>No Team (Disable)</strong>. This way, they will receive an error message when trying to login in and will have to reach out to Admins to get the correct team and role assigned. This is a useful safeguard in case certain users accidentally get assigned the OptiSigns app but not the correct group.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186635129363" alt="unmapped users/groups with no team selected" width="624" height="103"></p>
<div>
<table style="width: 100%;">
<colgroup> <col> </colgroup>
<tbody>
<tr>
<td>
<strong>NOTE: </strong>If you map an SAML group to a Team, then delete the Team, it will result in new users being mapped to No Team. They will have to contact you to be assigned to a team in order to use the app.</td>
</tr>
</tbody>
</table>
</div>
<p><a name="AttributesClaims"></a></p>
<h3 id="h_01JH5W64QFQR07M3C5J5Z3ENTA"><span style="color: #434343;">Managing Attributes &amp; Claims in Microsoft Azure</span></h3>
<p>Editing the Attributes &amp; Claims in Microsoft Azure can give you even more control over the Users added to the group, and is a valuable tool.</p>
<p>To begin, go to the Azure portal. Click <strong>Enterprise Applications </strong>→ <strong>OptiSigns </strong>→ <strong>Single sign-on</strong>. Scroll down to Section 2: User Attributes &amp; Claims. This is where you maintain the mapping of these attributes.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186682899603" alt="user attributes and claims ms azure" width="624" height="256"></p>
<p>Within this section, there are two main things to customize:</p>
<ul>
<li>Group Claims</li>
<li>User Attributes</li>
</ul>
<p>We’ll walk you through each.</p>
<p><a name="GroupClaims"></a></p>
<h4 id="h_01JH5W64QFH21XYCJYT4SFKZJG"><span style="color: #666666;">Creating Group Claims for Use with OptiSigns</span></h4>
<p>To create a Group Claim, first hit <strong>Add a group claim</strong>:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186682904595" alt="add group claim ms azure" width="624" height="360"></p>
<p>When you create a Group:</p>
<ol>
<li>Select <strong>Groups assigned to the application</strong> under “Which groups associated with the user should be returned in the claim?”</li>
<li>(Optional) Input the name “groups” in the “Customize the name of the group claim” and leave the Namespace section blank.</li>
</ol>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186635155987" alt="group claim settings ms azure" width="624" height="340"><br>That’s all for creating Group claims.</p>
<p><a name="UserClaims"></a></p>
<h4 id="h_01JH5W64QFV72FHGMZ7CFWAYZR"><span style="color: #666666;">Customizing User Claims for Use with OptiSigns</span></h4>
<p>These mappings will pass information to OptiSigns on the user’s Name and Group:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186635162003" alt="managing user claims ms azure" width="624" height="221"></p>
<p>The Claim names are, by default, represented by a URL. The Type will be given as SAML, with the Value corresponding to identifying information about the user, including:</p>
<ul>
<li>user.givenname</li>
<li>user.groups (only if setup - see above section)</li>
<li>user.mail</li>
<li>user.userprincipalname</li>
<li>user.surname</li>
</ul>
<p>These Claim names correspond to this section under <strong>Advanced Settings </strong>on the SAML SSO Settings page:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186635168659" alt="advanced settings optisigns saml sso settings page" width="624" height="148"></p>
<p>OptiSigns accepts First Names, Last Names, and Groups by default.</p>
<p>These values correspond to the <strong>Namespace</strong> of the claim. So, in other words, if the Value corresponding to the firstName (user.givenname) is a URL, you will have to paste the entire URL into OptiSigns. It is possible, however, to change the Namespace to something more manageable.</p>
<p>In Azure, click on any of these claims to Manage them.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186635174931" alt="ms azure manage claims" width="624" height="161"></p>
<p>To eliminate the URL, simply delete it from the Namespace field, then hit <strong>Save</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186635182483" alt="eliminate URL ms azure claim" width="624" height="76"></p>
<p>This will replace the URL in the Namespace with the Name. This is a much easier piece of information to manage.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186635189523" alt="claims after removing url ms azure" width="624" height="183"></p>
<p>These can now be mapped, like so:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186635199123" alt="proper user mapping in optisigns example" width="624" height="148"></p>
<p>Finally, go to the <strong>Users and groups </strong>section within Azure and assign your groups to the OptiSigns Enterprise app.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186682960019" alt="add user/group" width="624" height="340"></p>
<hr>
<p><a name="Office.com"></a></p>
<h2 id="h_01JH5W64QFBXHZWGH79T3NGN49">Setting Up OptiSigns Login to Appear in Office.com</h2>
<p>It’s often convenient to have the OptiSigns app appear as a clickable option on your company’s Office.com portal.</p>
<p>To set this up, you'll first need to find your OptiSigns Account ID. To do this, simply find a paired screen, and hit <strong>Edit <span id="docs-internal-guid-af17cc22-7fff-76d0-f908-3ba6ea4fe31b">→</span> Advanced <span id="docs-internal-guid-af17cc22-7fff-76d0-f908-3ba6ea4fe31b">→</span> More</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/38825933298579" alt="edit screen advanced more"></p>
<p>Click <strong>Device Info:</strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/38825917033875" alt="info button edit screen"></p>
<p>Find the <strong>"accountId"</strong> number, then write it down somewhere. You'll be needing it soon.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/38825917043475"></p>
<p>Now copy the following URL, being sure to substitute your account ID where appropriate:</p>
<pre>https://app.optisigns.com/signIn/&lt;accountId&gt;</pre>
<p>Next, head back to your Azure portal, and go to <strong>SAML-based Sign-on</strong>. Once there, find <strong>Basic SAML Configuration </strong>and hit <strong>Edit. </strong>This will open up a sidebar. Simply paste/type your URL into the <strong>Sign on URL (Optional) </strong>and <strong>Relay State </strong>(Optional) fields.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/38838224681235"></p>
<p>This will allow the OptiSigns app to appear in your Microsoft Office portal. This will also provide the full range of options for your side menu.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186635219219" alt="optisigns app in ms office portal" width="624" height="156"></p>
<hr>
<p><a name="FAQs"></a></p>
<h2 id="h_01JH5W64QFXMPPYM2D8Q7TE5AZ">Frequently Asked Questions</h2>
<p>Here, we’ll answer some of the most common questions we get around this topic.</p>
<h4 id="h_01JH5W64QFZMPNKVHX3ZVC3PT8"><span class="wysiwyg-font-size-large"><strong><span style="color: #666666;">I Got this Error Message. Help?</span></strong></span></h4>
<p><span style="color: #188038;">Unable to process request due to missing initial state. This may happen if browser sessionStorage is inaccessible or accidentally cleared. Some specific scenarios are - 1) Using IDP-Initiated SAML SSO. 2) Using signInWithRedirect in a storage-partitioned browser environment.</span></p>
<p><span style="color: #188038;"><img src="https://support.optisigns.com/hc/article_attachments/37186635223443" alt="optisigns common error message" width="624" height="92"></span></p>
<p>This error appears for one of two reasons:</p>
<ol>
<li>The wrong URL was input. This is frequently (https://auth.optisigns.com/__/auth/handler)</li>
<li>The user has tried to access the OptiSigns portal from Office.com without setting up SAML SSO in Microsoft Azure correctly.</li>
</ol>
<p>The easiest way to solve this problem is to login through your branded URL.</p>
<p><span class="wysiwyg-underline" style="color: #1155cc;"><img src="https://support.optisigns.com/hc/article_attachments/37186682989075" alt="branded url example" width="624" height="348"></span></p>
<p>This will be unique to your organization. For more information, follow the steps outlined in the “Add OptiSigns as an App in Microsoft Entra ID Portal” section.</p>
<h4 id="h_01JH5W64QF4NFEDC8GRP2N2XM8"><strong><span style="color: #666666;">It’s Saying I Don’t Belong to a Team/Group. How Can I Fix This?</span></strong></h4>
<p>This error has to do with group mapping. To start, follow all the steps outlined in the “Assign and Map Users and Groups” section above.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37188678189203" alt="team/group error message" width="307" height="339"></p>
<p>If you’re still having trouble, check your Group names. In Azure, that’s Object ID:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186635239699" alt="ms azure groups tab object id" width="624" height="273"></p>
<p>Check the desired User’s Attributes &amp; Claims and make sure their Group name is assigned as <strong>Groups assigned to the application</strong>.</p>
<p><strong><img src="https://support.optisigns.com/hc/article_attachments/37186635254803" alt="group claims error fix" width="624" height="339"></strong></p>
<p>Next, check if the Claim has been set up properly:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186683011731" alt="proper claims names ms azure" width="624" height="320"></p>
<p>The above values should match these within the OptiSigns portal:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186683017875" alt="proper claims names optisigns" width="624" height="211"></p>
<p>Finally, make sure the user and group have been added to the application within MS Azure:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/37186635286419" alt="user and group added to app within ms azure" width="624" height="307"></p>
<p>This should resolve the issue.</p>
<h4 id="h_01JH5W64QF8FQMHHK66NHKXHT2"><strong><span style="color: #666666;">I've made it into my OptiSigns account, but don't seem to have all the side menu options I'm used to. What’s going on?</span></strong></h4>
<p>It's likely you've signed on through your Branded Portal, using a URL similar to this one:</p>
<pre>https://app.optisigns.com/signIn/&lt;accountId&gt;</pre>
<p>Go ahead and follow the steps outlined <a href="#Office.com"><strong>here</strong></a> and this issue should resolve itself.</p>
<h3 id="h_01JH5W64QFF3P79H6H0454P2ZR"><strong>That's all!</strong></h3>
<p>You have configured SAML 2.0 for OptiSigns with Microsoft Entra.</p>
<p>You can share the URL with your users and they can log in with their SSO credentials.</p>
<p>If you have any additional questions or any feedback about OptiSigns, feel free to reach out to our support team at support@optisigns.com</p>