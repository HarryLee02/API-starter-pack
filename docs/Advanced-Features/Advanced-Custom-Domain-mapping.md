<p>With OptiSigns Pro and Enterprise plan, you can enhance your branding by mapping your custom domain for OptiSigns Management Portal.</p>
<p> </p>
<p>For example: you can map your sub-domain: <strong>login.abcmedia.com</strong> so that your users can log in and use the portal from <strong>login.abcmedia.com</strong> and use the app like the screenshot below.</p>
<p> </p>
<p class="wysiwyg-text-align-center"><img src="https://support.optisigns.com/hc/article_attachments/1500000517302" alt="mceclip0.png"></p>
<p> </p>
<h4 id="h_01HQ0AM0SJ64Y0NCCC8ETQ2MAB"><strong>Let's jump in and get started!</strong></h4>
<p><strong>1) Activate your OptiSigns sub-domain (in this example: abcmedia.optisigns.net):</strong></p>
<p>Go to the Branding page of your Account Management Settings:</p>
<p><a href="https://app.optisigns.com/app/s/branding-settings">https://app.optisigns.com/app/s/branding-settings</a></p>
<p>Type in your desired sub-domain for optisigns.net. In this case, we type in "abcmedia".<br>Don't worry about optisigns.net, you will map your domain in the next step.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/360099399934" alt="mceclip2.png"></p>
<p><strong>2) Map CNAME alias for your domain/sub-domain:</strong></p>
<p>In your Domain DNS management, map your desired domain/sub-domain to your OptiSigns sub-domain using CNAME Alias.<br>In this example, we map: login.abcmedia.com -&gt; abcmedia.optisigns.net</p>
<p>Refer to your domain host documentation for more specific details.</p>
<p>Here are the generic steps:</p>
<ol class="spaced-list">
<li>Go to your domain’s DNS records.</li>
<li>Add a record to your DNS settings, selecting <strong>CNAME</strong> as the record type.</li>
<li>Return to the first window or tab and copy the contents of the <strong>Label/Host</strong> field.</li>
<li>Paste the copied contents into the <strong>Label</strong> or <strong>Host</strong> field with your DNS records.</li>
<li>Return to the first window or tab and copy the contents of the <strong>Destination/Target</strong> field.</li>
<li class="" data-outlined="false">Paste the copied contents into the <strong>Destination</strong> or <strong>Target</strong> field with your DNS records.
<p>Your record should look similar to one of the tables below:</p>
<p class="align-center"><strong>CNAME Record</strong></p>
<table class="wide nice-table no-stripes">
<thead>
<tr>
<th>Record type</th>
<th>Label/Host field</th>
<th>Time To Live (TTL)</th>
<th>Destination/Target field</th>
</tr>
</thead>
<tbody>
<tr>
<td class="align-center" data-outlined="true">CNAME</td>
<td class="align-center" data-outlined="true">login</td>
<td class="align-center" data-outlined="true">3600 or leave the default</td>
<td class="align-center" data-outlined="true">abcmedia.optisigns.net</td>
</tr>
</tbody>
</table>
</li>
<li>Save your record.<br>CNAME record changes can take up to 72 hours to go into effect, but typically they happen much sooner.</li>
</ol>
<p>Here are links to documentation from some popular domain hosts:</p>
<ul>
<li><a href="https://www.godaddy.com/help/add-a-cname-record-19236" target="_self">GoDaddy</a></li>
<li><a href="https://www.namecheap.com/support/knowledgebase/article.aspx/9646/2237/how-to-create-a-cname-record-for-your-domain/" target="_self">Namecheap</a></li>
<li><a href="https://my.bluehost.com/hosting/help/resource/714" target="_self">Bluehost</a></li>
<li><a href="https://www.ionos.com/help/domains/configuring-cname-records-for-subdomains/configuring-a-cname-record-for-a-subdomain/" target="_self">1&amp;1 IONOS</a></li>
<li><a href="https://www.hostgator.com/help/article/how-to-change-dns-zones-mx-cname-and-a-records" target="_self">HostGator</a></li>
<li><a href="https://help.dreamhost.com/hc/en-us/articles/215414867-How-do-I-add-custom-DNS-records-" target="_self">DreamHost</a></li>
<li><a href="https://support.cloudflare.com/hc/en-us/articles/360020615111-Configuring-a-CNAME-setup" target="_self">Cloudflare</a></li>
</ul>
<p><strong>3) Activate SSL for your sub-domain</strong></p>
<p>Once you have done step 2, return to the Branding page:</p>
<p><a href="https://app.optisigns.com/app/s/branding-settings">https://app.optisigns.com/app/s/branding-settings</a></p>
<p>Enter the domain/sub-domain you have configured in Step 2 in Your domain section.</p>
<p>In this example, we use: login.abcmedia.com</p>
<p>Then click Activate.</p>
<p>This will trigger the process on OptiSigns side to activate SSL for your sub-domain. This will ensure that your user can use HTTPS: i.e. <a href="https://login.abcmedia.com">https://login.abcmedia.com</a> to use the app.</p>
<p>This process can take up to 24-48 hours to complete. You will be notified via email once it's done.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/360101613533" alt="mceclip3.png"></p>
<p> </p>
<h4 id="h_01HQ0AM0SKDGJ97MKSF9SRPC1A"><strong>That's all!</strong></h4>
<p>Once you get the notification that your SSL is activated, you can start using your own domain/sub-domain (i.e. <a href="https://login.abcmedia.com">https://login.abcmedia.com</a>).</p>