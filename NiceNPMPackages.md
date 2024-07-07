# Nice NPM Global Packages

1. servez
    ```bash
    npm install -g servez
    servez
    servez -p 80
    # print out the QR code of the page
    servez -p 80 --qr
    # set the password to the webpage
    servez -p 80 --qr --username YOUR_NAME --password YOUR_PASSWORD
    # for more information
    servez -h
    ```

2. markserv
    ```bash
    npm install -g markserv
    markserv
    # change default port to 80
    markserv -p 80
    # to make it externally available
    markserv -p 8642 -a 0.0.0.0
    ```

