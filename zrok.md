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

