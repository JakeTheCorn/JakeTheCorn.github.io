---
layout: post
title:  "Dockerize rails app on alpine"
date:   2021-05-28 09:00:00 -0400
categories: jekyll update
---

Dockerfile...

{% highlight docker %}
FROM ruby:3.0.1-alpine3.13
RUN mkdir /app
WORKDIR /app

RUN apk update && \
    apk add --update \
        make \
        gcc \
        libc-dev \
        sqlite-dev \
        g++ \
        tzdata \
        nodejs \
        yarn

RUN gem install rails

COPY Gemfile .

RUN bundle install

COPY . .

EXPOSE 3000

CMD [ "rails", "server", "--binding", "0.0.0.0"]

{% endhighlight %}

To build...

{% highlight bash %}
docker build --tag='rails_app' .
{% endhighlight %}

Running ...

{% highlight bash %}
docker run \
    -it \
    --volume="${ROOT_DIR}":/app \
    --rm \
    --workdir=/app \
	--publish="3000:3000" \
    rails_app;
{% endhighlight %}


set up may change if using postgres or other database, but this should be a good starting block

