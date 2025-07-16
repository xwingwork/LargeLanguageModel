<https://pypi.org/project/fastapi/0.115.14/>

<https://python.langchain.com/docs/troubleshooting/errors/MESSAGE_COERCION_FAILURE>

學習中 4:33 左右
<https://www.youtube.com/watch?v=KC8HT0eWSGk&t=383s>

FastAPI.OpenAPI：<http://localhost:9001/docs>

```bash
python
from api.ai.assistants import *

email_assistant("show me my latest email")
email_assistant("Send me an email about needing more coffee")

```

```bash
python

from api.ai.agent import *
agent = get_email_agent()
agent.invoke({"message":"what are my recent emails?"})
# TODO 為什麼不是讀郵件?，有密碼了
```

```bash
python

from api.ai.agent import *
supe = get_supervisor()
supe.invoke({"message":[{"role":"user","content":"Find out how to create a late then mail me the results."}]})

```
<!-- TODO 郵件系統無法登入，改用其他案例 -->