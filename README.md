# 说明

**CS61A** 是我在学习Python的过程中遇见的非常优秀的课程，由Berkeley提供。帮助我理清和练习了许多如递归，树之类的较难理解的计算机概念。这个库里记录了我习题和项目的答案，还有我在学习过程中遇到的困难。

## 时间线

2023年7月 - 首次开始这个课程的学习，（2020 Summer）
2024年3月 - 2024年10月 因为大学课程繁忙而暂停
2024年10月 - 当重新开始时，发现Berkeley将曾经的2020 Summer课程收入了内部域名，需要伯克利账号才可以访问了。可公开访问了变成了目前的官网：https://cs61a.org/ ，课程为2024 Fall。也罢，课程的内容都是相仿的，我就从 2024 Fall 的 Homework 4 开始，希望能在这个学期完成这个课程。

## 待解决的问题

1. In HW04, the last question Par Diff. What is it all about?

## 遭遇问题的记录

在CS61A的学习中，我也遇到了一些技术问题。在这里记录一下解答。

### VSCODE貌似不会同步VIM插件的配置，而我喜欢jk进入normal模式

需要在settings.json里添加：
"vim.insertModeKeyBindings": [
        {
            "before": ["j", "k"],
            "after": ["<Esc>"]
        }
    ],

### 通过Https协议Push到GitHub经常失败

方法一：可以切换到SSH协议：

1. 在自己的电脑上通过Terminal ssh-key gen生成一个SSH-key。参考[这篇文章](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agenthttps://blog.csdn.net/weixin_42310154/article/details/118340458)。

1. 登陆自己的Github填入刚刚生成的SSH-key

1. 修改仓库的push，fetch地址为SSH协议

    查看当前远程仓库地址：git remote -v  
    修改远程仓库地址：git remote set-url origin git@{...}  
    (用git@取代原先地址中的http(s)://)  

方法二：可以关闭代理（成功率不高），在命令行中键入：  

1. git config --global --unset http.proxy  
2. git:(main) git config --global --unset https.proxy
