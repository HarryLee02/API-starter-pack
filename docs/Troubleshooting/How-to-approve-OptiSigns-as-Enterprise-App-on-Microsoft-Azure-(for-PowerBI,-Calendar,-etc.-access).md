<p>With OptiSigns, you can use PowerBI, Microsoft Outlook Calendar, OneDrive app to integrate your Dashboard, calendar or content from your OneDrive on to your digital signage screens.</p>
<p>In this article we will cover:</p>
<p>1) OptiSigns User/Admin: How to send request approval for OptiSigns to access your PowerBI, Calendar, etc.</p>
<p>2) Microsoft Azure Admin: How to approve the request.</p>
<p>Let's dive in.</p>
<h4 id="h_01HQ08B7MYK34W0HD3DB4T3NPB"><strong>1) OptiSigns User/Admin: How to send request approval for OptiSigns to access your PowerBI, Calendar, etc.</strong></h4>
<p>If you are using a work account from your organization, sometimes, your organization's Admin have set security workflow so that apps like OptiSigns will need to be reviewed by your  Microsoft Azure Admin before granting access to your organization resources (like PowerBI, Calendar, OneDrive).</p>
<p>In OptiSigns, when click Log In with Microsoft account, it will prompt a window like below.</p>
<p> </p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4403615938579" alt="mceclip1.png"></p>
<p>If you click "Request approval", this will send an email to your Microsoft Azure Admin to review and approve.</p>
<p>Please enter something meaningful so that they know who you are and what you want to use OptiSigns for. For example:</p>
<p><em>"We are looking to use OptiSigns Digital Signage to display PowerBI KPI Dashboard on big screens TVs in breakroom &amp; common areas. As Digital Signage use case, OptiSigns only read, display assets, OptiSigns will not modify, move, delete objects."</em></p>
<p>Then click "Request Approval"</p>
<p> </p>
<p>Your admin will be notified by Microsoft Azure automatically, but it's usually a good idea to send them an email as well. <strong>You can send your Admin a link to this article and refer to section #2 below for how to review &amp; approve.</strong></p>
<p>If some times have past, and the Request Approval Expires (by default it's 30 days, but it could be different based on your organization's settings)</p>
<p>You can repeat this whole process again to send a new request.</p>
<p> </p>
<h4 id="h_01HQ08B7N0WGR4YDYRFPMRAQ8H"><strong>2) Microsoft Azure Admin: How to approve the request.</strong></h4>
<p>As Microsoft Azure Admin, you will receive an email when a user request a 3rd party app like OptiSigns to access your organization resources.</p>
<p>You can click "Review request" to review.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4403616205715" alt="mceclip2.png"></p>
<p>Or you can log in to Azure portal -&gt; "Azure Active Directory" -&gt; "Enterprise applications" -&gt; "Admin consent requests".</p>
<p>You will see pending approval request there.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4403627418643" alt="mceclip5.png"></p>
<p>Click "Review permission &amp; consent"</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4403622874387" alt="mceclip6.png"></p>
<p>Review the permissions requested by OptiSigns. OptiSigns, as a digital signage application, only reads and displays assets. It will not modify, move, or delete objects. See our <a href="https://www.optisigns.com/privacy-policy" target="_blank" rel="noopener noreferrer">Privacy Policy</a> for more information.</p>
<p>Click <strong>Accept:</strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/4403627456531" alt="mceclip7.png"></p>
<p><strong>That's all!</strong> You have reviewed and approve OptiSigns to be used as Enterprise App in your organization.</p>
<p>You can notify your users who made the request that they can start using the requested app (Power BI, OneDrive, or Calendar) with OptiSigns now.</p>
<p>If users want to use more than 1 app (i.e. Power BI and OneDrive, then you will need to approve more than 1 time).</p>
<h3 id="h_01JK6MB1BDGMGEBXA8NG4GKRTY">Why does using Office 365, PowerBI, or other Microsoft App require giving OptiSigns Admin permission to use?</h3>
<p>OptiSigns uses Microsoft APIs for integration. In order for our integrations to work, the integration has to be approved by an administrator to be allowed in the Azure tenant. This is the same across all integrations using Microsoft APIs.</p>
<p>This administrator access is only needed for first time access. Once the OptiSigns app is approved for use in the Azure tenant, other users can use OptiSigns directly.</p>
<p><strong>References:</strong></p>
<p><a href="https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/configure-admin-consent-workflow">Configure the admin consent workflow - Azure Active Directory | Microsoft Docs</a></p>
<p><a href="https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/add-application-portal-configure">Quickstart: Configure properties for an application in your Azure Active Directory (Azure AD) tenant | Microsoft Docs</a></p>
<p> </p>
<p>If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self" rel="undefined">support@optisigns.com</a></p>
<p> </p>
<p> </p>
<p> </p>
<p> </p>