Title: Quick Tip Post #3 - cURL, JSON and Python
Date: 2015-07-29 11:00
Category: Old
Tags: quick tips,python
Slug: quick-tip-post-3-curl
Authors: easydevmixin
Summary: Using cURL to get JSON responses and pretty-printing them with Python
Status: published

Today I’ve been using cURL for testing an endpoint I’m developing with Django. The answer of the endpoint is in json format, so sometimes it is hard to read its output. Luckily Python has a module (`json.tools`) which can help us in that situation.

This is the output without using `json.tools`:

    easydevmixin@bimbolane $ curl http://192.168.33.11:8000/api/v1/env/DEMO/uptime
    [{"DEMO":{"0":{"2014-7":99.99},"1":{"2014-8":100.0},"2":{"2014-9":99.7},"3":{"2014-10":99.96},"4":{"2014-11":100.0},"5":{"2014-12":100.0},"6":{"2015-1":99.9},"7":{"2015-2":100.0},"8":{"2015-3":100.0},"9":{"2015-4":100.0},"10":{"2015-5":100.0},"11":{"2015-6":100.0}}}]

Hard to read, isn’t it?

This is the output using the module:

    easydevmixin@bimbolane $ curl http://192.168.33.11:8000/api/v1/env/DEMO/uptime | python -m json.tool
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100   268    0   268    0     0   1234      0 --:--:-- --:--:-- --:--:--  1240
    [
        {
            "NA1": {
                "0": {
                    "2014-7": 99.99
                },
                "1": {
                    "2014-8": 99.97
                },
                "10": {
                    "2015-5": 99.95
                },
                "11": {
                    "2015-6": 99.96
                },
                "2": {
                    "2014-9": 99.87
                },
                "3": {
                    "2014-10": 100.0
                },
                "4": {
                    "2014-11": 100.0
                },
                "5": {
                    "2014-12": 100.0
                },
                "6": {
                    "2015-1": 100.0
                },
                "7": {
                    "2015-2": 99.99
                },
                "8": {
                    "2015-3": 100.0
                },
                "9": {
                    "2015-4": 100.0
                }
            }
        }
    ]

You can use this ‘trick’ with Python >= 2.6 and Python 3 also. Until now the only handicap I’ve found is that `json.tools` sorts outs the JSON keys, and this is something you want to take care about.

Cheers!
