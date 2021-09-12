# import json
# from httprunner import __version__
# from pactverify.matchers import Matcher, Like, EachLike, Term, Enum, PactVerify, PactVerifyError,PactJsonVerify
# from pacts import Pact
from deepdiff import DeepDiff
from mongo_util import MongoUtil

mogo = MongoUtil()

# def pactverify(response, pact_name):
#     if not hasattr(Pact, pact_name):
#         raise PactVerifyError('{}契约未找到'.format(pact_name))
#
#     rsp_json = response.resp_obj.json()
#     expect_format = getattr(Pact, pact_name)
#     mPactVerify = PactVerify(expect_format)
#     mPactVerify.verify(rsp_json)
#     response.verify_result = mPactVerify.verify_result
#     response.verify_info = mPactVerify.verify_info


# def json_pact_v(response, pact_name):
#     if not hasattr(Pact, pact_name):
#         raise PactVerifyError('{}契约未找到'.format(pact_name))
#     rsp_json = response.resp_obj.json()
#     expect_format = getattr(Pact, pact_name)
#     mPactJsonVerify = PactJsonVerify(expect_format, hard_mode=True, separator='$')
#     mPactJsonVerify.verify(rsp_json)
#     response.verify_result = mPactJsonVerify.verify_result
#     response.verify_info = mPactJsonVerify.verify_info


def json_diff(response):
    request = response.request
    actual_json = response.resp_obj.json()

    # 1 获取url, http方法和入参

    # if type(request.body) is bytes:
    #     body = str(request.body, encoding="utf8")
    #     key = request.method + request.path_url + body
    # if type(request.body) is str:
    #     key = request.method + request.path_url + request.body

    if request.headers["Content-Type"] == "application/json":
        body = str(request.body, encoding="utf8")
        key = request.method + request.path_url + body
    else:
        key = request.method + request.path_url + request.body
    expect_json = mogo.find_one(key)
    if expect_json is None:
        temp = {"req": key, "res": actual_json}
        mogo.insert_one(temp)
        response.verify_result = True
        response.verify_info = {}
    else:

        difference = DeepDiff(expect_json["res"], actual_json, exclude_paths=[r"root['headers']['X-Amzn-Trace-Id']"])
        response.verify_result = (difference == {})
        response.verify_info = difference


