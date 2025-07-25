<h3 id="h_01JZX1KT0B9BZAP82JXKNN264Z"><span style="color: #434343;">In this article, we’ll cover our Legacy DataSources - key-value pair formatting with Google Sheets or Microsoft 365 Excel</span></h3>
<ul>
<li><a href="#HowitWorks">How it Works and When to Use Legacy DataSources</a></li>
<li><a href="#Creating">Creating Data Mapping Elements</a></li>
<li><a href="#Generating">Generating a Google Sheet or Excel Document</a></li>
<li><a href="#Modifying">Modifying the Data</a></li>
</ul>
<p>Using Designer, it’s possible to assign a key value to an element, then map it to a Google Sheet or Microsoft Excel document. This will create a new spreadsheet directly mapped to the individual design. The values on this new spreadsheet can be modified to change what the design displays.</p>
<figure class="wysiwyg-image"><img style="aspect-ratio: 624/233;" src="https://support.optisigns.com/hc/article_attachments/42915203035795" alt="advanced datasources googlesheet or ms excel 365" width="624" height="233"></figure>
<p>Please note that this is an older form of Data Mapping in OptiSigns. Now, with our new OptiSync feature, exsiting Google Sheets or MS Excell sheets can be directly integrated into a design with a simple drag-and-drop. It is also possible to directly connect APIs, JSON, XML, or custom tables. See our article on <a href="https://support.optisigns.com/hc/en-us/articles/29217646663187-How-to-Set-Up-Dynamic-Data-Mapping-with-OptiSync" target="_blank" rel="noopener noreferrer"><strong><span class="wysiwyg-underline">Dynamic Data Mapping using OptiSync</span></strong></a> for more information.</p>
<hr><p><a name="HowitWorks"></a></p>
<h2 id="h_01JZX1KCVTYNKB17ZB8VZE526Q">How it Works and When to Use Legacy DataSources</h2>
<p>This form of Data Mapping follows these steps:</p>
<ol>
<li>Mapping data to individual design elements</li>
<li>Generating a Google or Excel spreadsheet of these elements</li>
<li>Altering the spreadsheet so changes are reflected on the design</li>
</ol>
<p>Different screens can be mapped to the same design so that, depending on where it’s shown, the values will be different.</p>
<p>Legacy DataSources are particularly useful for pairing with our <a href="https://support.optisigns.com/hc/en-us/articles/42436941395475-Widgets-in-Designer#ScrollingText" target="_blank" rel="noopener noreferrer"><strong>Scrolling Text</strong></a> and <a href="https://support.optisigns.com/hc/en-us/articles/42436941395475-Widgets-in-Designer#ScrollingVertical" target="_blank" rel="noopener noreferrer"><strong><span class="wysiwyg-underline">Scrolling Vertical </span></strong><span class="wysiwyg-underline">widgets</span></a>, and if you have numerous elements on a single design you wish to be dynamic.</p>
<hr><p><a name="Creating"></a></p>
<h2 id="h_01JZX1KCVYY3Q7AP8TEYVPYYCR">Creating Data Mapping Elements</h2>
<p>To get started, you’ll need to create a design. To do this, go to <strong>Files/Assets → Apps → Designer</strong>.</p>
<p>For this example, we’ve used one of our <a href="https://canvas.optisigns.com/" target="_blank" rel="noopener noreferrer">pre-built Templates</a> as the design. For yours, you can explore our 5000+ template library, or create a design from scratch. See our article on <a href="https://support.optisigns.com/hc/en-us/articles/42087942047379-Getting-Started-with-Designer" target="_blank" rel="noopener noreferrer"><strong><span class="wysiwyg-underline">Getting Started with Designer</span></strong></a><strong> </strong>if you need help.</p>
<p>Now, we’ll need to add a Data Mapping to an element. Click the Element you want to map to your DataSource, then hit the <strong>Settings </strong>button. Then, click <strong>Make Data Mapping</strong>.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42915219044243" alt="how to make data mapping" width="624" height="145"></p>
<p>The element will automatically be given an <strong>Element ID. </strong>We also recommend giving it an <strong>Asset Element Name</strong>, which will appear on your generated spreadsheet and can help identify what the value is.</p>
<p> <img src="https://support.optisigns.com/hc/article_attachments/42915203032083" alt="data mapping element id and asset element name" width="373" height="545"></p>
<p>There are also additional options:</p>
<ul>
<li>
<strong>Hide when data not available: </strong>When no data is present on the sheet, nothing will display</li>
<li>
<strong>Empty Data Handling:</strong> When there is no DataSource element, the default behavior is to use the default value. You can adjust this with the following options:<ul>
<li>
<strong>Use Default Value:</strong> Show default content, which is what your element looks like originally.</li>
<li>
<strong>Use Blank:</strong> Nothing will display.</li>
</ul>
</li>
</ul>
<p>For more on the <strong>Advanced Options </strong>here, see <a href="https://support.optisigns.com/hc/en-us/articles/29217646663187-How-to-Set-Up-Dynamic-Data-Mapping-with-OptiSync#Property" target="_blank" rel="noopener noreferrer"><strong><span class="wysiwyg-underline">Property Mapping and Display Format</span></strong></a>.</p>
<p>Now, you’ll want to <em><strong>repeat this process for every element you wish to be dynamic</strong></em>. Make sure you do this before you move on to the next step.</p>
<hr><p><a name="Generating"></a></p>
<h2 id="h_01JZX1KCWCNDEFGD0XZED39GVK">Generating a Google Sheet or Excel Document</h2>
<p>Once you’ve mapped all the elements you want to be dynamic, it’s time to generate your spreadsheet. To do this, click the <strong>DataSource </strong>button on the Side Menu, then click <strong>Add DataSource</strong>:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42915203033491" alt="how to add a datasource" width="431" height="661"></p>
<p>Scroll down in the popup to the <strong>Adv. DataSources </strong>section and choose either <strong>Google Sheets (legacy) </strong>or <strong>MS Excel 365 (legacy)</strong> depending on which you prefer.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42915203035795" alt="advanced datasources googlesheet or ms excel 365" width="624" height="233"></p>
<p>Clicking one of these will bring up the option to sign in with your account of choice. </p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42915203036819" alt="choose between google sheet or ms excel datasource" width="624" height="212"></p>
<figure style="width: 100%;" class="wysiwyg-table"><table style="border-style: solid; border-width: 1px;"><tbody>
<tr><td style="border-style: solid; border-width: 1px;"><p class="wysiwyg-text-align-center"><strong>NOTE</strong></p></td></tr>
<tr><td style="border-style: solid; border-width: 1px;">This requires a paid account for Microsoft 365, as the free account does not support this feature. Without a paid MS 365 account, we recommend a Google Sheet.</td></tr>
</tbody></table></figure>
<p>Give the Sheet a <strong>Name</strong>, then sign in to your preferred account. You will need to provide certain permissions for this to work. See our <a href="https://www.optisigns.com/privacy-policy"><span class="wysiwyg-underline">Privacy Policy</span></a> for additional information.</p>
<p>Next, you’ll be asked to provide the Folder for where you want your sheet to be saved. Select one, then continue. Your DataSource will be created:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42915203039123" alt="authorized google sheets datasource example" width="624" height="452"></p>
<figure style="width: 100%;" class="wysiwyg-table"><table style="border-style: solid; border-width: 1px;"><tbody>
<tr><td style="border-style: solid; border-width: 1px;"><p class="wysiwyg-text-align-center"><strong>IMPORTANT</strong></p></td></tr>
<tr><td style="border-style: solid; border-width: 1px;">
<p>Data must be within a table if using Excel Sheets.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42915203043091" alt="excel datasource table example" width="624" height="179"></p>
</td></tr>
</tbody></table></figure>
<p>At this point, you can access your spreadsheet to see the elements you’ve mapped by hitting the <strong>Open </strong>button.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42915219091475" alt="how to open google sheet in optisigns" width="217" height="101"></p>
<p>The elements you’ve mapped will appear in the sheet.</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42915219094419" width="624" height="275"></p>
<hr><p><a name="Modifying"></a></p>
<h2 id="h_01JZX1V1JHYD3BTS9NVW7A27ZY">Modifying the Data</h2>
<p>To change the mapping, simply edit the values in the columns, being sure to keep the Asset Element ID and Asset Element Name the same. </p>
<p>For example, say we want the word “SOCIAL” to appear on one screen in one location, but we want it to say “COMMUNAL” in another. To do this, we simply duplicate the Row, then change the “Screen Name” and “Value” cells:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42915203045779" alt="modified data in datasource" width="624" height="136"></p>
<p>The “Screen Name” will need to be the same as the name of the screen you’re targeting with the asset. This is equivalent to the <strong>Device Name </strong>under the <strong>Edit Screen </strong>tab:</p>
<p><img src="https://support.optisigns.com/hc/article_attachments/42915203048467" alt="device name on edit screen tab" width="583" height="646"></p>
<p>Some best practices:</p>
<ul>
<li>OptiSigns will identify the screens by name and adjust the Value based on what's entered on your spreadsheet.</li>
<li>If you change your screen's name, be sure to update your spreadsheet at the same time. If updated later, it could cause issues with data mapping on the screen at the next update interval.</li>
<li>***ALL*** tells OptiSigns that if a screen is not specifically assigned values, it will take value from this row of data. This is equivalent to the "Default Value" mentioned earlier in the article.<ul><li>If a value is detected, it will override the ***ALL*** value, like in the example above.</li></ul>
</li>
</ul>
<h3 id="27------that-s-all----"><strong>That’s all!</strong></h3>
<p>OptiSigns is the leader in <a href="https://www.optisigns.com/" target="_blank" rel="noopener noreferrer"><span class="wysiwyg-underline">digital signage software</span></a>. If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at <a href="mailto:support@optisigns.com" target="_blank" rel="noopener noreferrer"><span class="wysiwyg-underline">support@optisigns.com</span></a>. </p>