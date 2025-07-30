<p id="docs-internal-guid-7d3df2c0-7fff-0879-e9e7-0eda2e804dd3">Using GraphQL, it is possible to create a website asset on OptiSigns.</p>
<table style="border-collapse: collapse; width: 100%; height: 44px;" border="1">
<tbody>
<tr style="height: 22px;">
<td class="wysiwyg-text-align-center" style="width: 100%; height: 22px;"><strong>NOTE</strong></td>
</tr>
<tr style="height: 22px;">
<td style="width: 100%; height: 22px;">At this time, this Mutation is primarily used to create or update Website assets.</td>
</tr>
</tbody>
</table>
<p><strong>1. Creating a New Website Asset</strong></p>
<p>To do this, we’ll need to create a specific Mutation:</p>
<pre>mutation saveAsset ($payload: AssetInput!, $teamId: String)<br>{saveAsset (payload:$payload,teamId:$teamId){<br>  _id<br>  originalFileName<br>  webLink<br>  webType<br>  fileType<br>  }<br>}</pre>
<p><strong>Variables:</strong></p>
<pre>{<br>  "payload": {<br>    "originalFileName": "",<br>    "webLink": "",<br>    "webType": "",<br>    "fileType": ""<br>  }<br>}</pre>
<p><img src="https://support.optisigns.com/hc/article_attachments/36562094972435" width="561" height="563"></p>
<p>This Mutation, once run, will create a new asset:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/36562091083539" width="431" height="277"></p>
<p>This asset can now be assigned to a device, queried for additional information, or added to a playlist or schedule.</p>
<p><strong>2. Updating Assets</strong></p>
<p>Updating assets is as simple as running the same Mutation while providing an _id field. This can be done for any asset type, not just website assets, but we will be using a website asset as an example.</p>
<p><strong>Variables:</strong></p>
<pre>{<br>  "payload": {<br>    "_id": "",<br>    "originalFileName": "",<br>    "webLink": "",<br>    "webType": "",<br>    "fileType": ""<br>  }<br>}</pre>
<p><img src="https://support.optisigns.com/hc/article_attachments/36562091085843" width="497" height="203"></p>
<p><strong>Previous Article - <a href="https://support.optisigns.com/hc/en-us/articles/4414558295955-Tutorial-Create-Update-Add-Remove-items-from-Playlists" target="_blank" rel="noopener noreferrer">Tutorial: Create, Update, Add, Remove Items from Playlists</a></strong></p>
<p><strong>Next Article - <a href="https://support.optisigns.com/hc/en-us/articles/36558834998291-Tutorial-Creating-Schedules-and-Adding-Schedule-Items-Using-GraphQL" target="_blank" rel="noopener noreferrer">Tutorial: Creating Schedules and Adding Schedule Items Using GraphQL</a></strong></p>