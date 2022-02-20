def solution(id_list, report, k):
    answer = []
    report_count = []
    re = {}
    reverse ={}
    for i in range(len(report)):
        reporter, reported = map(str,report[i].split())
        if reported in re:
            if reporter in re[reported]:
                continue
            else:
                re[reported].append(reporter)
        else:
            re[reported]=[reporter]

        if reporter in reverse:
            if reported in reverse[reporter]:
                continue
            else:
                reverse[reporter].append(reported)
        else:
            reverse[reporter]=[reported]

    val = list(re.values())
    for i in range(len(id_list)):
        if id_list[i] in re:
            if len(re[id_list[i]])>=k:
                report_count.append(id_list[i])


    cnt=0
    r={}
    for i in range(len(id_list)):
        r[id_list[i]]=0

    for i in range(len(id_list)):
        for j in range(len(report_count)):
            if id_list[i] in reverse:
                if report_count[j] in reverse[id_list[i]]:
                    r[id_list[i]] += 1

    answer = list(r.values())
    return answer