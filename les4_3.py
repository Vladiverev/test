myParams = {"server": "mpilgrim",
            "database": "master",
            "uid": "sa",
            "pwd": "secret"}

print(';'.join(["{}={}".format(k, v) for k, v in myParams.items()]))
