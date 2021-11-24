FROM jekyll/jekyll:3.8
COPY Gemfile .
COPY Gemfile.lock .
RUN bundle install
EXPOSE 4000
CMD ["bundle", "exec", "jekyll", "serve", "--port=4000", "--host=0.0.0.0"]
