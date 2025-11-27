import os
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import aiosmtplib
from nonebot import logger
from src.configs.api_config import google_smtp_server, google_email, google_password
from src.configs.api_config import qq_smtp_server,qq_email,qq_password
from src.configs.api_config import server_smtp_server,server_email,server_password, server_port

# 发送内容
html = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>健康小贴士</title>
    <style>
        body {
            font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            color: #333;
            line-height: 1.6;
        }

        .container {
            background-color: white;
            border-radius: 12px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            padding: 30px;
            max-width: 500px;
            width: 90%;
            text-align: center;
            transition: transform 0.3s ease;
        }

        .container:hover {
            transform: translateY(-5px);
        }

        h1 {
            color: #ff6b6b;
            font-size: 2.2rem;
            margin-bottom: 20px;
            position: relative;
            display: inline-block;
        }

        h1:after {
            content: "";
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 60px;
            height: 3px;
            background: linear-gradient(90deg, #ff6b6b, #ff8e8e);
            border-radius: 3px;
        }

        p {
            font-size: 1.1rem;
            margin: 25px 0;
            padding: 0 10px;
        }

        .emoji {
            font-size: 1.5rem;
            vertical-align: middle;
            margin: 0 3px;
        }

        .tip-box {
            background-color: #f8f9fa;
            border-left: 4px solid #74b9ff;
            padding: 15px;
            margin: 20px 0;
            text-align: left;
            border-radius: 0 8px 8px 0;
        }

        .footer {
            margin-top: 30px;
            font-size: 0.9rem;
            color: #777;
        }

        @media (max-width: 480px) {
            h1 {
                font-size: 1.8rem;
            }
            p {
                font-size: 1rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>可别<span class="emoji">🦌</span>死了</h1>
        <p>作案前记得洗手，适度使用手动挡，别让发动机过热抛锚。</p>

        <div class="tip-box">
            <strong>健康小贴士：</strong> 适度有益健康，过度可能影响日常生活。保持良好卫生习惯，合理安排时间哦~
        </div>
    </div>
</body>
</html>
    """
async def send_email_by_google(receiver_email: str, file_path: str):
    """发送单个文件附件邮件（Google版）"""
    msg = MIMEMultipart()
    msg["From"] = google_email
    msg["To"] = receiver_email
    msg["Subject"] = "您的快递已送达"
    msg.attach(MIMEText(html, "html", "utf-8"))

    try:
        # 验证文件存在性
        if not os.path.isfile(file_path):
            logger.error(f"文件不存在：{file_path}")
            return False

        # 添加单个文件附件
        file_name = os.path.basename(file_path)
        with open(file_path, "rb") as f:
            attachment = MIMEApplication(f.read())
            attachment.add_header(
                "Content-Disposition",
                "attachment",
                filename=file_name
            )
            msg.attach(attachment)

        async with aiosmtplib.SMTP(
                hostname=google_smtp_server,
                port=465,
                timeout=60,
                use_tls=True
        ) as server:
            await server.login(google_email, google_password)
            await server.send_message(msg)
            return True

    except Exception as e:
        logger.error(f"邮件发送失败：{e}")
        return False

async def send_email_by_qq(receiver_email: str, file_path: str):
    """发送单个文件附件邮件（QQ版）"""
    msg = MIMEMultipart()
    msg["From"] = qq_email
    msg["To"] = receiver_email
    msg["Subject"] = "您的快递已送达"
    msg.attach(MIMEText(html, "html", "utf-8"))

    try:
        if not os.path.exists(file_path):
            logger.error(f"文件不存在：{file_path}")
            return False

        # 添加附件
        file_name = os.path.basename(file_path)
        with open(file_path, "rb") as f:
            attachment = MIMEApplication(f.read())
            attachment.add_header(
                "Content-Disposition",
                "attachment",
                filename=file_name
            )
            msg.attach(attachment)

        async with aiosmtplib.SMTP(
                hostname=qq_smtp_server,
                port=465,
                use_tls=True,
                timeout=30
        ) as server:
            await server.login(qq_email, qq_password)
            await server.send_message(msg)
            print("QQ文件邮件发送成功！")
            return True
    except Exception as e:
        logger.error(f"QQ邮件发送失败：{e}")
        return False

async def send_email_by_server(receiver_email: str, file_path: str):
    """发送单个文件附件邮件（自建服务器版）"""
    msg = MIMEMultipart()
    msg["From"] = server_email
    msg["To"] = receiver_email
    msg["Subject"] = "您的快递已送达"
    msg.attach(MIMEText(html, "html", "utf-8"))

    try:
        if not os.path.exists(file_path):
            logger.error(f"文件不存在：{file_path}")
            return False

        # 添加附件
        file_name = os.path.basename(file_path)
        with open(file_path, "rb") as f:
            attachment = MIMEApplication(f.read())
            attachment.add_header(
                "Content-Disposition",
                "attachment",
                filename=file_name
            )
            msg.attach(attachment)

        async with aiosmtplib.SMTP(
                hostname=server_smtp_server,
                port=server_port,
                start_tls=True,
                timeout=120
        ) as server:
            await server.login(server_email, server_password)
            await server.send_message(msg)
            print("自建服务器文件邮件发送成功！")
            return True
    except Exception as e:
        logger.error(f"自建服务器邮件发送失败：{e}")
        return False