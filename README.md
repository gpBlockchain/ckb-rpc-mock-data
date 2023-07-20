### CKB RPC Mock Data

#### JS Adapter Demo
- The function `setupMockRpcTest` is used for initializing mock data.
  - It fetches the RPC mock data based on the `describe` name, such as `get_tip_block_number`, and the test name, such as `[]`.

- When adding new test cases, you only need to focus on the RPC you want to call.
```shell
describe('get_tip_block_number', function () {
    let mockData = setupMockRpcTest();
    test('[]', async () => {
        let { RPCClient, requestData, responseData } = mockData();
        let number = await RPCClient.getTipBlockNumber();
        expect(number).toEqual(responseData["result"]);
        expect(axios).toBeCalledWith(getRequestCall(requestData));
    });
});
```
