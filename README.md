# BookBot v1.0 #
  You can look email multiple files to a single email to a single person, after which the entire directory will be wiped clean. Use this for your `Kindle` or anything.

## Dependencies ##
- `yagmail` --> sending the emails
- `os` --> directory access and listing
- `shutil` --> purging the directory afterwords
  ### Dependency Installation ###
  - Within a set virtual env ([venv](https://docs.python.org/3/library/venv.html)), pip install those dependencies
  - Be sure to have the venv running while executing this code
    * Though if you clone this repo, you can just navigate to that folder and run...
      ```
      source BookBot/bin/activate
      ```
      ...and you can use the venv that I have created. 
## Pre-Usage ##
1. Clone this repository
```
 https://github.com/patelpratham11/BookBot.git
 ```

2. Make sure your gmail account is set to allow for un-safe applications to access it
  1. This is in order to make sure that this client can access your email and send the emails
  2. You can access that site and turn it on [here](https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4O58MFMjNVIKVEKaC111KA9L7cS9HSwvjSQY2cWjhFXBpv1nPrm99gWIG7A9jL7cpQp5I7SGoQNxDSNFRelflBjGluXDA)
3. Make sure to change the 'folder' variable to where ever you want the 'Books' directory to be made/ where you want to place the books to be emailed to you
4. Make sure current dependencies are installed with the latest updates
5. Execute the code by making sure you're running from the directory and running
  ```
  python3 Book.py
  ```

## Usage Instructions ##
1. Make sure you have followed the pre-usage Instructions
2. Place whatever files you would like to email in the folder
3. Run the program from the command line, making sure you're following all Instructions
4. Put your email, password, and receiving email down
5. Everything should send in a single email and clear the directory

## Development ##
- This project was developed by Pratham Patel (patelpratham11) starting December 25, 2021
- All bugs and other comments can be submitted through GitHub
