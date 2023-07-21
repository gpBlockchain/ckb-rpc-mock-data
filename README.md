### CKB RPC Mock Data

#### start 
```shell
pip install -r requirements.txt
python api/index.py
```

### api

#### get test
click link  http://localhost:5000/

#### test

- get 
  - get test message 
- post 
  - mock ckb rpc ,will check request ,if request == request.json ,return response.json 

#### JS Adapter Demo
- When adding new test cases, you only need to focus on the RPC you want to call.
```shell
 it("[tx]",async ()=>{
        let data = request("http://127.0.0.1:5000/test/estimate_cycles/[tx]")
        let requestData = data['request']
        let responseData = data['response'] 
        let RPCClient = new RPC("http://127.0.0.1:5000/test/estimate_cycles/[tx]");
        let tx = toTransaction(requestData["params"][0])
        // @ts-ignore
        let response = await RPCClient.estimateCycles(tx)
        expect(response.cycles).toEqual(responseData["result"]["cycles"])
})

```
