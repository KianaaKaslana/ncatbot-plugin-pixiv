# 将您的 Pixiv 插件发布到 GitHub 的步骤

## 1. 在 GitHub 上创建新仓库
- 登录 GitHub
- 点击 "New repository" 按钮
- 输入仓库名称（如 "ncatbot-pixiv-plugin"）
- 添加描述（可选）
- 选择 "Public" 或 "Private"
- 不要勾选 "Initialize this repository with a README"（因为我们已经有了）
- 点击 "Create repository"

## 2. 在本地初始化 Git 仓库并连接到 GitHub
打开命令行工具，然后执行以下命令：

```bash
cd E:\github\cangku\plugins\pixiv

# 初始化 Git 仓库
git init

# 添加所有文件到暂存区
git add .

# 提交更改
git commit -m "Initial commit: Pixiv plugin for NcatBot"

# 添加远程仓库地址（替换为您在 GitHub 上创建的仓库地址）
git remote add origin https://github.com/您的用户名/ncatbot-pixiv-plugin.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

## 3. 重要提醒
- 请确保您的 `plugin.py` 文件中的 `refresh_token` 不要泄露到公共仓库中
- 如果您使用的是公共仓库，建议将敏感配置信息移到单独的配置文件中并添加到 .gitignore
- 请更新 setup.py 和 README.md 中的仓库 URL 为您实际的 GitHub 仓库地址