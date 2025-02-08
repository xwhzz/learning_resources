import os
from jinja2 import Environment, FileSystemLoader

# Path to the directory containing the templates
template_dir = './templates'
output_dir = './slides'

# List of all notebooks
notebooks = []
for notebook in os.listdir('./notebooks'):
    if notebook.endswith('.ipynb'):
        # Create the corresponding slide file name
        slide_name = notebook.replace('.ipynb', '.slides.html')
        notebooks.append({'name': notebook.replace('.ipynb', ''), 'url': f'./{slide_name}'})

# Set up the Jinja2 environment and load the template
env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template('index_template.html')

# Render the template with the notebook list
output = template.render(notebooks=notebooks)

# Write the final index.html to the slides directory
with open(os.path.join(output_dir, 'index.html'), 'w') as f:
    f.write(output)

print("index.html has been generated!")