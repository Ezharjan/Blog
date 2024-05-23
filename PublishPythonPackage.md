
### Tips: How to Publish a Python Package?

1. Register your account on its [official website](https://pypi.org);
2. Get your API token for uploading your package online from the [website](https://pypi.org);
3. Add a file named `.pypirc` inside your directory of `C:\Users\your_user_name`;
4. Add the following content to your `.pypirc` file created:
   ```
    [pypi]
    repository = https://upload.pypi.org/legacy/
    username = your_user_name
    password = YOUR_API_TOKEN
   ```
5. Make sure you have the correct `setup.py` file.
6. `pip install twine`
7. `python setup.py sdist`
8. `twine upload dist/*`
