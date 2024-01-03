# How to Use Zrok

1. Download `zrok` to specific platform.
2. RUn the following to try it out:
```bash
./zrok invite # register and get your zrok-token
./zrok enable zrok-token
./zrok status # See details in https://api.zrok.io/

# Close all servers holding the port 8080 before running the following command
./zrok share public # get help for sharing
./zrok share public --backend-mode web ./StaticFolder/ # sharing ./z-ChatSim/ to public as a static server

./zrok share private http://localhost:8080 # gain your ACCESS_TOKEN
./zrok access private ACCESS_TOKEN
# Output:: http://127.0.0.1:9191 -> ACCESS_TOKEN
# Access from browser:: https://ACCESS_TOKEN.share.zrok.io:9191/

```

# How to Use Ngrok

1. Download ngrok from [official site](https://ngrok.com/download).
2. Then run the command below:

    ```bash
    sudo tar xvzf ~/Downloads/ngrok-v3-stable-linux-amd64.tgz -C /usr/local/bin
    ```

3. Login to official [auth-token site](https://dashboard.ngrok.com/get-started/your-authtoken) to get your token.
4. Configure ngrok:

    ```bash
    ngrok authtoken YOUR_TOKEN
    ```

5. Open localhost as a static HTTP server:
    
    ```bash
    ngrok http 8080
    # Or
    ngrok http 8080 --log=stdout
    # Or
    ngrok http 8080 --log=stdout > ngrok.log &
    # Output: the URL accessible publically created 
    ```

6. On another terminal:
   ```bash
    servez
    # Output: 127.0.0.1:8080
   ```

7. On browser, copy the created URL and visit the site.


8. Open tcp so as to connect remotely to this computer via SSH:
    
    ```bash
    ngrok tcp 22
    # Or
    ngrok tcp 22 --log=stdout
    # Or
    ngrok tcp 22 --log=stdout > ngrok.log &
    # Result:                                                                                                                                                                                                                  
    # Introducing Pay-as-you-go pricing: https://ngrok.com/r/payg                                                                                                                                                        
    # Session Status                online                                                                                                                                                                               
    # Account                       ACCOUNT_NAME (Plan: Free)                                                                                                                                                                   
    # Version                       3.5.0                                                                                                                                                                                
    # Region                        Asia Pacific (ap)                                                                                                                                                                    
    # Latency                       41ms                                                                                                                                                                                 
    # Web Interface                 http://127.0.0.1:4040                                                                                                                                                                
    # Forwarding                    tcp://address_gain:port_gain -> localhost:22  # Copy your address from this line!!! (Note that the port will change dynamically on each run) 
    # Connections                   ttl     opn     rt1     rt5     p50     p90                                                                                                                                          
    #                              2       0       0.01    0.01    35.41   57.66     
    ```

9. On a remote computer:

    ```bash
    ssh username@address_gain_from_out_put_above -p port_gain_from_output_above
    ```


# How to Use `localhost.run`

1. Run the following command to publicize your localhost on a ssh-installed machine:
    ```bash
    ssh -R 80:localhost:8080 localhost.run
    ```


# How to Use `localtunnel`

1. Run the following command to install and run:
    ```bash
    npm install -g localtunnel
    lt --port 8080
    # Output: a publically accessible URL
    # On another terminal
    servez
    # Visit the publically accessible URL then fill in the IP address to the page to configure its accessiblity, then everyone can access that page via the URL
    ```    
