<p>If you need to configure the firewall, here is the list of OptiSigns IP addresses and Port to whitelist:</p>
<p>Port: please whitelist HTTPS port 443</p>
<p>IP Address for <strong>OptiSigns</strong>:</p>
<ul>
<li>*.optisigns.com</li>
<li>api.optisignsapp.com</li>
<li>api.optisigns.com</li>
<li>api-prod-2.optisigns.com</li>
<li>api-prod-3.optisigns.com</li>
<li>api-prod-4.optisigns.com</li>
<li>ws-prod-1.optisigns.com</li>
<li>ws-prod-2.optisigns.com</li>
<li>ws-prod-3.optisigns.com</li>
<li>mdm-ws-prod-1.optisigns.com</li>
<li>mdm-ws-prod-2.optisigns.com</li>
<li>signagecloud-prd.nyc3.cdn.digitaloceanspaces.com</li>
<li>smallapp-api.prod.optisignsapp.com</li>
<li>smallapp.optisigns.com</li>
<li>download.optisigns-cdn.com</li>
<li>52.217.39.148 (File)</li>
<li>162.243.189.2 (Files)</li>
<li>157.230.201.46 (API)</li>
<li>206.189.255.219 (API)</li>
<li>software-update.optisigns.com (Pro Player OTA update)</li>
<li>software-download.optisigns.com (Pro Player OTA update)</li>
</ul>
<p>OptiSigns utilizes Transloadit for <strong>uploading files via the OptiSigns portal</strong>. If you encounter any issues with uploading files, you can resolve this by whitelisting Transloadit's IP address.</p>
<ul>
<li>*.transloadit.com</li>
<li>*.*.transloadit.com</li>
<li>s3.amazonaws.com</li>
<li>s3-eu-west-1.amazonaws.com</li>
</ul>
<p>OptiSigns utilizes Unsplash images in the <strong>Designer app</strong>. If you encounter any issues with using free Unsplash images, you can resolve this by whitelisting Unsplash's IP address.</p>
<ul>
<li>plus.unsplash.com</li>
<li>images.unsplash.com</li>
</ul>
<p>OptiSigns utilizes RealVNC for <strong>Remote Device Control</strong>. If you use remote control and experience any connection issues with remote control, you can resolve this by whitelisting RealVNC's domain and IP address.</p>
<ul>
<li>*.services.vnc.com</li>
</ul>
<p>OptiSigns utilizes Sport Pulse for <strong>Sports Feeds</strong>. If you have an issue displaying the sports feed, you can resolve this by whitelisting Sport Pulse's domain and IP address.</p>
<ul>
<li>sportpulse.app</li>
</ul>
<p>IP Address for <strong>AeriCast</strong>:</p>
<ul>
<li>screenshare.aericast.com</li>
<li>present.aericast.com</li>
<li>apps-api-prd.aericast.com<strong><br></strong>
</li>
</ul>
<p><strong>IMPORTANT NOTE:</strong> we use CDN to optimize file distribution to your devices. Some firewalls may block CDNs. If you experiencing issues where your device is online, but when you assign files, it's just a black screen because the device cannot download files. You can contact us at <a href="mailto:support@optisigns.com">support@optisigns.com</a> to disable the CDN feature for your account. (Note: It requires the Engage or Enterprise Plan)</p>
<p>There's no set of IP addresses for Social Media and some other apps like Facebook, Instagram, YouTube, and Google Calendar, so if you restrict HTTPS access by IP, you may not be able to use those apps.</p>