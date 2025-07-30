<h3 id="h_01J42NQ13RWXKTMQEBC7M1AAKP">OptiSync allows you to create dynamic digital menus through API integration. Your POS systems can interface directly with OptiSigns to automatically update prices, track inventory, and more.</h3>
<ul>
<li>
<a href="#Section%201">How to Integrate POS Systems Through API Requests</a><br>
<ul>
<li><a href="#Section%202">Get API URL Endpoint and Set Up API Request DataSource</a></li>
<li><a href="#Section%203">Additional Information on API Authentication</a></li>
<li><a href="#Section%204">Handling Multiple Stores or POS Locations</a></li>
<li><a href="#Section%205">How to Use Post-Request Processing to Convert API Data</a></li>
</ul>
</li>
<li>
<a href="#Section%206">How to Build Digital Menu Boards in Designer with OptiSync</a><br>
<ul>
<li><a href="#Section%207">Using DataSources and Repeaters</a></li>
<li>
<a href="#Section%208">Element Mapping</a><br>
<ul>
<li><a href="#Section%209">Adding Text Elements to Your Menu</a></li>
<li><a href="#Section%2010">Creating Strike Throughs and Sold Out Warnings</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#Section11">Pushing a Digital Menu Board to a Screen</a></li>
</ul>
<p>In this article, we will create a real Digital Menu Board (DMB) integrated with a Clover POS system. The DMB pulls product info from Clover and display it onscreen. When an item is not available, it will display as "SOLD OUT."</p>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td class="wysiwyg-text-align-center" style="width: 100%;"><strong>NOTE</strong></td>
</tr>
<tr>
<td style="width: 100%;">
<h4 id="h_01HYP5KK9Y8NPA313WRC263MMQ">API Integration is only available with a <strong>Pro Plus </strong>plan or higher.</h4>
</td>
</tr>
</tbody>
</table>
<hr>
<p><a name="Section%201"></a></p>
<h2 id="h_01J42PGTCG733REFMF4EYGDP1Z">How to Integrate POS Systems Through API Requests</h2>
<p>Most POS systems have an API library which OptiSigns can use to get the relevant data from the system programmatically. This API can return menu items, item price, availability, and more.</p>
<p>With OptiSync, we can link APIs to the OptiSigns portal and push the data to screens as a Digital Menu Board (DMB) or any other type of screen you'd like without the need of human intervention.</p>
<p><span id="docs-internal-guid-11755c21-7fff-77b9-e7ec-e7ae6d8efac2"><img src="https://support.optisigns.com/hc/article_attachments/31860108901523" alt="api optisigns integration diagram" width="624" height="192"></span><span class="wysiwyg-font-size-large"></span></p>
<p>This article will focus on these POS specific wrinkles, and the process of mapping POS data to assets and pushing them to screens.</p>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td class="wysiwyg-text-align-center" style="width: 100%;"><strong>IMPORTANT</strong></td>
</tr>
<tr>
<td style="width: 100%;">In order to integrate a POS system, you'll need to first set up an API Gateway request. A complete guide for how to do that can be found <a href="https://support.optisigns.com/hc/en-us/articles/22875592994195-How-to-Integrate-API-and-Publish-API-Data-via-OptiSync">here</a>.</td>
</tr>
</tbody>
</table>
<hr>
<p><a name="Section%202"></a></p>
<h3 id="h_01J4ADGSYSMKXCMA4JA2218H8Z">Get API Endpoint URL and Set Up API Request DataSource</h3>
<p>We have a <a href="https://support.optisigns.com/hc/en-us/articles/22875592994195-How-to-Integrate-API-and-Publish-API-Data-via-OptiSync" target="_blank" rel="noopener noreferrer">comprehensive guide</a> on how to set up your API gateway request. We recommend following this guide until your initial request is set up.</p>
<p>Bare minimum, you'll need an API endpoint URL and an API Authentication token.</p>
<p><a name="Section%203"></a></p>
<h3 id="h_01J4ADQGQFWYVZ7FXXASZCZJS2">Additional Information on API Authentication</h3>
<p>For most token based authentication, setting up the authentication token with the key store is normally all that's required for an API request. But certain APIs (such as Toast) will require additional calls to get the authentication token for each request, this can be handled through pre-request processing. To see how to handle that, see our <a href="https://support.optisigns.com/hc/en-us/articles/31113088917907-How-to-use-Toast-API-data-with-OptiSigns" target="_blank" rel="noopener noreferrer">article on Toast APIs</a>.</p>
<p><a name="Section%204"></a></p>
<h3 id="h_01J42SJXHV5A3HAQRNQGKDHDTS">Handling Multiple Stores or POS Locations</h3>
<p>Once you've got your basic API Gateway request set up, there are a few additional steps you'll want to perform if you have multiple locations for your screens. These different locations may have different menus, or different specials for that day, or even different pricing depending on various factors.</p>
<p>POS systems normally require separate license for each location. Your POS system API may provide different store ID in the API endpoint or using different authentication token. For larger deployment with multiple stores, you can use substitution parameters to handle that with OptiSigns. </p>
<p>There are two ways to handle multiple POS locations:</p>
<ol>
<li>Set up individual API requests for each of your POS locations, changing the value in the URL endpoint each time and mapping them to each of your screens individually. If you only have a few locations where your POS system is used, this will work just fine.</li>
<li>
<em>(Recommended) </em>Configuring each screen to send its storeID to the API call, allowing a single API request to provide data to multiple screens. For anything more than two or three screens, we recommend this method.</li>
</ol>
<p>Here's how to handle option 2.</p>
<p>To get started, find the screen you wish to edit.</p>
<p><span id="docs-internal-guid-c02db463-7fff-a591-fd82-0c5602b1eaa0"><img src="https://support.optisigns.com/hc/article_attachments/31893086724755" alt="edit screen" width="624" height="32"></span></p>
<p><span id="docs-internal-guid-d18c1488-7fff-9df6-01e8-ebdb6aac504f">Click <strong>Advanced</strong> <strong>→</strong> <strong>More</strong> <strong>→</strong> <strong>Device Additional Attributes.</strong></span></p>
<p><span id="docs-internal-guid-bd724934-7fff-6026-36a9-6d967d990667"><img src="https://support.optisigns.com/hc/article_attachments/31893080684563" alt="device additional attributes on edit screen" width="624" height="681"></span></p>
<p>Two fields will show up, <strong>Key</strong> and <strong>Value</strong>.<br><img src="https://support.optisigns.com/hc/article_attachments/32043124363155" alt="device additional attributes key value"></p>
<ul>
<li>
<strong>Key</strong> - A parameter that will be used during the API call to substitute for your store's value. This will replace part of your API URL endpoint.</li>
<li>
<strong>Value </strong>- Represents the unique code associated with the store or location you wish to pass through to your API.</li>
</ul>
<p>In this example, we'll pretend the parameter you are changing is called "merchantID". The value inputted will need to be obtained on your end as it will be unique.</p>
<p>Now, go back to the API request config page. Substitute the merchantID in the API endpoint with the Key name you previously defined.</p>
<h4 id="h_01J4253EJPPRGWMTR1GE8S2QMJ"><strong><img src="https://support.optisigns.com/hc/article_attachments/31893086738707" alt="clover url request"></strong></h4>
<p>When the API request is triggered on the device, it will take the value from the device and substitute it at runtime. For each screen, you'll want to perform these same steps, keeping the Key name the same while changing the Value. This will allow you to push different data to different screens off a single API Request.</p>
<p><a name="Section%205"></a></p>
<h3 id="h_01J452PTNGXSTP64QBFPSP5FCM">How to Use Post-Request Processing to Convert API Data</h3>
<p>When retrieving data from your POS system, it may not initially show up exactly the way you'd like, or you might want to add some functionality, such as the ability to display SOLD OUT for items out of stock.</p>
<p>For example, prices may display as whole numbers (i.e. 1299 instead of $12.99). That's where the "Post-request" tab comes in - this allows changes to be made to the data after it comes in. This will require some basic coding to use.</p>
<p>Take the example of the price display from earlier. How would we convert a number like 1299 to display as $12.99, and make that piece of code extensible to any similar display errors (e.g. 1899 instead of $18.99)?</p>
<p><span id="docs-internal-guid-22ff4310-7fff-0bbb-7ec5-d4f3b5b0f0fc"><img src="https://support.optisigns.com/hc/article_attachments/31893086743187" width="451" height="481"></span></p>
<p><span>For this common example, this piece of JavaScript code should solve your issue.</span></p>
<pre><span>let {data, headers, status} = os.context.get("response");<br>temp_data = data.elements<br>for (let object of temp_data) {<br>        object.price = '$' + (object.price*.01);<br>        if (object.available == true)<br>              {object.soldout=0;}<br>            else {object.soldout=1;}<br>    }<br>return temp_data</span></pre>
<p>This will fix the returned data, allowing it to display properly. It will also allow for creation of SOLD OUT and strike through for when items are out of stock.</p>
<p><span><span id="docs-internal-guid-fe2e42f8-7fff-a321-5d2c-e37c897928f2"><img src="https://support.optisigns.com/hc/article_attachments/32060273039763"></span></span></p>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<td style="width: 100%;">
<strong>NOTE: </strong>Enabling and configuring a WebHook allows near real-time updating of the data pulled from your API. If you plan to keep track of store inventory using your digital signs, we recommend setting one up. You will need to input the provided WebHook key into your API to set this up.</td>
</tr>
</tbody>
</table>
<p><span><span> </span></span></p>
<hr>
<p><a name="Section%206"></a></p>
<h2 id="h_01J47S7KNZFD9YVW2WZ7RN6JF8">How to Build Digital Menu Boards in Designer with OptiSync</h2>
<p>In order to create a DMB with data from your POS system, the API Request will need to be registered as a DataSource. This allows data elements to be added to <a href="https://support.optisigns.com/hc/en-us/articles/4404151402899-How-to-use-OptiSigns-Template-Designer-app-to-make-your-Digital-Signs-in-minutes" target="_blank" rel="noopener noreferrer">OptiSigns' Designer app</a>, where it can be formatted and incorporated into any visual design you'd like to display.</p>
<p>The Designer app and templates can be used to do the formatting, and mapping the element to the data from the API data source. Any text box or image element can be mapped in Designer. When you map an image element, the URL of the image will be replaced at run time.</p>
<hr>
<p><a name="Section%207"></a></p>
<h3 id="h_01J42FP3F4Y02SGZ3V3MGKV3ZZ">Using DataSources and Repeaters</h3>
<p>To get started, find your design or create a new one in the <strong>Files/Assets </strong>tab.</p>
<p>With the design open, click <strong>"DataSource" </strong>in the left hand column. Then, click <strong>"Add DataSource" </strong>to add an API data source to the design.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/43051537966355" alt="firefox_ebkICMVoVf.jpg"></p>
<p>Scroll down to where it says <strong>"API Gateway Collection"</strong> and click it.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/31936613189523" alt="firefox_mCdtjleFse - Copy.png"></p>
<p>You can also set up a one-time Gateway with the <em>API Gateway</em> command if you need a one-off design with no pre- or post-request processing. In our example, however, we are, so we'll use Gateway Collection.</p>
<p>You should see this screen:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/31936613193747" alt="firefox_xXJk2r7wuv - Copy.png"></p>
<ul>
<li>
<strong>Name - </strong>The name of the DataSource. This is internally facing and will not be shown on your screens.</li>
<li>
<strong>Select APIs - </strong>Here you'll select from the API Gateways you've already set up in earlier steps. You can select just one, or multiple. If multiple are selected, the API DataSource will automatically aggregate them.</li>
<li>
<strong>Update Interval - </strong>How often to send requests back to the API for updates. Select from None (never call the API back), 30 minutes, 60 minutes, or every 6 hours. If you Enable WebHook on your API Request and input the provided URL in your API, this Update Interval will change to near real-time.</li>
</ul>
<p>Hit <strong>Save</strong>, and the DataSource is created.</p>
<p>It should appear in the left column under <strong>"Used in this design". </strong>It will definitely appear in the <strong>"Other DataSources" </strong>section. You may need to refresh the page for it to appear.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/31937799814163"></p>
<p><a name="Section%208"></a></p>
<h3 id="h_01J47YAEH51B1AEQRD9YMH85J7">Element Mapping</h3>
<p>Now that you've got your API DataSource has been created, we're ready to map the data. In this example, we will show you how to make a DMB with the ability to strike through product names and display the phrase "SOLD OUT" when the item is out of stock.</p>
<p><a name="Section%209"></a></p>
<h4 id="h_01J4A095APB88KJRX3M1KR038D">Adding Text Elements to a Digital Menu Board</h4>
<p>First, create your design. You can create your menu within our Designer app.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/43051537968787" alt="firefox_g87oDmb7i3.jpg"></p>
<p>The easiest way to set up a DMB is with a <strong>Data Repeater</strong>. For a full breakdown of a Repeater's capabilities, <a href="https://support.optisigns.com/hc/en-us/articles/29217646663187">see this article</a>. Here, we'll stick to teaching how to add information from your POS system.</p>
<p>To set up a Repeater, click <strong>"Repeaters" <span id="docs-internal-guid-d18c1488-7fff-9df6-01e8-ebdb6aac504f">→</span> Add Blank Repeater</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/43051537970195"></p>
<p>With the Repeater selected, click <strong>Settings</strong>. Then select <strong>Connect to DataSource </strong>on the Side Menu.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/43051537971219" alt="firefox_yX20kMKstf.jpg"></p>
<p>Select the DataSource you set up in the last set under <strong>"Other DataSources"</strong>.</p>
<p>You'll be taken back to the last pane with your DataSource now selected. Now, click <strong>Edit</strong> or double click the selected Repeater to head to the Repeater Editor. This is like a design-within-a-design, specifically for your Repeater (menu) items. With text selected, click the arrow on the left.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32078326973331"></p>
<p>That brings up the DataSource tab. Click on the DataSource Used in this Design and you'll see something like this:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/31968058948371" width="202" height="161"></p>
<p>In this example, we want to display the name and the price, with the possibility of saying "SOLD OUT"</p>
<p>By creating text and dragging data points to it, we can create a menu item like this:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32060268861331"></p>
<p>This was created by finding data points from the API and dragging them into the desired text boxes. In this case, we only wish to display the "name" and "price," so those values were what we dragged into a blank or existing text box.</p>
<p>If your numbers need extra formatting, click on the number, then hit <strong>Settings.</strong><span id="docs-internal-guid-d18c1488-7fff-9df6-01e8-ebdb6aac504f"> </span><span></span></p>
<p><strong><span><img src="https://support.optisigns.com/hc/article_attachments/32077278901139"></span></strong></p>
<p><span id="docs-internal-guid-d18c1488-7fff-9df6-01e8-ebdb6aac504f">Click <strong>Advanced Options →</strong> <strong>"Display Format" </strong>and choose <strong>"Number," </strong>then click <strong>"Number Format" </strong>and select the formatting you'd like. This will allow you to add dollar signs to your prices, with other options.</span></p>
<p><span><img src="https://support.optisigns.com/hc/article_attachments/32060268867859" alt="ShareX_q0ybaobi0E.png" width="180" height="426"></span></p>
<p><span>Make sure to hit <strong>Update</strong> to make your new number format display.</span></p>
<p><span><img src="https://support.optisigns.com/hc/article_attachments/32060273056019" alt="mraS5gfp1n.png" width="267" height="355"></span></p>
<p><span>The value of a repeater is that it will copy the format of this one cell, then replace the data points with others from your API. Done correctly, y</span><span>our menu should look something like this:</span></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32077278906643"></p>
<p>The Repeater will pull as many data points as you have set up on your API. In this example, we've made a menu with 9 items, but with proper design you can put as many items as you'd like, with dynamic descriptions as well. If you have more items than what you've set to show on your screen at any one time, the items on the menu will rotate through them until they have all displayed.</p>
<p><a name="Section%2010"></a></p>
<h4 id="h_01J4A06311R1Z8V4ME8XZPQ3HF">Creating Strike Throughs and Sold Out Warnings</h4>
<p>In the above example, we show a Sold Out warning. However, we don't want to display that all the time - only when the item isn't available. With OptiSync, this can be accomplished thanks to the Post-request processing we did earlier. Our code created this <strong>"soldout: 0"</strong> data. This is tied to our <strong>"available"</strong> data:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32077278913043" width="244" height="394"></p>
<p>When the "available" data reads "true," the "soldout" data reads 0. When your POS system detects items are unavailable, the "available" data will read "false". This will make the "soldout" data read 1.</p>
<p>We can use this knowledge to set up our Sold Out warnings and strike throughs to only appear when items are not available.</p>
<p>Going back to our Repeater Editor, we can click on a piece of text we want to strike through and hit <strong>Settings</strong>:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32077293399315" width="344" height="254"></p>
<p>In the Settings tab, hit <strong>Advanced Options</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32077801189779" width="177" height="289"></p>
<p>Under Advanced Options, hit <strong>Property Mapping</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/31968071408915" width="251" height="399"></p>
<p>Two values will show up: <strong>Property</strong> and <strong>Value</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/31968059040275" width="137" height="92"></p>
<p>Under Property, choose <strong>Linethrough</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/31968450832915" width="158" height="288"></p>
<p>Under Value, choose <strong>.soldout. </strong>Before the "." will be the name of your API Request.</p>
<p><strong><img src="https://support.optisigns.com/hc/article_attachments/32077293403411" width="114" height="345"></strong></p>
<p>This sets the text to be crossed out when the "soldout" data reads 1.</p>
<p>We can repeat this with the Sold Out reading, except instead of Linethrough, choose <strong>Visible</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/31968463038227" width="84" height="252"></p>
<p>This will make the Sold Out text only appear when the "visible" data reads 1 - in other words, when your product is sold out.</p>
<p>Your final menu ought to look something like this:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/32077820105875"></p>
<p>Finally, you're ready to Name and <strong>Save</strong> your Design.</p>
<p><a name="Section11"></a></p>
<h2 id="h_01J4A9ESD2PYYXGRRDCSV8HCG2">Pushing Digital Menu Boards to Screens</h2>
<p>Getting your new DMB onto a screen is relatively simple. Go back to the screens you set up with substitution parameters earlier. Then, hit <strong>Edit Screen.</strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/31969909937299" width="456" height="313"></p>
<p>Under <strong>Type</strong>, choose asset, then select your DMB asset to play.</p>
<h2 id="h_01J4AA1ZVJXQMW7BWVK8TQDXYJ">That's all!</h2>
<p>You should be able to create an Digital Menu Board with dynamic data features.</p>
<p>If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_self">support@optisigns.com</a>.</p>