<p>Subscriptions are a query type that allows you to be notified when any changes are made to a device, asset, or playlist. </p>
<p>An example might be that you want to be notified of any changes made to your device, be that changing the asset or playlist. This can be done entirely within GraphQL by using queries to find the information about a device, setting up a subscription, then using mutations to alter the device attributes.</p>
<h3 id="h_01JFDF0RN3V7WXP3V4NQ4ZC5PH"><strong>1. Set Up the Subscription</strong></h3>
<pre class="wysiwyg-text-align-justify">subscription subscribe($_id:String,$type:OBJECT_TYPES){<br><br>  subscribe(_id:$_id,type:$type){<br><br>    _id,<br><br>    mutation,<br><br>    teamId<br><br>    type<br><br>  }<br><br>}</pre>
<p class="wysiwyg-text-align-justify"><strong>Variables</strong></p>
<pre class="wysiwyg-text-align-justify">{"_id":"",<br><br>  "type": ""<br><br>}</pre>
<p><img src="https://support.optisigns.com/hc/article_attachments/36558469943443" width="624" height="499"></p>
<p>Note the elements present in the Subscription query. These are the elements it will monitor, and return to you when any of them are changed via Mutation.</p>
<p>When a Subscription is properly input, you should see this on the right side of the GraphQL UI:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/36558442820115" width="227" height="66"></p>
<p>This means, as long as the Subscription is active, it will report any changes to the item.</p>
<h3 id="h_01JFDF13V59TVZ8MFFX2S1C8SZ"><strong>2. Testing the Subscription</strong></h3>
<p>Here, we have a Mutation script that is changing the name and playlist on the selected device.</p>
<pre class="wysiwyg-text-align-justify">mutation updateDevice($_id: String!,$payload: UpdateDeviceInput!, $teamId: String){<br>  updateDevice(_id:$_id,payload:$payload,teamId:$teamId){<br>     _id,<br>     deviceName,<br>     UUID,<br>     pairingCode,<br>     currentType,<br>     currentAssetId,<br>     currentPlaylistId,<br>     path,<br>     localAppVersion<br>  }<br>}</pre>
<p class="wysiwyg-text-align-justify"><strong>Variables</strong></p>
<pre class="wysiwyg-text-align-justify">{"_id": "",<br>  "payload": {"deviceName": "",<br>    "currentType": "",<br>    "currentAssetId": “”,<br>    "currentPlaylistId": "",<br>    "orientation": "LANDSCAPE"<br>  } <br>} </pre>
<p><img src="https://support.optisigns.com/hc/article_attachments/36558442824211" width="624" height="531"></p>
<p>When we perform this Mutation, we can switch over to where our Subscription is Listening and see this:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/36558469955603" width="624" height="311"></p>
<p><strong>Previous Article - <a href="https://support.optisigns.com/hc/en-us/articles/4414564078995-Error-Handling" target="_blank" rel="noopener noreferrer">Error Handling</a></strong></p>
<p><strong>Next Article - <a href="https://support.optisigns.com/hc/en-us/articles/4414558392339-API-Reference" target="_blank" rel="noopener noreferrer">API Reference</a></strong></p>