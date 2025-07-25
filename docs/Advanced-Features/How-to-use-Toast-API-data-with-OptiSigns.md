<h3 id="h_01J5B5T1WQ12TCW4BQW2R71CS9">Toast is one of the most common Point-of-Sale systems in North America. In this article, we'll explain how to set up API integration between your Toast system and OptiSigns.</h3>
<ul>
<li><a href="#Step1">Step 1: Preparation</a></li>
<li><a href="#Step2">Step 2: Authentication to Toast API</a></li>
<li><a href="#Step3">Step 3: Call the API to Get the Required Data from Toast</a></li>
<li><a href="#Step4">Step 4: Build the DMB Designer with OptiSync</a></li>
</ul>
<p>Toast provides an API for users to integrate POS data with other systems. With OptiSync, building auto-updating digital menu boards from your Toast API's data is simple.</p>
<p>Toast API requires a dynamically generated authentication token to be supplied with every API call, unlike many other POS systems that use a static API key. This adds some complexity to the integration that other POS systems don't have. However, using OptiSigns' API request and OptiSync, these added complexities are no trouble at all.</p>
<p>In this article, we'll provide a step-by-step guide on how to integrate your Toast API using OptiSigns API request, and how to create a DMB using OptiSync. Below are the high level steps we will follow:</p>
<p>1. Get required information from Toast portal</p>
<p>2. Get the Authentication Token from Toast (Inside Pre-Request step)</p>
<p>3. Call the API to get the required data from Toast</p>
<p>4. Use Toast API data to build DMB in designer with OptiSync</p>
<hr>
<p><a name="Step1"></a></p>
<h2 id="h_01J43T39XTJCRF7K7BCVR929XK">Step 1: Preparation</h2>
<p>To get started with integrating a Toast API with OptiSigns, we need the following information from the Toast system:</p>
<ul>
<li><em>toast-api-hostname</em></li>
<li>clientId</li>
<li>clientSecret</li>
<li>userAccessType</li>
</ul>
<p>Refer to Toast's Documentation <a href="https://doc.toasttab.com/doc/devguide/portalHowToBuildAToastIntegration.html">here</a> for further details.</p>
<hr>
<p><a name="Step2"></a></p>
<h2 id="01J43T457PRWRQNZ58BKKQXSMY">Step 2: Authentication for Toast API</h2>
<p>For Toast API authentication, we will first need to pass the POST request to get the authentication token. The authentication token is then used to pass in the API request to get the data from Toast menus, orders etc. </p>
<p>This authentication process will be handled using Pre-request processing with OptiSigns' API request. For more information about Pre-request processing and API requests in general, please check <a href="https://support.optisigns.com/hc/en-us/articles/22875592994195" target="_blank" rel="noopener noreferrer">here</a>.</p>
<p>In the Pre-request processing stage, the OptiSigns API calls the authentication API to get the necessary token, and sets it to the context of the API request.</p>
<p>In this example, the token is set to the context variable "authorization". When the API request is made, it will be able to use the authentication token. Below is a screenshot of this example in practice.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/31870675893011"></p>
<p>Use this code snippet (with the data obtained earlier filling in the "xxx"s) to</p>
<pre>const body = {<br>"clientId": "<span style="color: #ce9178;">xxx</span>",<br>"clientSecret": "<span style="color: #ce9178;">xxx</span>",<br>"userAccessType": "<span style="color: #ce9178;">xxx</span>"<br>};<br>const {data, headers} = await os.postRequest("https://<span style="color: #ce9178;">[toast-api-hostname]</span>/authentication/v1/authentication/login", body );<br>const token = os.getValue(data.token.accessToken);<br>os.context.set("authorization", os.getValue(token));</pre>
<hr>
<p><a name="Step3"></a></p>
<h2 id="01J43TQM68FW7XVXN1P63ASCAG">Step 3: Call the API to get the required data from Toast</h2>
<p>Now we'll use the authorization token we received in Pre-request processing and pass it to the actual API call header. </p>
<p>In the Header tab, create two parameters with the following values:</p>
<p class="wysiwyg-indent2"><strong>authorization</strong> Bearer {{authorization}}</p>
<p class="wysiwyg-indent2"><strong>Toast-Restaurant-External-ID</strong> </p>
<p>You can get the <strong>Toast-Restaurant-External-ID value </strong>from Toast Portal. This is the specific restaurant Id you want to get data for.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/31870675894035"></p>
<p>Now put the desired API URL from which you want to get data. In this example we have used the following API to get the menus</p>
<ul>
<li style="list-style-type: none;">
<ul>
<li><a href="https://ws-api.toasttab.com/menus/v2/menus">https://ws-api.toasttab.com/menus/v2/menus</a></li>
</ul>
</li>
</ul>
<p>The final request will look something like this:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/31870675898515"></p>
<p>You can enable this request and save the API. Click <strong>Run Test</strong>.</p>
<p>You should receive a <em>(200 OK)</em> response, with data returning from the API. This means the API request has successfully contacted Toast and is transferring data.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/31870683910291"></p>
<hr>
<p><a name="Step4"></a></p>
<h2 id="01J43V65M8TPKKMPBQ9FWNB8KR">Step 4: Build Digital Menu Board in Designer with OptiSync </h2>
<p>Now that your API request data source is ready for use, you can build your DMB using Designer with OptiSync. OptiSync allows you to map the API data to an element in the designer, either text or images. Using Repeaters, this data can be used to build out multiple item menus, and you're also able to define how you'd like to handle sold-out items, specials, and more.</p>
<p>For a step-by-step guide and more examples, please see our article on <a href="https://support.optisigns.com/hc/en-us/articles/31860170199955-Integrating-Point-of-Sale-POS-Systems-to-Build-Digital-Menu-Boards-with-OptiSync" target="_blank" rel="noopener noreferrer">Building Digital Menu Boards Using OptiSync</a>.</p>
<p> </p>
<h2 id="h_01J5BAG8XP7ZR1BZDXKZ946X53">That's all!</h2>
<p>You have successfully retrieved data from Toast and displayed it on the screens using OptiSigns. </p>
<p> </p>