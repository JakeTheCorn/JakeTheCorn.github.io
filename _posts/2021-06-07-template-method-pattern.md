---
layout: post
title:  "Design Patterns - Template Method - Ruby"
date:   2021-06-07 09:00:00 -0400
categories: jekyll update
---

# Design Patterns: Template Method

I was recently installing a couple of storm doors on the house we live in.  The door was not sold with
a handle, you have to buy the handle separately which is nice because it allows one to choose from
a few different styles and finishes. On top of that, the doors were not sold as either "left-hand" or
"right-hand"... meaning that if you would actually like a functioning door, you have to drill a hole
for the handle on one side of the door or the other, and place the hinge on one side or the other.

Pretty versatile door setup.  We're pretty happy with both doors.

The directions were very well written.  Most of the steps for assembling and attaching the door to its frame
fit on one page. There was a separate page included that on one side had the specific directions for a
"left-open" door and on the other side had directions for a "right-open" door.

The main directions page was too abstract to install the door.  But it did contain all of the same shared steps which meant
that the company did not have to print redundant directions for both installations.

## How does that relate to the template method pattern?

The Template method pattern is any time when a "Fill in the blanks" kind of solution can take place.

Meaning that essentially a generic algorithm gets defined in a parent class where most of the steps are sort of worked
out.  But then child classes "Fill in the blanks" in a way that is important for them.

Most of the steps are defined in the parent, but then children can change parts as needed.

This is especially useful for design time deviations in the algorithm.

To illustrate this example, some ruby code...

This may not be the ***best*** example, however, I write in my off time and hopefully can be forgiven the contrived example, any structural concerns, or lack of tests..

{% highlight ruby %}
class TableRenderer
  def initialize(items:)
    @items = items || []
  end

  def render
    body = ''
    header = ''

    @items.each_with_index do |item, index|
      if index == 0
        header = build_header(item: item)
      end
      body += build_row(item: item)
    end
    body = "<tbody>#{body}</tbody>"
    "<table>#{header}#{body}</table>"
  end

  protected
    def build_row(item:)
      cells = []
      item.each do |key, value|
        cells << build_cell(key: key, value: value)
      end
      build_row_contents(cells: cells)
    end

    def build_header(item:)
      header_output = ''
      item.each do |key, _value|
        header_output += build_header_cell(key: key)
      end
      %{<thead>#{header_output}</thead>}
    end

    def build_header_cell(key:)
      "<th>#{key}</th>"
    end

    def build_cell(key:, value:)
      "<td>#{value}</td>"
    end

    def build_row_contents(cells:)
      output = ''

      for cell in cells do
        output += cell
      end
      "<tr>#{output}</tr>"
    end
end

class EmployeesTableRenderer < TableRenderer
  protected
    def build_header_cell(key:)
      "<th>#{key.upcase}</th>"
    end
end

class QuartersTableRenderer < TableRenderer
  protected
    def build_cell(key:, value:)
      if key != "year"
        return super
      end
      %{<td><a href="https://en.wikipedia.org/wiki/#{value}">#{value}</a></td>}
    end

    def build_header_cell(key:)
      %{<th style="color: green;">#{key}</th>}
    end
end


employees = [
  { "name" => 'bob', "age" => 45 },
]

quarters = [
  { "year" => "2012", "q1" => 13000, "q2" => 1000, "q3" => 2000, "q4" => 2000, },
  { "year" => "2013", "q1" => 13000, "q2" => 1000, "q3" => 2000, "q4" => 2000, },
]

html =
%{<html>
  <head>
  </head>
  <body>
      #{EmployeesTableRenderer.new(items: employees).render}
      #{QuartersTableRenderer.new(items: quarters).render}
  </body>
</html>
}

File.write('index.html', html)

{% endhighlight %}

then run the file

{% highlight bash %}
ruby main.rb
{% endhighlight %}

This should generate an index.html

Open it in your favorite browser

You should see something like this...

<table><thead><th>NAME</th><th>AGE</th></thead><tbody><tr><td>bob</td><td>45</td></tr></tbody></table>
<table><thead><th style="color: green;">year</th><th style="color: green;">q1</th><th style="color: green;">q2</th><th style="color: green;">q3</th><th style="color: green;">q4</th></thead><tbody><tr><td><a href="https://en.wikipedia.org/wiki/2012">2012</a></td><td>13000</td><td>1000</td><td>2000</td><td>2000</td></tr><tr><td><a href="https://en.wikipedia.org/wiki/2013">2013</a></td><td>13000</td><td>1000</td><td>2000</td><td>2000</td></tr></tbody></table>


