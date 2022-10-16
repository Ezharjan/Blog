local function commander(argToExcute)
    local result = io.popen(argToExcute)
    local strInfo = result:read("*all")
    return strInfo
end

function tryTillSucceed(arg, tryTimes)
    tryTimes = tryTimes or 1000
    for i = 1, tryTimes, 1 do
        print("argument is: ", arg)
        local res = commander(arg)
        if res ~= "" then
            print("Conduction succeeded!")
            break
        end
    end
end

local cmds = {
    "hexo g",
    "hexo d",
    "git add .",
    'git commit -m "auto"',
    "git push -u origin master",
    "git pull"
}

-- local pushMaster2github = "git push -u origin master"
for i = 1, #cmds, 1 do
    print(("running `%s`"):format(cmds[i]))
    commander(cmds[i])
end
-- tryTillSucceed(pushMaster2github)
