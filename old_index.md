---
title: Home
"<!--layout": default -->
layout: default
---

## "Specialization is for insects" 
-- Robert A. Heinlein
<br>
<br>
I want to make us Smarter, Faster, Stronger, Higher. 
<br>
<br>
Life should be more [epic](http://tvtropes.org/pmwiki/pmwiki.php/Main/ClarkesThirdLaw). 
<br>
<br>

  <h1>Posts</h1>

  <ul class="posts">
    {% for post in site.posts %}
      <li>
        <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
        <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
      </li>
    {% endfor %}
  </ul>

  <p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | prepend: site.baseurl }}">via RSS</a></p>


[lab]:http://www.spacecraftresearch.com/
[cal]:/pages/calendar.html
[projects]:/projects
[resume]:/pages/bzr_resume.pdf
[tractor]: https://www.youtube.com/watch?v=Y-FXqIcmVHc
[beams]: https://www.youtube.com/watch?v=8lF_H1IqPiU
[magicleap]: http://www.magicleap.com
[deeplearning]:https://en.wikipedia.org/wiki/Deep_learning
[susa]:http://susaventures.com/
