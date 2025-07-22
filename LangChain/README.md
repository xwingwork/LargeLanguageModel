# LangChain (語言鏈)

LangChain vs LangGraph：<https://www.youtube.com/watch?v=qAF1NjEVHhY>

> `Lang`是`Language`縮寫

## LangChain 組成

固定順序流程，串成鏈的結構

* Retrieve (檢索)
  * Indexes (索引群)
    * Doc Loading
    * Vectgn DB
    * Text Sbutteng
* Summarize (摘要)
  * Prompt (提示)
  * LLM
* Answer (回答)
  * Memory (記憶)
    * Limited (有限的) State (狀態)
  * Prompt (提示)
  * LLM

<https://www.youtube.com/watch?v=1bUy-1hGZpI>

## LangGraph (語言圖)

複雜流程，不斷循環至 State (狀態) 結束

* Process (程序)
  * Taskcs (任務群)
    * Add
    * Complete (完成)
    * Summarize (摘要)
* State (狀態)
  * Memory (記憶) Robust (強韌)

### Graph概念架構

* Node (節點)
  * Process (程序) 中心模式
  * Taskcs (任務群)
    * Add
    * Complete (完成)
    * Summarize (摘要)
* Edge (邊緣)
  * Process (程序) 與 Taskcs (任務群) 溝通
    * Task.Add
    * Task.Complete (完成)
    * Task.Summarize (摘要)
* State (狀態)
  * 所有 Node (節點) 可存取

## 可再現性

* [x] 如何下載模型並安裝，讓服務可以引用
  > `LangChain`本質是充當 OpneAI 的隔離層，讓開發者可以專心開發應用，不用擔心與 OpenAI 的 OpenAPI 串接格式的問題，不會`下載模型並安裝`(拔網路線測試過)
