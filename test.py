def compareVersion(version1, version2):
    v1List = [int(x) for x in version1.split('.')]
    v2List = [int(x) for x in version2.split('.')]
    minLen = min(len(v2List), len(v1List))
    for i in range(minLen):
        if v1List[i] > v2List[i]:
            return 1
        elif v1List[i] < v2List[i]:
            return -1
    sumV1 = sum(v1List[minLen:])
    sumV2 = sum(v2List[minLen:])
    if sumV1 == sumV2:
        return 0
    elif sumV1 > sumV2:
        return 1
    return -1


if __name__ == '__main__':
    r = compareVersion('1.0', '1.0.0')
    print(r)
