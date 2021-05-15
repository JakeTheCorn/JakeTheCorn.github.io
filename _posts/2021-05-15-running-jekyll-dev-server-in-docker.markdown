---
layout: post
title:  "Docker -- Running jekyll sev server in docker"
date:   2021-05-15 09:00:00 -0400
categories: jekyll update
---
This is a helpful to run Jekyll projects in a dockerized dev server so that the host does not have to install all the ruby deps.

First write a small dockerfile like this...

```
FROM jekyll/jekyll:3.8
COPY Gemfile .
RUN bundle install
EXPOSE 4000
CMD ["bundle", "exec", "jekyll", "serve", "--port=4000", "--host=0.0.0.0"]
```

NOTE: you must pass the 0.0.0.0 to the jekyll serve command because other wise docker won't pick it up when port mapping

build it...

{% highlight bash %}
docker build . --tag jekyll-dev
{% endhighlight %}

Then run it...

{% highlight bash %}
docker run -it --rm --publish="4000:4000" --volume="$(pwd)":/srv/jekyll jekyll-dev
{% endhighlight %}

make a change and you should see a "live reload"


-- jake
