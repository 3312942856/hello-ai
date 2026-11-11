# hello-ai

我的第一个 AI 应用练习：用 Python 调用 DeepSeek 大模型 API。

## 功能
- 调用 DeepSeek Chat API，打印模型回答

## 运行方式
1. pip install openai
2. export DEEPSEEK_API_KEY="你的 API Key"
3. python hello.py

## 技术栈
- Python 3.11
- OpenAI Python SDK（DeepSeek API 兼容 OpenAI 格式）

## 说明
API Key 通过环境变量读取，不写入代码。
