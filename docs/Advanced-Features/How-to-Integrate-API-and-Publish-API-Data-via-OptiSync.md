<h3 id="h_01J3ZHSCASHHEB5PB9D56J88TV">Integrating your API with OptiSigns has many uses and allows easy display of auto-updating data on your screens. In this guide, we'll walk you through how to connect your API - no software engineering background required.</h3>
<ul>
<li><a href="#Integration">What API Integration Can Do</a></li>
<li><a href="#What">What You'll Need to Get Started</a></li>
<li>
<a href="#Request">How to Set Up an API Request</a><br>
<ul>
<li><a href="#Store">Step 1: Store Your API Authorization Token in the OptiSigns API Keystore</a></li>
<li>
<a href="#Test">Step 2: Set Up and Test the API Request</a>
<ul>
<li><a href="#Parameters">How to Use Parameters</a></li>
<li><a href="#PrePost">How to Use Pre- and Post-Request</a></li>
</ul>
</li>
<li><a href="#Substitution">Step 3 (Optional): Use Substitution Parameters from Device Attributes</a></li>
</ul>
</li>
<li>
<a href="#Map">How to Map API Data in Designer</a>
<ul>
<li><a href="#Create">Step 1: Creating an API DataSource</a></li>
<li><a href="#Maintain">Step 2: Maintain the Element Mapping</a></li>
</ul>
</li>
<li><a href="#Use%20Cases">More on OptiSync Use Cases</a></li>
</ul>
<table style="width: 52.9996%;" border="1">
<tbody>
<tr>
<td style="width: 100%;">
<p id="h_01HYP5KK9Y8NPA313WRC263MMQ"><strong>NOTE:</strong> API Integration is only available with a <strong>Pro Plus </strong>plan or higher.</p>
</td>
</tr>
</tbody>
</table>
<hr>
<p><a name="Integration"></a></p>
<h2 id="h_01J3ZK2JXTCNCJF71XEPJJ3C5X">What API Integration Can Do</h2>
<p>OptiSigns allows easy integration with user APIs. This allows data from a user's API to be shown on any of your digital signs. This allows dynamic updates for:</p>
<ul>
<li>
<strong>Digital Menu Boards</strong> - Integrate with your POS systems and get the DMB updated automatically, and edit the format of your DMB using the designer app whenever needed. </li>
<li>
<strong>Automated HR Update</strong> - Use the API from your HR systems to display birthdays or work anniversaries on the screens automatically.</li>
<li>
<strong>Warehouse Inventory Tracking</strong> - Use your Warehouse's API to display inventory levels with automatic updates throughout your organization</li>
<li>Any other information display use cases that you will need to consume API data and display the data on the screens.</li>
</ul>
<p>This API integration can be achieved in OptiSigns with little to no coding, making it approachable for those without backgrounds in software engineering. In this guide, we will walk you through how to get it set up with the example below using an API from the Clover POS system.</p>
<hr>
<p><a name="What"></a></p>
<h2 id="docs-internal-guid-dff268b8-7fff-8866-a97c-ebf60203dfbc">What You’ll Need to Get Started</h2>
<p>You’ll need your:</p>
<ul>
<li><strong>API Endpoint URL</strong></li>
<li><strong>API Authorization Token</strong></li>
</ul>
<p>These are required for OptiSigns to connect with your desired API. Make sure you have them in an easily accessible place before you try to set up your API Request in the OptiSigns Web Portal. You should be able to obtain these from an IT professional in your organization, or through your POS system administrator.</p>
<hr>
<p><a name="Request"></a></p>
<h2 id="h_01HF3BD565P5F04MNA597DDPGR">How to Set Up an API Request</h2>
<p>The API gateway is a powerful tool that allows users to centrally manage the APIs, as well as configure and test the APIs. </p>
<p id="docs-internal-guid-0067ad93-7fff-d9bf-6592-4daac536d654">Now that you have everything you need, let's get started on setting up an API Request. With an API request, you can:</p>
<ol>
<li>Use the OptiSigns API Keystore to securely store and use API keys from other systems.</li>
<li>Test the API endpoints, with the capability to modify headers and parameters.</li>
<li>Use substitution parameters and pre-processing and post-processing rules to handle complex integration. Pre-processing rules can help you handle those API integration situations that require an additional call to get an authentication token before making the API call. Post-processing will allow you to process the returned data and tailor it to fit your use better. </li>
</ol>
<p>To get started, open your OptiSigns Web Portal.<span id="docs-internal-guid-d6e782f8-7fff-57a7-2ba1-de6444875e31"></span></p>
<p>Once there, navigate to the upper right corner of the screen, and hover over your account name.</p>
<p>Hover over <strong>More <span id="docs-internal-guid-d18c1488-7fff-9df6-01e8-ebdb6aac504f">→ </span></strong><strong><span id="docs-internal-guid-d18c1488-7fff-9df6-01e8-ebdb6aac504f">DataSources</span></strong></p>
<p><strong><span id="docs-internal-guid-d6e782f8-7fff-57a7-2ba1-de6444875e31"><span id="docs-internal-guid-d18c1488-7fff-9df6-01e8-ebdb6aac504f"><img src="https://support.optisigns.com/hc/article_attachments/32427378791315"></span></span></strong></p>
<p>You'll see the screen below.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32427378806803"></p>
<p id="h_01J400P761P7A900DXSV9F0MQB">Now you're ready to get started.</p>
<hr>
<p><a name="Store"></a></p>
<h3 id="h_01HF3BD565741WVSCFRV96BA7K">Step 1: Store Your API Authorization Token in the OptiSigns API Keystore</h3>
<p>The first step is to take your API Authorization Token and store it in the OptiSigns API Keystore.</p>
<p>This step is technically optional: you can input your API Authorization token into an individual API request. However, the Keystore has a few major advantages:</p>
<ul>
<li>Allows your API Authorization token to be sent to multiple API requests, without the need to manually input it each time</li>
<li>Provides superior security for your API Authorization token, making it much harder for outside actors to discover it</li>
</ul>
<p>Therefore, we <strong><em>highly recommend</em></strong> this step.</p>
<p>To enter the Keystore, find the <strong>Lock Icon</strong> and click it.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32427362113683" alt="firefox_YNrLQDITUl.png"></p>
<p>This will open the <strong>API Keystore.</strong></p>
<p><span id="docs-internal-guid-95cd8038-7fff-9e2d-a4ad-27f801d36175"><img src="https://support.optisigns.com/hc/article_attachments/32427378817171" width="470" height="241"></span></p>
<p id="h_01J4043NS8A4BWRYMETEP01EWC">Click <strong>Add Key</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32427378823187" alt="firefox_Af1bBuAYxy.png"></p>
<p>There are two fields here.</p>
<ul>
<li>
<strong>First Field - </strong>Enter the name of the key here. We recommend something that will help you remember it. You'll be using this to set up an API request.</li>
<li>
<strong>Second Field - </strong>The actual unique passcode for your API communications.</li>
</ul>
<p>Once you've input your API Authorization token, hit <strong>Save</strong>. When you want to run a request using this API Key, you'll use the term: <strong>{{apiKeystore.&lt;&lt;key&gt;&gt;}}</strong> where "&lt;&lt;key&gt;&gt;" is replaced by the name you inserted earlier. In this example, we'll name our request "clover".</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32427378828051"></p>
<p>Now, we're ready to set up your API request.</p>
<hr>
<p><a name="Test"></a></p>
<h3 id="01HF649SAMCTE9X7YTD5MN92RC">Step 2: Set Up and Test the API Request</h3>
<p>Before moving forward in OptiSigns, we recommend <a href="https://www.postman.com/api-platform/api-testing/"><strong>testing your API</strong></a> connection using a free tool, such as <a href="https://www.postman.com/"><strong>Postman</strong></a>. This provides several advantages, including:</p>
<ul>
<li>Checking your data formatting</li>
<li>Ensuring the correct data is being provided</li>
<li>Verifying your authentication</li>
<li>Identifying integration problems or connection errors</li>
</ul>
<p>The test parameters, endpoints, and authenticators can then be used in OptiSigns to set up your API request. Here's how to do that.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32427362124563" alt="firefox_orSTybxxGU.png"></p>
<p> </p>
<p>Click the <strong>Add Request</strong> button, it will launch the window for you to configure and test the API request.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32427362128147" alt="firefox_owER9ex9xQ.png"></p>
<ul>
<li>
<strong>Display Name - </strong>This will be shown under the API gateway list, mainly to help users identify the API request.</li>
<li>
<strong>Name -</strong> This is used as a reference to the API request, it is a technical name that will be used later in the path to refer to the API request data. </li>
<li>
<strong>URL -</strong> This is the API endpoint, you can use the GET or POST method depending on the API request, for example, if you are using GraphQL, then all requests will be using POST.</li>
<li>
<strong>Params - </strong>Allows you to define the parameters in your API request. You may see parameters in your API endpoint URL, these will be preceded by a "?" mark. These can be used in pre and post processing request code to further automate your API request.</li>
<li>
<strong>Headers - </strong>The header(s) of the API request. You will want to input your API Authentication token here.</li>
<li>
<strong>Pre-request - </strong>An optional piece of code which prepares the context before the API request. For example, you may need to call another API to get a short-lived authentication token before calling the API, or you need to calculate some variables to be used in the API request.</li>
<li>
<strong>Post-request - </strong>An optional piece of code which modifies the data received from the request. For example, if the data you receive is not exactly how you want it displayed, you can write a bit of code to modify it according to your digital display needs.</li>
<li>
<strong>Enable Webhook -</strong> Generates a webhook link and an associated token. This webhook can be used to notify us of a change in the data, which will refresh the API request and update your screens automatically.</li>
<li>
<strong>Enable this Request</strong> - Set the status of the API request.</li>
</ul>
<p>To test the request, we'll need to configure the header. This is where the Keystore comes in. In the second box, type <strong>Bearer {{apiKeystore.&lt;&lt;key&gt;&gt;}}</strong>, where <em>Bearer</em> is the type of token and <em>{{apiKeystore.&lt;&lt;key&gt;&gt;}}</em> pulls the token stored in the Keystore. In this example, we'll use the name "clover" as referenced above.</p>
<p>Once that's done, click <strong>"Run Test"</strong>. If the<span id="docs-internal-guid-07049797-7fff-b800-0f01-5a1868a79727"> response code is 200, the API has returned data successfully. If there is any other code, there is an issue in the API Request.</span></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/22917836593171"></p>
<p><a name="Parameters"></a></p>
<h4 id="h_01J457N0FSXX9H0KS2BW3AS2NA">How to Use Parameters</h4>
<p>Parameters are present in URLs of all types. There are two elements to a parameter:</p>
<ul>
<li>They have to follow a '?' mark in the URL;</li>
<li>They have a value associated with them</li>
</ul>
<p>The <strong>Params</strong> tab lets you specify the Parameters whose value you would like to change.</p>
<p>Usually, the <strong>Params</strong> tab is used in conjunction with the Pre-request and Post-request tabs to create automatically updating values.</p>
<p><a name="PrePost"></a></p>
<h4 id="h_01J457NW1FC6GHPSKZ1HX4AC76">How to Use Pre- and Post-Request Processing</h4>
<p>To use pre- and post-request processing, some amount of Javascript knowledge is needed.</p>
<table style="width: 100%;" border="1">
<tbody>
<tr>
<td>What is the Difference Between the Two?</td>
</tr>
<tr>
<td>
<strong>Pre-request:  </strong>This is a code snippet normally set the context <em><strong>before</strong></em> the API request. This can be retrieving an authentication token from another API, or to change parameters to allow for more automation.</td>
</tr>
<tr>
<td>
<strong>Post-request: </strong>A piece of code to apply to the data <em><strong>received from</strong></em> the API request. This code can be used to modify the received data to change how it is displayed on your screens.</td>
</tr>
</tbody>
</table>
<p> </p>
<p>The <strong>Pre-request</strong> tab is where you'll input code for pre-request processing.</p>
<p><strong>Example: </strong>For the systems that requires a dynamically generated authentication token like Toast, this can be used to call another API to retrieve the authentication token and set it to the context of the API.</p>
<p>For more on this example, see this article on <a href="https://support.optisigns.com/hc/en-us/articles/31113088917907-How-to-use-Toast-API-data-with-OptiSigns">how to connect your Toast API</a>.</p>
<p> </p>
<p>The <strong>Post-request </strong>tab is where you'll input code for post-request processing.</p>
<p><strong>Example: </strong>You are receiving data from your point-of-sale (POS) software API, but certain pieces of data aren't displaying the way you'd like.</p>
<p>Prices may display as whole numbers (i.e. 1299) instead of as a proper pricing (i.e. $12.99). For this, we'd need a piece of code to convert the whole number into a price, and have that code be extensible to any similar display errors (e.g. 1899 instead of $18.99).</p>
<p><span id="docs-internal-guid-22ff4310-7fff-0bbb-7ec5-d4f3b5b0f0fc"><img src="https://support.optisigns.com/hc/article_attachments/32427362130195" width="451" height="481"></span></p>
<p> </p>
<p>For this common example, this piece of JavaScript code should solve your issue. We can also set up the ability to map product availability at the same time.</p>
<p>This will fix the returned data, allowing it to display properly:</p>
<p><span id="docs-internal-guid-fe2e42f8-7fff-a321-5d2c-e37c897928f2"><img src="https://support.optisigns.com/hc/article_attachments/32427362133523" width="624" height="615"></span></p>
<p>This can also be used to make data appear as "SOLD OUT," to strike through an item if it's unavailable, or to display warnings in an inventory management system. For more on this example, see our article on <a href="https://support.optisigns.com/hc/en-us/articles/31860170199955-Integrating-Point-of-Sale-POS-Systems-to-Build-Digital-Menu-Boards-with-OptiSync" target="_blank" rel="noopener noreferrer">Digital Menu Boards.</a></p>
<hr>
<p><a name="Substitution"></a></p>
<h3 id="01HF65Q85XJHBVKS0TE422NHB9">Step 3 (Optional): Use Substitution Parameters from Device Attributes.</h3>
<p id="h_01HF3BD56518CMJ91M7S15DNHK">Many point-of-sale (POS) systems are licensed by store/location. It's possible to configure a single API Request with OptiSync and have it work with different locations using <strong>substitution parameters</strong>. Inputting these allows your screen to communicate its store or location identification information. This means a single API request can communicate different data to different stores or locations, rather than needing to make individual API requests per screen.</p>
<p>To get started, find the screen you wish to edit.</p>
<p><span id="docs-internal-guid-c02db463-7fff-a591-fd82-0c5602b1eaa0"><img src="https://support.optisigns.com/hc/article_attachments/32427362139411" width="624" height="32"></span></p>
<p><span id="docs-internal-guid-d18c1488-7fff-9df6-01e8-ebdb6aac504f">Click <strong>Advanced</strong> <strong>→</strong> <strong>More</strong> <strong>→</strong> <strong>Device Additional Attributes.</strong></span></p>
<p><span id="docs-internal-guid-bd724934-7fff-6026-36a9-6d967d990667"><img src="https://support.optisigns.com/hc/article_attachments/32427378848019" width="624" height="681"></span></p>
<p>Two fields will show up, <strong>Key</strong> and <strong>Value</strong>.<br><img src="https://support.optisigns.com/hc/article_attachments/32427362146707" alt="firefox_KkCBvxsPKU.png"></p>
<ul>
<li>
<strong>Key</strong> - A parameter that will be used during the API call to substitute for your store's value. This will replace part of your API URL endpoint.</li>
<li>
<strong>Value </strong>- Represents the unique code associated with the store or location you wish to pass through to your API.</li>
</ul>
<p>In this example, we are maintaining the Clover merchantID here. The value inputted will need to be obtained on your end as it will be unique.</p>
<p>Now, go back to the API request config page. Substitute the merchantID in the API endpoint with the Key name you previously defined.</p>
<h4 id="h_01J4253EJPPRGWMTR1GE8S2QMJ"><strong><img src="https://support.optisigns.com/hc/article_attachments/22917801932051"></strong></h4>
<p>When the API call is triggered on the device, it will take the value from the device and substitute it at runtime. For each screen, you'll want to perform these same steps, keeping the Key name the same while changing the Value. This will allow you to push different data to different screens.</p>
<hr>
<p><a name="Map"></a></p>
<h2 id="01HF66CVDRC8Z6HP67NCV3NFB6">How to Map API Data in Designer</h2>
<p>In order to push data from your API to a screen, it will need to be registered as a DataSource. This allows data elements to be added to OptiSigns' Designer app, where it can be formatted and incorporated into any visual design you'd like to display.</p>
<p>The Designer app and templates can be used to do the formatting, and the API data source will handle the data mapping. Any text box or image element can be mapped in Designer. When you map an image element, the URL of the image will be replaced at run time.</p>
<hr>
<p><a name="Create"></a></p>
<h3 id="h_01J42FP3F4Y02SGZ3V3MGKV3ZZ">Step 1: Creating an API DataSource</h3>
<p>To get started, find your design or create a new one in the <strong>Files/Assets </strong>tab.</p>
<p>With the design open, click <strong>"DataSource" </strong>in the left hand column. Then, click <strong>"Add DataSource" </strong>to add an API data source to the design.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42850937896211"></p>
<p>Scroll down to where it says <strong>"API Gateway"</strong> and click it.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42850937907987"></p>
<p>You should see this screen:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42850937909523"></p>
<p>Select the API Request created above. You'll see a screen like the one below:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42850937911187"></p>
<p>Here, you can choose what data specifically you want to add to the Design. If you want all the options, hit <strong>"Continue"</strong>. This screen will appear.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42850937917715"></p>
<p><strong>DataSource Name</strong> is how this DataSource will appear in Designer. Name it whatever helps you identify it.</p>
<p><strong>Synchronization </strong>lets you choose how often to sync back to your API. <em>Only import once</em> makes sense for one-time promos and the like. If this is for a longer-term asset, choose <em>Periodic direct access </em>or <em>Periodic background sync </em>depending if you need to use the data from specific device to set the context<em>.</em></p>
<p>Hit <strong>Done</strong>, and the DataSource is created.</p>
<p>It should appear in the left column under <strong>"Used in this design". </strong>It will definitely appear in the <strong>"Other DataSources" </strong>section. You may need to refresh the page for it to appear.</p>
<p>Now, we move to step 2.</p>
<hr>
<p><a name="Maintain"></a></p>
<h3 id="01HF678TZ846EDXFB4DEW06H4B">Step 2: Maintain the Element Mapping</h3>
<p>Once the API DataSource has been created, you're ready to map the data.</p>
<p>In Designer, open your DataSource.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42850953614611"></p>
<p>Click on it and a screen similar to this will pop up:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42850953615763"></p>
<p>Opening up any of these will display the data pulled from your API:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42850953617427"></p>
<p>By clicking on any piece of this data and dragging it onto the screen, the data will appear. You'll have the option to use the data as a Repeater or on its own. </p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42850937928467"></p>
<p>In this case, we want to use it on its own. For menus, a Repeater makes the most sense.</p>
<p>In order to check the data binding, you can click on any mapped element, then click <strong>Settings</strong>. You will see the <strong>Asset Element Name </strong>there.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42850937932307"></p>
<p>We have the item name and price from the API mapped to the design. When published on the screen, the value will be automatically replaced with the value from the API. If updates are made in the Clover POS system, the change will be reflected on the screen automatically. </p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42850937936019"></p>
<p>Repeat this step for all the elements that you want to map to the API data source, and save the design. Your design is ready to go.</p>
<hr>
<p><a name="Use%20Cases"></a></p>
<h2 id="h_01J42GW2TPXQBKAT3RS8DNQH86">More OptiSync Use Cases</h2>
<p>If you'd like more detail on API integration use cases, we have several additional articles. Please see:</p>
<ul>
<li><a href="https://support.optisigns.com/hc/en-us/articles/31860170199955-Integrating-Point-of-Sale-POS-Systems-to-Build-Digital-Menu-Boards-with-OptiSync" target="_blank" rel="noopener noreferrer">Point-of-Sale Systems to build Digital Menu Boards</a></li>
<li><a href="https://support.optisigns.com/hc/en-us/articles/33468569218067-How-to-Display-Dynamic-Event-Schedules-Using-OptiSync" target="_blank" rel="noopener noreferrer">Displaying Event Schedules</a></li>
<li><a href="https://support.optisigns.com/hc/en-us/articles/31113088917907-How-to-use-Toast-API-data-with-OptiSigns" target="_blank" rel="noopener noreferrer">Integrating Toast API Systems</a></li>
<li>Custom RSS Feeds</li>
<li><a href="https://support.optisigns.com/hc/en-us/articles/4404511767571-How-to-use-Dynamic-Data-Mapping-feature-with-Google-Sheets" target="_blank" rel="noopener noreferrer">Dynamic Data-Mapping</a></li>
</ul>
<hr>
<h2 id="h_01J42FH3Q6C6J4BH4TS4HR5M4Y">That's all!</h2>
<p>This is how you integrate API data and get it published on your screen. Most importantly, with no coding!</p>
<p>If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self">support@optisigns.com</a></p>