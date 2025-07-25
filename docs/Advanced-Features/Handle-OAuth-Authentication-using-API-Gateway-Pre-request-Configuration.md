<h3 id="h_01JNHD3FT6QVAV5CM0YGMM5YWR">In this article, we will explain how to set up a Pre-request to retrieve an OAuth 2.0 access token for connecting to an API using an API Gateway.</h3>
<p>OptiSigns API Gateway allows for OAuth authentication via Pre-request. This gives users the capability to consume API that requires OAuth authentication or similar.</p>
<p>To get started, you'll need to set up an API request. Hover over <strong>Account Name <span id="docs-internal-guid-e0fb68c4-7fff-1742-2ee5-6f88957884ce">→</span> More </strong><strong><span id="docs-internal-guid-e0fb68c4-7fff-1742-2ee5-6f88957884ce">→</span></strong><span id="docs-internal-guid-e0fb68c4-7fff-1742-2ee5-6f88957884ce"> Click</span><strong> DataSources</strong>:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/39080869728915" alt="how to navigate to datasource"></p>
<p>From there, hit <strong>Add Request</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/39080900410515" alt="datasources add request button"></p>
<p>Create a <strong>GET </strong><strong>Request</strong> and input your API endpoint, then click <strong>Pre-request:</strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/39080869729555" alt="optisigns api request form pre-request"></p>
<p>Within the Pre-request field, input the following code:</p>
<pre>const body = {<br>  "grant_type": "client_credentials",<br>  "client_id": "&lt;CLIENT_ID&gt;",<br>  "client_secret": "&lt;CLIENT_SECRET&gt;"<br><br>};<br>const params = Object.keys(body || {}).map((key) =&gt; {<br>        return key + '=' + body[key];<br>      }).join('&amp;');<br><br>const {data, headers} = await os.postRequest("&lt;OAUTH_AUTHENTICATION_URL&gt;", params,{headers: {'content-type': 'application/x-www-form-urlencoded'}});<br>const token = 'Bearer' + data.access_token;<br>os.context.set("request.headers.authorization", token);</pre>
<p><strong>Notes:</strong></p>
<ul>
<li>"grant_type": Use "client_credentials" ., because "client_credentials" is the grant type in OAuth for server-side integration without user interaction.</li>
<li>&lt;CLIENT_ID&gt; and &lt;CLIENT_SECRET&gt; refers to the user's code for the API being accessed, this will need to be provided by the user.</li>
<li>&lt;OAUTH_AUTHENTICATION_URL&gt; refers to the URL the access token is being retrieved from. This URL will need to be provided by the user.</li>
</ul>
<p>Now configure the <strong>Header</strong>:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/39080900411795" alt="properly configured API header"></p>
<p>With this and the rest of the required fields filled out, you've properly configured your Pre-request. Hitting <strong>Run Test</strong> should return a <strong>200 OK</strong> Response.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/39080869736211" alt="successful api request"></p>
<p>If so, hit <strong>Save </strong>to finish your API Request.</p>
<h3 id="h_01JNHK93FEN4N6V7CT2XW4VEV5">That's all!</h3>
<p>If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self">support@optisigns.com</a>.</p>