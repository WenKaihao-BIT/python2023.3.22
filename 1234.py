


data='VEABS 0.176 1.525 <64>\r\n-->\nPFB<D8>\r\n0.112 [mm]\r\n-->MOVEABS 0.205 1.374 <5F>\r\n-->\nMOVEABS 0.231'


def DataAnlysis(self, data, head):
    data2 = data.split('\n')
    print(data2)
    matched_index = -1
    i = 0
    length = len(data2)
    while i < length:
        if head+'\r' == data2[i]:
            matched_index = i
            break
        i = i + 1
    if matched_index != -1:
        data3 = data2[matched_index + 1].split(' ')[0]
        return data3
    return 'error'

if __name__ == '__main__':
    self=[]
    # print(data,end='')
    print(DataAnlysis(self,data,'PFB<D8>'))
    # print('\n'.encode().hex())