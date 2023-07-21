### CKB RPC Mock Data

#### start 
```shell
pip install flask
python -m app
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
- The function `setupMockRpcTest` is used for initializing mock data.
  - It fetches the RPC mock data based on the `describe` name, such as `get_tip_block_number`, and the test name, such as `[]`.

- When adding new test cases, you only need to focus on the RPC you want to call.
```shell
 it("[tx]", async () => {
        let {RPCClient, requestData, responseData} = await mock_rpc()
        let tx = toTransaction(requestData["params"][0])
        // @ts-ignore
        let response = await RPCClient.estimateCycles(tx)
        expect(response.cycles).toEqual(responseData["result"]["cycles"])
    })

export async function mock_rpc(){
    let data = get_method_and_params(expect.getState().currentTestName)
    return get_mock_test_data(data.method,data.params)
}
async function get_mock_test_data(method: string, params: string) {

    let data = await get(`http://127.0.0.1:5000/test/${method}/${params}`)
    let requestData = data['request']
    let responseData = data['response']
    let RPCClient = new RPC(`http://127.0.0.1:5000/test/${method}/${params}`);
    return {RPCClient,requestData, responseData}

}

function get_method_and_params(currentTestName: string): { method: string, params: string } {
    let [name, params] = splitFirstSpace(currentTestName)
    return {
        method: name, params: params
    }
}
```
