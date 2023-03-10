def next_index(text=str, display_length=int):
    num = 0
    to_show = list(' ' * display_length)
    while True:
        iterable_text = iter(text)
        while True:
            try:
                to_show[num] = next(iterable_text)
            except StopIteration:
                to_show = list('THE END')
                num = 0
                while len(to_show)<display_length:
                    to_show = ['-'] + to_show + ['-']
                yield ''.join(to_show), num
                yield ''.join(to_show), num
                yield ''.join(to_show), num
                break
            if num < display_length - 1:
                num += 1
            else:
                num = 0
            to_show[num] = '_'
            yield ''.join(to_show), num

if __name__ == '__main__':
    from time import sleep
    a=next_index('gdsidhsudahsdjaodjosadf',15)
    while True:
        try:
            sleep(0.05)
            print(next(a))
        except KeyboardInterrupt:
            print(id(a))
            a=next_index('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',15)
            print(id(a))