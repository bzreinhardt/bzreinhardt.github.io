---
<!--layout: default -->
title: Home
layout: default
---

## "Specialization is for insects" 
-- Robert A. Heinlein
<br>
<br>
I want to make us Smarter, Faster, Stronger, Higher. Currently, I'm a PhD student working on [tractor][tractor] [beams][beams] for space robotics at [Cornell][lab]. I've, been a plumber, an archer, a waiter, a nazgul, and an oregano salesman. I'm  one of the few people in the world with a Bachelor of Science in History. 
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
