
# Database AI Helper

## 📋 **專案概述**
`Database AI Helper` 是一個基於 Python 和資料庫操作的工具集，旨在輔助數據的插入、查詢、訓練和展示，並集成了 OpenAI API 進行 AI 功能擴展。

---

## 🗂 **專案目錄結構**
```plaintext
Database_AI_Helper/
│
├── __pycache__/                 # 編譯後的 Python 快取檔案
│   ├── Chatgpt_api.cpython-312.pyc
│   └── Getdata.cpython-312.pyc
│
├── Chat_gpt_test.py             # OpenAI API 測試腳本
├── Chatgpt_api.py               # 與 OpenAI API 連接的主腳本
├── Database_insert.py           # 資料庫插入功能
├── Database_search.py           # 資料庫搜尋功能
├── Database_search2.py          # 加強版資料庫搜尋腳本
├── Getdata.py                   # 從資料庫中提取數據
├── backend.py                   # 後端邏輯處理
│
├── test.html                    # 測試用的 HTML 文件
├── test1.html                   # 第二個測試用 HTML 文件
│
├── train_data.jsonl             # 訓練數據文件 (JSONL 格式)
├── train_data.jsonl2            # 訓練數據文件 2 (JSONL 格式)
├── train_data2.jsonl            # 訓練數據文件 3 (JSONL 格式)
├── training_data.jsonl.txt      # 訓練數據的文本備份
│
└── 博物館資料庫小工具對話實例.docx  # 文檔：博物館資料庫 AI 對話實例
```

---

## 🚀 **功能介紹**
### **1. ChatGPT API 連接**
- **檔案**：`Chatgpt_api.py`, `Chat_gpt_test.py`
- **功能**：利用 OpenAI API 提供自然語言生成，支援各種 AI 對話與測試功能。

### **2. 資料庫操作工具**
- **檔案**：`Database_insert.py`, `Database_search.py`, `Database_search2.py`
- **功能**：
    - **插入數據**：將數據存入資料庫。
    - **搜索數據**：高效搜尋並提取數據，支援增強版搜尋功能。

### **3. 資料提取與後端邏輯**
- **檔案**：`Getdata.py`, `backend.py`
- **功能**：
    - 提取資料庫中的數據進行後續處理。
    - 提供後端邏輯支撐前端或其他功能模組。

### **4. 訓練數據文件**
- **檔案**：`train_data.jsonl`, `train_data.jsonl2`, `train_data2.jsonl`
- **功能**：
    - 訓練數據存儲於 JSONL 格式，支援大規模 AI 模型訓練和測試。

---

## 📌 **使用說明**
1. **設置 API Key**  
   在 `Chatgpt_api.py` 或 `Chat_gpt_test.py` 中設置 OpenAI API 金鑰。

2. **運行資料庫腳本**  
   使用以下指令運行資料庫操作腳本：  
   ```bash
   python Database_insert.py
   python Database_search.py
   ```

3. **測試 HTML 檔案**  
   使用瀏覽器打開 `test.html` 或 `test1.html` 進行測試。

4. **數據訓練**  
   確保 `train_data.jsonl` 文件存在，然後運行相關的模型訓練腳本。

---

## 🛠 **技術細節**
- **後端語言**：Python
- **API 集成**：OpenAI API
- **數據格式**：JSONL
- **前端測試**：HTML 文件
- **文檔**：包含博物館資料庫對話實例

---

## 🔗 **版本控制**
- **Git 分支**：`main`
- **初次提交**：`first_test`

---

## ⚠️ **注意事項**
- **API Key 保密**：請勿將 OpenAI API Key 泄露至公有倉庫。
- **JSONL 數據格式**：訓練數據文件應符合 JSONL 規範。

---

## 📝 **版本日誌**
### v1.0.0
- 初始版本：新增核心功能模組和訓練數據文件。

---

## 🤝 **貢獻者**
- **作者**：Zhu-astor  
- **GitHub**：[Zhu-astor/Database_AI_Helper](https://github.com/Zhu-astor/Database_AI_Helper)

---

## 📄 **授權**
本專案採用 MIT 授權。
