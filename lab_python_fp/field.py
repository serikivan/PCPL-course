
def field(dicts, *args):
    result = []
    for i in dicts:
        if len(args) == 1:
            if i[args[0]]:
                result.append(i[args[0]])
        else:
            tmp = dict()
            for j in args:
                if i[j]:
                    tmp[j] = i[j]
            result.append(tmp)
    print(result)

if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    field(goods, 'title') # 'Ковер', 'Диван для отдыха'
    field(goods, 'title', 'price') # [{'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}]