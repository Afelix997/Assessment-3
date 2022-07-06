# Assessment 3: HTML/CSS/JS and Django
- **E-commerce Business**

## Important Grading Information
- Make sure you read the [Assessment-3 Grading Rubric](https://docs.google.com/spreadsheets/d/1-YjVU8Wt7qgW8yOImASqB2uYiLBu93dVJuLYjUlEIgk/edit?usp=sharing).

- You need to get a 75% or better to pass. (You must pass all assessments in order to graduate Code Platoon's program.)
- If you fail the assessment, you have can retake it once to improve your score. For this assessment... 
  - *5% penalty*: If you complete and submit the retake **within one week** of receiving your grade.
  - *10% penalty*: If you complete and submit the retake after one week of receiving your grade.

## Rules / Process
- This test is fully open notes and open Google, but is not to be completed with the help of any other student/individual.
- Do not open a pull request against this repository. We will evaluate your code individually with you.

## Requirements

Build an e-commerce website. Your website should be a Django application that renders HTML templates, using CSS/Bootstrap. This website should feature multiple pages, which should include:
- **Home page** (index.html)
  - This page should show just a basic intro and other common basic home page content
  - Include appropriate site navigation between all pages

- **Category pages**
  - There should be a separate page for each of the various product categories (e.g. "Home", "Kitchen", "Bed & Bath", "Office", etc...)
  - These pages should show at least 3 featured items per category, with images, names, and prices. This data should come from a list of dictionaries in the Django server (i.e. don't hardcode them into your HTML pages, instead pass them into your templates as a dictionary of data).
  - These pages should allow users to add products to their virtual shopping cart. The shopping cart should be persisted in-memory using a list of dictionaries, which are read and written using Django. 
- **Shopping Cart page**
  - This page should show all of the items that were added to the user's shopping cart. Users should be able to see quantities for each item, subtotals for each item, and a total price for the entire order. 
- **Search page**
  - This page should allow a user to search for a specific product by name. If the product does not exist in your store, tell the user that it is out of stock, and use [the noun project API](https://api.thenounproject.com/) to display a picture of that item. 

Additionally, your site should:
  - Include some basic styling using CSS
  - Use the bootstrap navbar, and at least one of the following Bootstrap components: carousel, collapse, dropdowns, or modal.
  - Avoid repeating HTML across your different pages by using `{% include partial.html %}` and `{% extends layout.html %}`. There should only be one `<html>` tag in your whole project!

