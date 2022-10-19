how-to :: Dynamic pages with form inputs and Jinja2
---
## Overview
We learned how to parse form submissions in class, and how to use Jinja to dynamically affect content in our HTML. 
In this how-to, we will combine these two concepts to create a dynamic page whose content is affected by user input.

### Estimated Time Cost: 0.4 hours

### Prerequisites:

- Python understanding, Jinja and Flask experience
- Knowledge of the request object, where to find it, and how to use it

1. Prepare your flask app boilerplate code.
2. Create a form with an input field (`name="your_arg_name_here"`) and a submit button (`type="submit"`)
3. Create a route that handles the form submission. This route should have a `methods=["POST"]` argument.
4. Using that route name, in your HTML, set the `action` attribute of your form to that route name.
5. In your route, use `request.args.get("your_arg_name_here")` to get the value of the input field.
6. Use that value in your Jinja template to dynamically affect the content of your page.
7. Profit**!** (or at least, see your page change)

### Resources
* [Python Docs](https://docs.python.org/3/tutorial/modules.html)
* [MoAR MODULES](https://pypi.org/)
* [Demo Code]

---

Accurate as of (last update): 2022-10-07

#### Contributors:  
William Vongphanith, pd2  
Elizabeth Paperno, pd2  
Konstantin Dubovskiy, pd2  