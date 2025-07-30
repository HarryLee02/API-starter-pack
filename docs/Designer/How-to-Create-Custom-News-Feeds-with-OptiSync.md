<h3 id="h_01JCGEGWN33ENDPRSSMP740PB6"><span style="color: #434343;">In this article, we will cover OptiSigns’ ability to create custom news apps using the OptiSync feature.</span></h3>
<ul>
<li><a href="#Examples">SharePoint News Examples</a></li>
<li>
<a href="#Setup">How to Set Up a Custom News Feed</a>
<ul>
<li>
<a href="#Gateway">Step 1: Setting Up an API Gateway (SharePoint Example)</a>
<ul>
<li><a href="#Endpoint">Choosing the Correct URL Endpoint for Connection</a></li>
<li><a href="#Authentication">SharePoint API Authentication using OAuth 2.0 in Microsoft Azure</a></li>
</ul>
</li>
<li><a href="#DataSource">Step 2: Mapping the API to a DataSource</a></li>
<li>
<a href="#Designer">Step 3: Creating a News Feed Using Designer</a>
<ul>
<li><a href="#Element">Element Mapping</a></li>
</ul>
</li>
<li><a href="#Filters">Applying Filters to Customize Which News Stories to Display</a></li>
</ul>
</li>
</ul>
<p>It is common for companies to share their internal communications, including memos, news, announcements and more via intranet. Digital signage will heighten employee awareness of published company news and announcements.</p>
<p>Using OptiSync, it’s possible to create a custom news app to display company news stored on your company’s intranet. This is achieved by connecting an intranet API with OptiSync and choosing what data to display in the <a href="https://support.optisigns.com/hc/en-us/articles/4404151402899-How-to-use-OptiSigns-Template-Designer-app-to-make-your-Digital-Signs-in-minutes"><span class="wysiwyg-underline" style="color: #1155cc;">OptiSigns Designer app</span></a>.</p>
<p>Creating news feeds with OptiSync has a key advantage: you have full control of the look and feel of your feed. You can create feeds that match your company branding and design guidelines no matter which news source you use. We will be using SharePoint here as an example, but you can use anything that can be input as a Datasource.</p>
<p>Before we get started, it will be helpful to familiarize yourself with a few other concepts which will be important to understand that we cover in other articles:</p>
<ul>
<li><a href="https://support.optisigns.com/hc/en-us/articles/22875592994195-How-to-Integrate-API-and-Publish-API-Data-via-OptiSync"><span class="wysiwyg-underline" style="color: #1155cc;">How to Integrate API and Publish API Data via OptiSync</span></a></li>
<li><a href="https://support.optisigns.com/hc/en-us/articles/29217646663187-How-to-Set-Up-Dynamic-Data-Mapping-with-OptiSync"><span class="wysiwyg-underline" style="color: #1155cc;">How to Set Up Dynamic Data Mapping via OptiSync</span></a></li>
</ul>
<p>The API article in particular will provide detailed instructions for how to pair an API and get its data on screen with automatic updates. Once you’ve got your API set up and its data saved as a data source, you can create some of the examples below using the Designer app.</p>
<p>The main example tackled in this article will be company news, but this feature can be used for far more, including:</p>
<ul>
<li>Custom RSS feeds</li>
<li>Custom XML/JSON feeds</li>
<li>Inventory management systems</li>
<li>Point-of-sales updates across multiple locations</li>
<li>Additional internal communications</li>
<li>Other news sites</li>
</ul>
<hr>
<p><a name="Examples"></a></p>
<h2 id="h_01JCGEGWN3TFHZMYFSAWGNTH3H">SharePoint News Examples</h2>
<p>Below are some examples using SharePoint. There are numerous possibilities of how to design and create engaging news feeds using SharePoint news or other intranet applications.</p>
<p>Here are a few examples:</p>
<p><a name="Bulletin"></a></p>
<h4 id="h_01JCGEGWN3WCGB53X4YGHENR86"><span style="color: #666666;">Bulletin Feed</span></h4>
<p><img src="https://support.optisigns.com/hc/article_attachments/35337756491283" alt="bulletin news feed example" width="624" height="349"></p>
<p>This style allows several news stories to be shown at once. The images and text are taken directly from the data source and displayed using OptiSync. These are set to periodically update every 30 minutes.</p>
<p><a name="Single"></a></p>
<h4 id="h_01JCGEGWN3Q52GYB8BNFZSD446"><span style="color: #666666;">Single Story Feed</span></h4>
<p><img src="https://support.optisigns.com/hc/article_attachments/35337746485139" alt="single story news feed example" width="624" height="349"></p>
<p>This style allows a single story to be featured. Using Repeater settings, this will allow a rotating slate of featured news articles.</p>
<hr>
<p><a name="Setup"></a></p>
<h2 id="h_01JCGEGWN3931VNHV3NMRJM0GR">How to Set Up a Custom News Feed</h2>
<p>In order to set up a custom news feed, you'll need to follow these steps:</p>
<ol>
<li>Set Up the Custom API Gateway</li>
<li>Map the API to a DataSource within OptiSigns</li>
<li>Create a News Feed Using OptiSigns Designer</li>
</ol>
<p><a name="Gateway"></a></p>
<h3 id="h_01JCGEGWN32K8QE6J9BE5WXGP9"><span style="color: #434343;">Step 1: Setting Up a Custom API Gateway (SharePoint Example)</span></h3>
<p>We cover most of the details of this step in our <a href="https://support.optisigns.com/hc/en-us/articles/22875592994195-How-to-Integrate-API-and-Publish-API-Data-via-OptiSync"><span class="wysiwyg-underline" style="color: #1155cc;">How to Integrate API and Publish API Data via OptiSync</span></a> guide. Please see that guide for a step-by-step process.</p>
<p>However, there are a few elements which are specific to connecting to a SharePoint API (or a variety of resources in Microsoft 365), which we will cover here.</p>
<p><a name="Endpoint"></a></p>
<h4 id="h_01JCGEGWN3YWNXPZCJ55KT0192"><span style="color: #666666;">Choosing the Correct URL Endpoint for SharePoint Connection</span></h4>
<p>There are numerous options for connecting to SharePoint’s API endpoints, and making sure you have the correct one is critical for importing the correct data into OptiSigns. Click here to learn more about <a href="https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/determine-sharepoint-rest-service-endpoint-uris?tabs=http"><span class="wysiwyg-underline" style="color: #1155cc;">Determine SharePoint REST service endpoint URIs</span></a>.</p>
<p>For the purposes of this example, we’ll be using “Site” feature area, meaning the access point will be:</p>
<pre>https://{site_url}/_api/site</pre>
<p><a name="Authentication"></a></p>
<h4 id="h_01JCGEGWN3R4BHJ8K01Y3ZCM47"><span style="color: #666666;">SharePoint API Authentication using OAuth 2.0 in Microsoft Azure</span></h4>
<p>Authentication for SharePoint can be carried out using different methods, but OAuth 2.0 has become the recommended standard. To get started using OAuth 2.0, you’ll need to <a href="https://learn.microsoft.com/en-us/azure/healthcare-apis/register-application" target="_blank" rel="noopener noreferrer">register your application in Azure Active Directory</a>.</p>
<p>Once that's done, you'll need:</p>
<ul>
<li><a href="https://learn.microsoft.com/en-us/azure/healthcare-apis/register-application#application-id-client-id" target="_blank" rel="noopener noreferrer"><strong>Client ID</strong></a></li>
<li><a href="https://learn.microsoft.com/en-us/azure/healthcare-apis/register-application#certificates--secrets" target="_blank" rel="noopener noreferrer"><strong>Client Secret Value</strong></a></li>
</ul>
<p>These are required for authentication. Any further authentication can be done in the Pre-Request stage to obtain access tokens. These authentication tokens will need to be kept refreshed: see <a href="https://learn.microsoft.com/en-us/entra/identity-platform/certificate-credentials" target="_blank" rel="noopener noreferrer">Microsoft's article on identity platform certificate credentials</a> for more information.</p>
<p>When paired with an “Accept” value, this will provide authentication for your API request. You’ll need the following values:</p>
<pre>Authorization: "Bearer " + accessToken<br>Accept: "application/json;odata=verbose"</pre>
<p>These values should be input under the <strong>Header </strong>tab when setting up your API request:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35337756499091" alt="api gateway header tab" width="624" height="228"></p>
<p>Be sure to <strong>Enable this Request</strong> before moving to the next step.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35337746496019" alt="api gateway enable this request" width="441" height="474"></p>
<p><a name="DataSource"></a></p>
<h3 id="h_01JCGEGWN35EDRBT5XFM7VAAV5"><span style="color: #434343;">Step 2: Mapping the API to a DataSource</span></h3>
<p>We cover most of the details of this step in our <a href="https://support.optisigns.com/hc/en-us/articles/29217646663187-How-to-Set-Up-Dynamic-Data-Mapping-with-OptiSync"><span class="wysiwyg-underline" style="color: #1155cc;">How to Set Up Dynamic Data Mapping via OptiSync</span></a>. If imported correctly, your data will appear in JSON format, like this:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35337756509075" alt="json data map optisigns" width="624" height="325"></p>
<p>Your news stories will have similar data sets if you’re following this guide. The most important data fields are:</p>
<ul>
<li>“Title”</li>
<li>“Description”</li>
<li>“Banner Image URL”
<ul>
<li>Inputting this URL will display the banner image.</li>
</ul>
</li>
</ul>
<div>
<table style="width: 100%;">
<colgroup> <col> </colgroup>
<tbody>
<tr>
<td style="text-align: center;"><strong>NOTE</strong></td>
</tr>
<tr>
<td>You will also want to make note of the “PromotedState” data value. These will be useful for applying filters later on. Other values can also be made use of with Filters, should you so desire.</td>
</tr>
</tbody>
</table>
</div>
<p><a name="Designer"></a></p>
<h3 id="h_01JCGEGWN3MGKJ5J0CZAH0ZB2K"><span style="color: #434343;">Step 3: Creating a News Feed Using Designer in OptiSigns</span></h3>
<p>The next step is getting these values onto your screens and make them automatically update.</p>
<p>To get started, find your design or create a new one in the <strong>Files/Assets </strong>tab.</p>
<p>With the design open, click <strong>"DataSource" </strong>in the left hand column. Then, click <strong>"Add DataSource" </strong>to add an API data source to the design.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/43089455677587" alt="firefox_ZFaS9dNCeY.jpg"></p>
<p>Scroll down to where it says <strong>"API Gateway"</strong> and click it.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35337746511251" alt="api gateway datasource" width="624" height="224"></p>
<p>You can also set up a multi-time Gateway with the <em>API Gateway Collection</em><strong><em>. </em></strong>For this example, we’ll stick with the single-use API Gateway.</p>
<p>You should see this screen:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35337756519187" alt="api datasource ui optisigns" width="624" height="448"></p>
<ul>
<li>
<strong>Name - </strong>The name of the DataSource. This is internally facing and will not be shown on your screens.</li>
<li>
<strong>Select APIs - </strong>Here you'll select from the API Gateways you've already set up in earlier steps. You can select just one, or multiple. If multiple are selected, the API DataSource will automatically aggregate them.</li>
<li>
<strong>Update Interval - </strong>How often to send requests back to the API for updates. Select from None (never call the API back), 30 minutes, 60 minutes, or every 6 hours. If you Enable WebHook on your API Request and input the provided URL in your API, this Update Interval will change to near real-time.</li>
</ul>
<p>Hit <strong>Save</strong>, and the DataSource is created.</p>
<p>It should appear in the left column under <strong>"Used in this design". </strong>It will definitely appear in the <strong>"Other DataSources" </strong>section. You may need to refresh the page for it to appear.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35337746518163" alt="datasource sharepoint news demo example" width="293" height="53"></p>
<p><a name="Element"></a></p>
<h4 id="h_01JCGEGWN438EM9SG8KPBG15W7"><span style="color: #666666;">Element Mapping</span></h4>
<p>Now that you've got your API DataSource has been created, we're ready to map the data. In this example, we will show you how to make a SharePoint News feed.</p>
<h5 id="h_01JCGEGWN4VC8YPY7ZVQ93H9H9"><span style="color: #666666;">Adding Text Elements to a Digital Menu Board</span></h5>
<p>First, create your design. You can make use of one of our repeater templates, or make the design yourself. Our repeater templates can be customized to fit in with your company branding.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35337756524691" alt="custom news feed with text elements" width="624" height="344"></p>
<p>The easiest way to set up a Custom News feed is with a <strong>Data Repeater</strong>. For a full breakdown of a Repeater's capabilities,<a href="https://support.optisigns.com/hc/en-us/articles/29217646663187"> <span class="wysiwyg-underline" style="color: #1155cc;">see this article</span></a>. Here, we'll stick to teaching how to add information from your API.</p>
<p>To set up a Repeater, click <strong>"Repeaters" → Add Blank Repeater</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/43089455679123" alt="ShareX_gnoDiLL4vn.jpg"></p>
<p>With the Repeater selected, click <strong>Settings</strong>. A new pane will open up on the right. Here, select <strong>Connect to DataSource</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/43089455679763" alt="firefox_Y7ut4qGqj7.jpg"></p>
<p>Select the DataSource you set up in the last set under <strong>"Other DataSources"</strong>.</p>
<p>You'll be taken back to the last pane with your DataSource now selected. Now, click <strong>Edit</strong> or double click the selected Repeater to head to the Repeater Editor. This is like a design-within-a-design, specifically for your Repeater (news) items. With text selected, click the arrow on the left.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/43089455680531" alt="firefox_6lEOTf7EZu.jpg"></p>
<p>That brings up the DataSource tab. Click on the DataSource Used in this Design and you'll see something like this:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/43089455681043" alt="firefox_0ZMcdeWGwF.jpg"></p>
<p>In this example, we want to display the title of the piece, its associated imagery, and the story itself.</p>
<p>By creating text and dragging data points to it, we can create a news feed like this:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35337756558355" alt="example news feed" width="624" height="204"></p>
<p>This was created by finding data points from the API and dragging them into the desired text boxes. In this case, we only wish to display the "Title,” “Banner URL Image,” and "Description" so those values were dragged into a blank or existing text box.</p>
<p>The value of a repeater is that it will copy the format of this one cell, then replace the data points with others from your API. It will pull as many data points as you have set up on your API. In this example, we’ve featured only one news story. The repeater will rotate through the rest, displaying only one at a time. If you want to display more, the number of repeated items and their formatting can be changed using these options under <strong>Settings: </strong></p>
<p><img src="https://support.optisigns.com/hc/article_attachments/43089441903379" alt="firefox_9ieNkZ0FYJ.jpg"></p>
<p>If we change the total items to, say, 3, we can get a news feed like this with a little bit of design work:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35337746553235" alt="three story news feed example" width="624" height="349"></p>
<p>Hopefully this is an effective demonstration of some of OptiSync’s abilities.</p>
<p><a name="Filters"></a></p>
<h3 id="h_01JCGEGWN4QKH0A010MPH21ZG8"><span style="color: #434343;">Applying Filters to Customize Which News Stories to Display</span></h3>
<p>What news stories you wish to display may vary depending on a number of factors. In order to filter out undesired or redundant stories, you can make use of the OptiSigns <strong>DataSource</strong> <strong>Filter</strong>.</p>
<p>To get started, highlight the data you want to filter, then hit <strong>Settings. </strong>Next, hit the <strong>Filter</strong> option under your DataSource.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/43089441904659" alt="firefox_yyCyvxGXBi.jpg"></p>
<p>This screen will appear:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/43089441904915" alt="firefox_M6EvhPuhbI.jpg"></p>
<p>What follows is, essentially, an<a href="https://support.microsoft.com/en-us/office/and-function-5f19b2e8-e1df-4408-897a-ce285a19e9d9"> <span class="wysiwyg-underline" style="color: #1155cc;">AND statement</span></a> or an<a href="https://support.microsoft.com/en-us/office/and-function-5f19b2e8-e1df-4408-897a-ce285a19e9d9"> <span class="wysiwyg-underline" style="color: #1155cc;">OR statement</span></a> you might use in Excel or Google Sheets. The easiest way to understand the Filter option is as an Excel or Google Sheet formula you input within OptiSigns.</p>
<p>You can add <strong>Rules</strong> or <strong>RuleSets</strong> to your filter to create as much complexity as you need:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35337756575507" alt="datasource filter option rulesets" width="624" height="339"></p>
<p>In order to set up a Rule, you’ll need to configure three values.</p>
<p>Selecting the first box gives you these options:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35337756579731" alt="filter first box options" width="354" height="192"></p>
<p>By default, these options equate to the <strong>headers of the data mapped to the source.</strong> This list will vary in length depending on how many headers you have. You can also input any value you wish by typing it in the box.</p>
<p>The second box is your <strong>Variable.</strong> OptiSigns provides these options:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35337746579347" alt="filter variable data" width="163" height="397"></p>
<p>The final option provides the following default values:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/35337756591251" alt="filter final options" width="393" height="183"></p>
<p>By default, these map to a screen or other device, allowing your filter to target only certain screens.</p>
<p>However, this value <strong>can be changed to anything you want.</strong> Simply type any value you wish.</p>
<p>There are dozens of possibilities using the OptiSync filter to show even more precise automated data on your screens.</p>
<div>
<table style="width: 100%;">
<colgroup> <col> </colgroup>
<tbody>
<tr>
<td style="text-align: center;"><strong>TIP</strong></td>
</tr>
<tr>
<td>
<p>Remember the “PromotedState” data value from before? If you want to make sure only custom news articles appear on your screen, try setting the Filter to state:</p>
<p><strong>PromotedState - Equals - 2</strong></p>
<p>This should filter out any other pieces of data received from the API.</p>
</td>
</tr>
</tbody>
</table>
</div>
<h3 id="h_01JCGEGWN4Z2N7X6ZHZSBWG3D2"><span style="color: #434343;">That’s all!</span></h3>
<p id="h_01JCGEGWN4HEHVZNH5PTTMZPS4">OptiSigns is the leader in <a href="https://www.optisigns.com/"><span class="wysiwyg-underline" style="color: #1155cc;">digital signage software</span></a>. If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com"><span class="wysiwyg-underline" style="color: #1155cc;">support@optisigns.com</span></a>.</p>