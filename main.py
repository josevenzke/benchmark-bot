from benchmark import Benchmark

def main():
    bench = Benchmark()
    while True:
        option = input('1 - memory \n2- reaction')
        if option == '1':
            times = input('quantas vezes?')
            bench.memory(int(times))
        
        if option == '2':
            bench.reaction()


if __name__ == '__main__':
    main()