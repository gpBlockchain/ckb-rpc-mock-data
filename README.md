### ckb rpc mock data 


#### js 适配 demo
- setupMockRpcTest为: 初始化mock数据
  - 会根据describe的名字`get_tip_block_number`和test 的名字`[]` 找到该rpc mock 数据

- 新增的测试用例,只需要关注要调用的rpc就可以了
```shell
describe('get_tip_block_number', function () {
    let mockData = setupMockRpcTest();
    test('[]', async () => {
       test('[]', async () => {
        let {RPCClient,requestData,responseData }= mockData()
        let number = await RPCClient.getTipBlockNumber()
        expect(number).toEqual(responseData["result"]);
        expect(axios).toBeCalledWith(getRequestCall(requestData))
    })
});


```