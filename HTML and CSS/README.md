## HTML
- Relation between tags can be described by a DOM (Document Object Model).
- HTML helps to bring out the structure of the webpage.

- Brief Tags:
  - Hello World
  - Headings
  - Images
  - Links
  - Lists
  - Tables
  - Forms

- Divs allow us to break the page into different sections.

## CSS
- Tells the browser about the styling properties of the HTML webpage
- Styling can be done in several ways:
  - In-built style tag
  - Inside head: one style snippet for one HTML tag like h1
  - New file: can be reused for different pages also

- Important CSS attributes:
  - Size of elements
  - width
  - height
  - margin: around the div, outside the border
  - padding: around the element, inside the border
  - font: 

- , is a multiple selector

- We can idntify an element in HTML using 4 ways:
  - id (#name)
  - class (.name)
  - span
  - div
  
- In case of style clash between id and class, the following preference order based on specificity is used:
  - inline
  - id
  - class
  - type (eg. h1)

- More CSS selectors:
  - Descendants
  - Hover (this is awesome!)

### Responsive Design
- ViewPort: Specify visual settings based on devices
```html
<meta name = "viewport" content = "width=device-width, initial-scale=1.0">
```

- Media Queries
  - Type of browser/page may change the experiences
  - Eg. change properties depending on window width

- FlexBox
  - eg. Wrap around text in an excel cell (read mobile screen here.)

- Grid
  - responsive table
  
### Bootstrap
- Pre-written styling code on the internet
- eg. Alerts,table column model (with responsive version)

## SaSS
- extension of CSS to remove redundancy in code
- Variables is a key feature
- Needs a compiler to convert code to CSS
  - Has auto compile on change feature
- Allows nesting of CSS elements
- Allows inheritance also