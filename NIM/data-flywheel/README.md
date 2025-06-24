# 資料飛輪

`data-flywheel`將模型`Distillation (蒸餾)`優化

<https://build.nvidia.com/nvidia/build-an-enterprise-data-flywheel/blueprintcard>

## 步驟

1. 取得NIM
2. 找群本地部屬資源<https://github.com/NVIDIA-AI-Blueprints/data-flywheel>
3. 將部屬所需的資源進行清理，排除多於檔案
4. 申請 NVIDIA AI 平台的帳號
5. 申請 API Keys (AI Token)<https://org.ngc.nvidia.com/setup/api-keys>
6. 將 API Key 設定到 Docker 的環境參數`NGC_API_KEY`(部分步驟會要求環境參數`oauthtoken`也是 API Key)，下載 image 時要用此通過認證
