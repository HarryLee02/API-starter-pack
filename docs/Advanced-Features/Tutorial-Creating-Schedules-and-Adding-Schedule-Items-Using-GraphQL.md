<p id="docs-internal-guid-761b6eea-7fff-c314-e9fe-dfeb3ba075fb">Using GraphQL, it’s possible to create a schedule on OptiSigns, then add items to it and assign values to them. We’ll cover each of these steps in turn.</p>
<p><strong>1. Creating a New Schedule</strong></p>
<p>To create a new schedule, we’ll need a specific Mutation:</p>
<pre>mutation CreateSchedule($payload: ScheduleInput!, $teamId: String)<br><br>{saveSchedule (payload:$payload,teamId:$teamId){<br>   _id,<br>   accountId,<br>   createdAt,<br>   createdBy,<br>   groupId,<br>   lastTeamId,<br>   lastUpdatedBy,<br>   lastUpdatedDate,<br>   name,<br>   path,<br>   tags,<br>   teamId<br>   }<br>}</pre>
<p><strong>Variables:</strong></p>
<pre>{“payload”: {<br>   “groupId”:<br>   “Name”:<br>   “Path”:<br>   “Tags”:<br>   “teamId”:<br>   }<br>}</pre>
<p><img src="https://support.optisigns.com/hc/article_attachments/36558841524243" width="624" height="699"></p>
<p>This Mutation creates a brand new schedule, as you can see from the data to the right:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/36558841526675" width="595" height="465"></p>
<p><strong>2. Updating Schedules</strong></p>
<p>This same Mutation can be used to update the schedule itself. In order to update the schedule, you’ll need to input the “_id” value in the payload:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/36558841527955" width="624" height="228"></p>
<p>Doing this will update the existing schedule.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/36558841534483" width="567" height="421"></p>
<p><strong>3. Adding Assets or Playlists to the Schedule</strong></p>
<p>Now, we’ll want to add an item to the schedule. For that, we’ll need another Mutation:</p>
<pre>mutation addScheduleItem($force:Boolean,$payload: AddScheduleItemInput!, $teamId: String!){<br><br>  addScheduleItem(force:$force,payload:$payload,teamId:$teamId){<br><br>         _id,<br><br>       name,<br><br>       assetId,      <br><br>       teamId,<br><br>       playlistId,<br><br>       repeatObject{<br><br>         id,<br><br>         repeat,<br><br>         text,<br><br>         type,<br><br>         rrule<br><br>       },<br><br>       range{startDate,endDate},<br><br>       documentDuration<br><br>  }<br><br>}</pre>
<p><img src="https://support.optisigns.com/hc/article_attachments/36558841535507" width="624" height="316"></p>
<p><strong>Variables:</strong></p>
<pre>{"force": false,<br> "payload": {"scheduleId": "",<br>            "assetId": "",<br>            "playlistId":"",<br>            "type": "",<br>            "repeatObject": {<br>              "rrule": ""<br>            },<br>             "range": {<br>               "startDate": "",<br>               "endDate": ""<br>            }<br>     },<br> "teamId": ""<br>}</pre>
<p><img src="https://support.optisigns.com/hc/article_attachments/36558834984339" width="624" height="296"></p>
<p>When the values are set up correctly, your data should display like this:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/36558834986643" width="541" height="581"></p>
<p><strong>4. Editing Schedule Items</strong></p>
<p>Once you’ve created a schedule and set an item on it, it’s possible to edit those items. This requires yet another Mutation:</p>
<pre>mutation updateScheduleItem($force:Boolean,$payload: UpdateScheduleItemInput!, $scope: APPLY_SCHEDULE_ITEM_SCOPES!){<br><br>  updateScheduleItem(force:$force,payload:$payload,scope:$scope){<br>       _id,<br>       name,<br>       assetId,      <br>       teamId,<br>       playlistId,<br>       repeatObject{<br>         id,<br>         repeat,<br>         text,<br>         type,<br>         rrule<br>       },<br>       range{startDate,endDate},<br>       documentDuration<br>  }<br>}</pre>
<p><img src="https://support.optisigns.com/hc/article_attachments/36558834989843" width="624" height="251"></p>
<p>With this mutation, we’ll input these variables:</p>
<pre>{"force": false,<br> "payload": {"_id": "",<br>            "assetId": "",<br>            "playlistId":"",<br>            "repeatObject": {<br>              "rrule": ""<br>             },<br>            "range": {<br>              "startDate": "",<br>              "endDate": ""<br>            }<br> },<br> "scope": ""<br>}</pre>
<p><img src="https://support.optisigns.com/hc/article_attachments/36558834991379" width="624" height="252"></p>
<p>Here, we’ve changed the repeat frequency from daily to weekly, and the start date from December 18, 2024 to December 20, 2024. This is reflected in the data retrieved:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/36558841549075" width="624" height="476"></p>
<p><strong>Previous Article - <a href="https://support.optisigns.com/hc/en-us/articles/36562094987795-Tutorial-Creating-or-Updating-Website-Assets-Using-GraphQL" target="_blank" rel="noopener noreferrer">Tutorial: Creating or Updating Website Assets Using GraphQL</a></strong></p>
<p><strong>Next Article - <a href="https://support.optisigns.com/hc/en-us/articles/4414558369811-Pagination" target="_blank" rel="noopener noreferrer">Pagination</a></strong></p>