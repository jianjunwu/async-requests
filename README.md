# async-requests

```
import async_requests
from async_requests import AsyncRequest
from async_requests.sessions import AsyncSession as Session
```

```
request1 = AsyncRequest(method="GET", url='http://www.baidu.com', session=Session(), timeout=0.001)
request2 = AsyncRequest(method="GET", url='http://www.baidu.com', session=Session())
```
```
results = async_requests.collect_async_results([request1, request2])
```
