# 定义校验契约类,定义每个接口的预期格式
from pactverify.matchers import Matcher, Like, EachLike, Term, Enum, PactVerify, PactJsonVerify


class Pact:
    # /api/v1/auth接口契约
    api_v1_auth_get_pact = Matcher(
        {
            "msg": "success",
            "code": 0,
            "data": Like({
                "token": 11
            })
        }
    )

    get_httpbin = {
        '$Like':
            {'args':
                {'$Like':
                    {'age': '12', 'name': 'lilei'}},
                    'headers': {'$Like': {'Accept': '*/*',
                                          'Accept-Encoding': 'gzip, deflate, br',
                                          'Cache-Control': 'no-cache',
                                          'Content-Type': 'application/json',
                                          'Host': 'httpbin.org',
                                          'Postman-Token': '786bc8bc-8e88-4147-8911-6e239ee7b2b6',
                                          'User-Agent': 'PostmanRuntime/7.26.8',
                                          'X-Amzn-Trace-Id': 'Root=1-613cb023-5a5124c61aa93ba10d3600b0'}},
             'origin': '115.197.80.131',
             'url': 'http://httpbin.org/get?name=lilei&age=12'}}

