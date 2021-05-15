FROM jekyll/jekyll:3.8
COPY Gemfile .
RUN bundle install
EXPOSE 4000
CMD ["bundle", "exec", "jekyll", "serve", "--port=4000", "--host=0.0.0.0"]
