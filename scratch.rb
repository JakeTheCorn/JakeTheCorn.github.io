# todo
#   code cleanup
#   tests?
# build vs render?

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
        cells << render_cell(key: key, value: value)
      end
      build_row_contents(cells: cells)
    end

    def build_header(item:)
      header_output = ''
      item.each do |key, _value|
        header_output += render_header_cell(key: key)
      end
      %{<thead>#{header_output}</thead>}
    end

    def render_header_cell(key:)
      "<th>#{key}</th>"
    end

    def render_cell(key:, value:)
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
  # get_column_mapping?
end

class QuartersTableRenderer < TableRenderer
  protected
    def render_cell(key:, value:)
      if key != "year"
        return super
      end
      %{<td><a href="https://en.wikipedia.org/wiki/#{value}">#{value}</a></td>}
    end

    def render_header_cell(key:)
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

File.write('derp.html', html)
