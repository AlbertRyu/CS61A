# 背景
在CS61A的学习中，我也遇到了一些技术问题。在这里记录一下解答。

# VSCODE貌似不会同步VIM插件的配置，而我喜欢jk进入normal模式

需要在settings.json里添加：
"vim.insertModeKeyBindings": [
        {
            "before": ["j", "k"],
            "after": ["<Esc>"]
        }
    ],

# 通过Https协议Push到GitHub经常失败

可以切换到SSH协议：
1. 在自己的电脑上通过Terminal ssh-key gen生成一个SSH-key
参考：https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
https://blog.csdn.net/weixin_42310154/article/details/118340458
2. 登陆自己的Github填入刚刚生成的SSH-key
3. 修改仓库的push，fetch地址为SSH协议
    查看当前远程仓库地址：git remote -v
    修改远程仓库地址：git remote set-url origin git@{...}
    (用git@取代原先地址中的http(s)://)

可以关闭代理（成功率不高）
在命令行中键入：
git config --global --unset http.proxy
git:(main) git config --global --unset https.proxy