<div class="x_VfD">
<div class="_zLbN _1szKo" tabindex="-1" data-hook="post-title"> </div>
</div>
<p class="_2dmGl x_VfD"> </p>
<div class="_3uWjK" data-hook="post-description">
<article class="blog-post-page-font">
<div class="post-content__body">
<div class="_2FZkM">
<div class="kcuBq xGuFA blog-post-page-font TCKPQ uatYj _1Ss7I" dir="ltr">
<div class="kaqlz _1PiV3 blog-post-page-font css-juod2b">
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">There are different codecs that used by videos, such as H264, HEVC, VP9, Mpeg-4, AV1. The support of the codec are dependent on the hardware, when the codec is not supported by the device used for video playback, you may see this error screen like below on OptiSigns. Or it could be simply that the video playback is slow and dropping frames, because it is use software decoding instead of hardware decoding. Similarly, when the video resolution or bit rate is too high for the hardware to handle, you may experience the same issue. </p>
<p class="undefined">Here are some options you can try to resolve the issue:</p>
<ul>
<li class="undefined">Try a different video player</li>
<li class="undefined">Re-encode the video</li>
</ul>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_"> <img class="_1Fjtc _2lDdg" src="https://static.wixstatic.com/media/e48f7f_1bfd9d9fa0754778b1981f98e092ebba~mv2.png/v1/fill/w_1920,h_1080,al_c,q_90/e48f7f_1bfd9d9fa0754778b1981f98e092ebba~mv2.webp" data-pin-url="https://www.optisigns.com/post/video-playback" data-pin-media="https://static.wixstatic.com/media/e48f7f_1bfd9d9fa0754778b1981f98e092ebba~mv2.png/v1/fit/w_1920,h_1080,al_c,q_80/file.png"></p>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_"> </p>
<h3 id="h_01J83894RXV6S4GQZ9GE0XVYF3"><strong>Try a different video player</strong></h3>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">To improve the supportability of different codecs, we provided users options to use different video players on different devices.</p>
<p class="undefined">For example, with OptiSigns Pro player, you can choose to use HTML5 video player or MPV player for video playback on the OptiSigns portal under Edit Screen. Or if you are using RPi with OptiSigns pre-built image, you can choose between HTML5 Video Player, OMX player or MPV player.</p>
<p class="undefined"><img src="https://support.optisigns.com/hc/article_attachments/33541399817619"></p>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_"> </p>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">If you are using Android devices, you can open the side menu of the player and go to Video Player Settings. This will allow you to change between Texture View and Surface View. Changing from the default Texture View to Surface View may provide better performance on certain hardware if the hardware is optimized only for Surface View. <img src="https://support.optisigns.com/hc/article_attachments/33541375854355"></p>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_"> </p>
<p class="undefined"> </p>
<h3 id="01J8389SSCBC33XEZGYYY76ZG3"><strong>Re-encode the video</strong></h3>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">H264 is the most widely supported codec, VP9 and HEVC(H265) are well supported by a lot of the hardware as well. However, there could be times when codec is not recognized or support by your devices. For example, here's a link to Amazon's <a class="_2qJYG blog-link-hashtag-color _3sz0l" href="https://developer.amazon.com/docs/fire-tv/device-specifications.html" target="_blank" rel="noopener"><u class="sDZYg">supported codec</u></a>.</p>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">To solve the problem you will need to convert/re-encode your video into something that Amazon or your Android device support.</p>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">There's a <a class="_2qJYG blog-link-hashtag-color _3sz0l" href="https://handbrake.fr/" target="_blank" rel="noopener"><u class="sDZYg">Handbreak is a free</u></a> and very popular software to do that. It runs on Windows, Mac and Linux.</p>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">To re-encode your video.</p>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">Download, Run Handbreak.</p>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">Drag your video in there.</p>
<div class="q2uC4 _2vlB-">
<div class="_2CvYQ c-Mgr _1K2V0 _1K2V0 _1hD8w">
<div class="_1Lhwj image-container" data-hook="imageViewer">
<div class="xdJBZ"><img class="_1Fjtc _2lDdg" src="https://static.wixstatic.com/media/e48f7f_13b3c91823cf4467a56ca8d221b9b043~mv2.jpg/v1/fill/w_1257,h_842,al_c,q_90/e48f7f_13b3c91823cf4467a56ca8d221b9b043~mv2.webp" data-pin-url="https://www.optisigns.com/post/video-playback" data-pin-media="https://static.wixstatic.com/media/e48f7f_13b3c91823cf4467a56ca8d221b9b043~mv2.jpg/v1/fit/w_1257,h_842,al_c,q_80/file.png"></div>
<div class=""> </div>
</div>
</div>
</div>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">Select the output format you desired.</p>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">Amazon, Android or General would work. Pick appropriate video resolution you want too.</p>
<div class="q2uC4 _2vlB-">
<div class="_2CvYQ c-Mgr _1K2V0 _1K2V0 _1hD8w">
<div class="_1Lhwj image-container" data-hook="imageViewer">
<div class="xdJBZ"><img class="_1Fjtc _2lDdg" src="https://static.wixstatic.com/media/e48f7f_82c690e3d69f4e23a49e1f209e119299~mv2.jpg/v1/fill/w_1257,h_842,al_c,q_90/e48f7f_82c690e3d69f4e23a49e1f209e119299~mv2.webp" data-pin-url="https://www.optisigns.com/post/video-playback" data-pin-media="https://static.wixstatic.com/media/e48f7f_82c690e3d69f4e23a49e1f209e119299~mv2.jpg/v1/fit/w_1257,h_842,al_c,q_80/file.png"></div>
<div class=""> </div>
<div class=""> </div>
</div>
</div>
</div>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">Select a location you want the new video file to be output to.</p>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">Click Start.</p>
<div class="q2uC4 _2vlB-">
<div class="_2CvYQ c-Mgr _1K2V0 _1K2V0 _1hD8w">
<div class="_1Lhwj image-container" data-hook="imageViewer">
<div class="xdJBZ"><img class="_1Fjtc _2lDdg" src="https://static.wixstatic.com/media/e48f7f_5ffa6467b7ee4474a3fbc6e7d9bb9918~mv2.jpg/v1/fill/w_1257,h_842,al_c,q_90/e48f7f_5ffa6467b7ee4474a3fbc6e7d9bb9918~mv2.webp" data-pin-url="https://www.optisigns.com/post/video-playback" data-pin-media="https://static.wixstatic.com/media/e48f7f_5ffa6467b7ee4474a3fbc6e7d9bb9918~mv2.jpg/v1/fit/w_1257,h_842,al_c,q_80/file.png"></div>
<div class=""> </div>
<div class=""> </div>
</div>
</div>
</div>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">Depend on video length and quality, and how fast your computer is. It could take some time.</p>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">When it's done, you can upload the file back to OptiSigns and assign to your playlists, screens.</p>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_"> </p>
<p class="XzvDs _208Ie _2Dym_ blog-post-text-font blog-post-text-color _2QAo- _25MYV _2R0Lu _2Dym_">If you have further questions, issues, please feel free to contact us at <a class="_2qJYG blog-link-hashtag-color _3sz0l" href="mailto:support@optisigns.com" target="_top" rel="noreferrer"><u class="sDZYg">support@optisigns.com</u></a></p>
</div>
</div>
</div>
</div>
</article>
</div>